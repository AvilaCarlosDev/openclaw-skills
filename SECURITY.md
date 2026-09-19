# Política de seguridad / Security policy

[Español](#español) · [English](#english)

## Español

Este repositorio reúne instrucciones y algunos scripts que un agente de IA puede leer y ejecutar. Por eso lo que puede ser un problema de seguridad es:

- una **skill con instrucciones maliciosas** (por ejemplo, que pida enviar secretos a un tercero, desactivar protecciones o ejecutar comandos ocultos);
- un **script peligroso** (`safe-web/scripts/`, `programming/skill.sh` u otro) o un enlace a un sitio malicioso;
- **credenciales o claves** incluidas por error en un commit;
- una **atribución o licencia falsa** que haga pasar por propio el trabajo ajeno.

### Cómo reportar

Usa el aviso privado de vulnerabilidades de GitHub: <https://github.com/AvilaCarlosDev/openclaw-skills/security/advisories/new>. Si solo es un error de atribución o quieres que se quite o se acredite tu skill, abre un issue normal.

No incluyas claves reales en el reporte. Solo se mantiene la rama `main`.

### Qué se comprueba

`python3 scripts/procedencia.py comprobar` corre en cada pull request y falla si el contenido de una skill de terceros cambió respecto al hash registrado. Además hay un escaneo de secretos (gitleaks) sobre todo el historial. Las skills de la comunidad son copias sin cambios de ClawHub: si encuentras algo peligroso en una, además de reportarlo aquí, avisa a su autor en ClawHub.

## English

This repository gathers instructions and a few scripts that an AI agent can read and run. So what can be a security problem is:

- a **skill with malicious instructions** (for example, one that asks to send secrets to a third party, turn off protections or run hidden commands);
- a **dangerous script** (`safe-web/scripts/`, `programming/skill.sh` or another) or a link to a malicious site;
- **credentials or keys** committed by mistake;
- a **false attribution or license** that passes off someone else's work as our own.

### Reporting

Use GitHub's private vulnerability reporting: <https://github.com/AvilaCarlosDev/openclaw-skills/security/advisories/new>. If it is only an attribution mistake, or you want your skill removed or credited differently, open a regular issue.

Do not include real keys in the report. Only the `main` branch is maintained.

### What is checked

`python3 scripts/procedencia.py comprobar` runs on every pull request and fails if a third-party skill's content changed from its recorded hash. There is also a secret scan (gitleaks) over the whole history. Community skills are unchanged copies from ClawHub: if you find something dangerous in one, besides reporting it here, tell its author on ClawHub.
