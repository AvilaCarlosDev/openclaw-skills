import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import procedencia  # noqa: E402

HASH = procedencia.hashlib.sha256


def skill(carpeta, extra="", homepage=None):
    carpeta.mkdir(parents=True, exist_ok=True)
    fm = "---\nname: x\n" + (f"homepage: {homepage}\n" if homepage else "") + "---\n"
    (carpeta / "SKILL.md").write_text(fm + "cuerpo" + extra, encoding="utf-8")


def registro(raiz, skills):
    (raiz / "procedencia.json").write_text(json.dumps({"version": 1, "skills": skills}), encoding="utf-8")


def repo_valido(raiz):
    skill(raiz / "ajena")
    skill(raiz / "mia", homepage="https://github.com/AvilaCarlosDev/openclaw-skills")
    (raiz / "README.md").write_text("`ajena` `mia`", encoding="utf-8")
    (raiz / "README.es.md").write_text("`ajena` `mia`", encoding="utf-8")
    registro(raiz, [
        {"ruta": "ajena", "tipo": "comunidad", "autor": "a", "slug": "ajena", "version": "1.0.0", "url": "https://clawhub.ai/a/skills/ajena",
         "archivos": procedencia.archivos_de(raiz / "ajena")},
        {"ruta": "mia", "tipo": "propia"},
    ])


class Comprobar(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        repo_valido(self.tmp)

    def test_un_repositorio_coherente_no_da_errores(self):
        self.assertEqual(procedencia.comprobar(self.tmp), [])

    def test_detecta_un_archivo_de_terceros_modificado(self):
        (self.tmp / "ajena" / "SKILL.md").write_text("otro", encoding="utf-8")
        self.assertTrue(any("cambió respecto al hash" in e for e in procedencia.comprobar(self.tmp)))

    def test_detecta_un_archivo_nuevo_dentro_de_una_skill_de_terceros(self):
        (self.tmp / "ajena" / "extra.sh").write_text("echo", encoding="utf-8")
        self.assertTrue(any("archivo nuevo sin registrar" in e for e in procedencia.comprobar(self.tmp)))

    def test_detecta_un_archivo_registrado_que_falta(self):
        extra = self.tmp / "ajena" / "guia.md"
        extra.write_text("guía", encoding="utf-8")
        reg = json.loads((self.tmp / "procedencia.json").read_text())
        reg["skills"][0]["archivos"] = procedencia.archivos_de(self.tmp / "ajena")
        (self.tmp / "procedencia.json").write_text(json.dumps(reg), encoding="utf-8")
        self.assertEqual(procedencia.comprobar(self.tmp), [])
        extra.unlink()
        self.assertTrue(any("guia.md: falta el archivo registrado" in e for e in procedencia.comprobar(self.tmp)))

    def test_ignora_metadatos_del_registro_de_origen(self):
        (self.tmp / "ajena" / "_meta.json").write_text("{}", encoding="utf-8")
        (self.tmp / "ajena" / ".clawhub").mkdir()
        (self.tmp / "ajena" / ".clawhub" / "origin.json").write_text("{}", encoding="utf-8")
        self.assertEqual(procedencia.comprobar(self.tmp), [])

    def test_detecta_una_skill_sin_registrar(self):
        skill(self.tmp / "nueva")
        self.assertTrue(any("nueva: existe la skill pero no está" in e for e in procedencia.comprobar(self.tmp)))

    def test_detecta_una_entrada_sin_carpeta(self):
        shutil.rmtree(self.tmp / "mia")
        self.assertTrue(any("mia: está en procedencia.json pero no existe" in e for e in procedencia.comprobar(self.tmp)))

    def test_una_skill_propia_no_puede_tener_homepage_de_otro_origen(self):
        skill(self.tmp / "mia", homepage="https://clawic.com/skills/mia")
        self.assertTrue(any("homepage de otro origen" in e for e in procedencia.comprobar(self.tmp)))

    def test_una_derivada_debe_listar_lo_que_modifico(self):
        s = json.loads((self.tmp / "procedencia.json").read_text())
        s["skills"][0]["tipo"] = "derivada"
        (self.tmp / "procedencia.json").write_text(json.dumps(s), encoding="utf-8")
        self.assertTrue(any("debe listar qué archivos modificó" in e for e in procedencia.comprobar(self.tmp)))

    def test_cada_skill_debe_aparecer_en_los_dos_readme(self):
        (self.tmp / "README.es.md").write_text("`ajena`", encoding="utf-8")
        self.assertTrue(any("mia: no aparece en README.es.md" in e for e in procedencia.comprobar(self.tmp)))

    def test_tipo_desconocido(self):
        s = json.loads((self.tmp / "procedencia.json").read_text())
        s["skills"][1]["tipo"] = "robada"
        (self.tmp / "procedencia.json").write_text(json.dumps(s), encoding="utf-8")
        self.assertTrue(any("tipo inválido" in e for e in procedencia.comprobar(self.tmp)))


class Remoto(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        repo_valido(self.tmp)
        s = json.loads((self.tmp / "procedencia.json").read_text())
        s["registro"] = "https://clawhub.ai"
        (self.tmp / "procedencia.json").write_text(json.dumps(s), encoding="utf-8")

    class Respuesta:
        def __init__(self, cuerpo): self.cuerpo = cuerpo
        def read(self): return self.cuerpo
        def __enter__(self): return self
        def __exit__(self, *a): return False

    def test_coincide_cuando_ClawHub_devuelve_el_mismo_contenido(self):
        original = (self.tmp / "ajena" / "SKILL.md").read_bytes()
        self.assertEqual(procedencia.remoto(self.tmp, lambda req, timeout: self.Respuesta(original)), [])

    def test_avisa_cuando_ClawHub_ya_no_coincide(self):
        errores = procedencia.remoto(self.tmp, lambda req, timeout: self.Respuesta(b"cambiado"))
        self.assertTrue(any("ya no coincide con ClawHub a/ajena@1.0.0" in e for e in errores))

    def test_avisa_cuando_no_puede_consultar(self):
        def falla(req, timeout): raise OSError("sin red")
        self.assertTrue(any("no se pudo consultar" in e for e in procedencia.remoto(self.tmp, falla)))

    def test_la_consulta_lleva_autor_version_y_ruta(self):
        vistas = []
        def abrir(req, timeout):
            vistas.append(req.full_url)
            return self.Respuesta((self.tmp / "ajena" / "SKILL.md").read_bytes())
        procedencia.remoto(self.tmp, abrir)
        self.assertEqual(vistas, ["https://clawhub.ai/api/v1/skills/ajena/file?path=SKILL.md&version=1.0.0&owner=a"])


if __name__ == "__main__":
    unittest.main()
