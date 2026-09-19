#!/usr/bin/env python3
"""Comprueba que cada skill del repositorio tiene su procedencia registrada y que los archivos
de terceros siguen siendo idénticos a los que se verificaron.

  python3 scripts/procedencia.py comprobar   # sin red: registro, hashes, README y homepage
  python3 scripts/procedencia.py remoto      # con red: compara contra la API de ClawHub
"""
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

TIPOS = {"comunidad", "derivada", "propia"}
EXCLUIDOS = {"_meta.json"}
ORIGENES_AJENOS = re.compile(r"clawic\.com|clawhub\.ai")


def sha256(ruta):
    return hashlib.sha256(ruta.read_bytes()).hexdigest()


def archivos_de(carpeta):
    """Todos los archivos de una skill, salvo los que genera el propio registro."""
    salida = {}
    for p in sorted(carpeta.rglob("*")):
        if not p.is_file() or ".clawhub" in p.relative_to(carpeta).parts or p.name in EXCLUIDOS:
            continue
        salida[p.relative_to(carpeta).as_posix()] = sha256(p)
    return salida


def frontmatter(texto):
    m = re.match(r"---\n(.*?)\n---", texto, re.S)
    return dict(re.findall(r"^([A-Za-z_-]+):\s*(.+)$", m.group(1), re.M)) if m else {}


def carpetas_con_skill(raiz):
    return sorted(p.parent.relative_to(raiz).as_posix() for p in raiz.rglob("SKILL.md") if ".git" not in p.parts)


def comprobar(raiz):
    """Devuelve la lista de problemas; vacía si todo coincide."""
    raiz = Path(raiz)
    errores = []
    registro = json.loads((raiz / "procedencia.json").read_text(encoding="utf-8"))
    skills = {s["ruta"]: s for s in registro["skills"]}
    reales = set(carpetas_con_skill(raiz))
    for ruta in sorted(reales - skills.keys()):
        errores.append(f"{ruta}: existe la skill pero no está en procedencia.json")
    for ruta in sorted(skills.keys() - reales):
        errores.append(f"{ruta}: está en procedencia.json pero no existe la carpeta")
    readmes = {n: (raiz / n).read_text(encoding="utf-8") for n in ("README.md", "README.es.md")}
    for ruta, s in sorted(skills.items()):
        if ruta not in reales:
            continue
        if s.get("tipo") not in TIPOS:
            errores.append(f"{ruta}: tipo inválido '{s.get('tipo')}'")
            continue
        carpeta = raiz / ruta
        if s["tipo"] in ("comunidad", "derivada"):
            esperado, actual = s.get("archivos", {}), archivos_de(carpeta)
            for rel in sorted(esperado.keys() | actual.keys()):
                if rel not in actual:
                    errores.append(f"{ruta}/{rel}: falta el archivo registrado")
                elif rel not in esperado:
                    errores.append(f"{ruta}/{rel}: archivo nuevo sin registrar")
                elif esperado[rel] != actual[rel]:
                    errores.append(f"{ruta}/{rel}: cambió respecto al hash registrado")
            if s["tipo"] == "derivada" and not s.get("modificados"):
                errores.append(f"{ruta}: una skill derivada debe listar qué archivos modificó")
            if not all(k in s for k in ("autor", "slug", "version", "url")):
                errores.append(f"{ruta}: faltan autor, slug, versión o URL de origen")
        else:
            fm = frontmatter((carpeta / "SKILL.md").read_text(encoding="utf-8"))
            if ORIGENES_AJENOS.search(fm.get("homepage", "")):
                errores.append(f"{ruta}: skill propia con homepage de otro origen ({fm['homepage']})")
            ins = s.get("inspirada_en")
            if ins and not str(ins.get("url", "")).startswith("https://"):
                errores.append(f"{ruta}: inspirada_en sin URL https")
        if s["tipo"] == "derivada":
            fm = frontmatter((carpeta / "SKILL.md").read_text(encoding="utf-8"))
            if "clawic.com" in fm.get("homepage", ""):
                errores.append(f"{ruta}: skill derivada con homepage de clawic.com que no existe")
        nombre = ruta.split("/")[-1]
        for archivo, texto in readmes.items():
            if f"`{nombre}`" not in texto and f"({ruta}/" not in texto and f"`{ruta}`" not in texto:
                errores.append(f"{ruta}: no aparece en {archivo}")
    return errores


def remoto(raiz, abrir=urllib.request.urlopen):
    """Compara los archivos de terceros con los publicados en ClawHub (necesita red)."""
    raiz = Path(raiz)
    registro = json.loads((raiz / "procedencia.json").read_text(encoding="utf-8"))
    errores = []
    for s in registro["skills"]:
        if s["tipo"] != "comunidad":
            continue
        for rel, esperado in s["archivos"].items():
            url = (f"{registro['registro']}/api/v1/skills/{s['slug']}/file?path={urllib.parse.quote(rel)}"
                   f"&version={s['version']}&owner={s['autor']}")
            try:
                with abrir(urllib.request.Request(url, headers={"User-Agent": "openclaw-skills-procedencia"}), timeout=30) as r:
                    cuerpo = r.read()
            except Exception as e:  # noqa: BLE001 - cualquier fallo de red es un problema a informar
                errores.append(f"{s['ruta']}/{rel}: no se pudo consultar ClawHub ({e})")
                continue
            if hashlib.sha256(cuerpo).hexdigest() != esperado:
                errores.append(f"{s['ruta']}/{rel}: ya no coincide con ClawHub {s['autor']}/{s['slug']}@{s['version']}")
    return errores


def main(argv):
    if len(argv) != 2 or argv[1] not in ("comprobar", "remoto"):
        print(__doc__)
        return 2
    raiz = Path(__file__).resolve().parent.parent
    errores = comprobar(raiz) if argv[1] == "comprobar" else remoto(raiz)
    for e in errores:
        print(f"ERROR {e}")
    if not errores:
        print("Procedencia correcta.")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
