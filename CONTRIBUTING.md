# Cómo contribuir / Contributing

[Español](#español) · [English](#english)

## Español

Gracias por querer aportar. Este repositorio distingue tres tipos de skills y la regla más importante es **no pasar por propio lo ajeno**.

### Agregar una skill propia

1. Crea la carpeta con su `SKILL.md`. El `homepage` del frontmatter, si lo hay, debe apuntar a este repositorio, no a otro sitio.
2. Agrégala a `procedencia.json` con `"tipo": "propia"`. Si adapta el concepto de otra skill pública, añade `inspirada_en` con su nombre, URL y licencia.
3. Añádela a `README.md` **y** a `README.es.md`.
4. Corre `python3 scripts/procedencia.py comprobar` y `python3 -m unittest discover -s tests -p 'test_*.py'`.

### Agregar una skill de ClawHub

1. Cópiala **sin cambios** desde ClawHub y anota autor, slug y versión.
2. Regístrala con `"tipo": "comunidad"` y el SHA-256 de cada archivo (`archivos`). No modifiques ninguno: la comprobación falla si cambia.
3. Verifica contra la fuente con `python3 scripts/procedencia.py remoto`.

### Modificar una skill de ClawHub

Se permite (MIT-0), pero pasa a `"tipo": "derivada"`, con `modificados` y una `nota` que diga qué cambió y por qué.

### Antes de abrir el pull request

- Sin claves ni tokens reales, ni enlaces de afiliado.
- Los dos README con la misma información.
- Si quitas o acreditas distinto la skill de otra persona, explica el motivo en el pull request.

## English

Thanks for wanting to contribute. This repository tells three kinds of skills apart, and the most important rule is **do not pass off someone else's work as your own**.

### Adding an own skill

1. Create the folder with its `SKILL.md`. Its frontmatter `homepage`, if any, must point to this repository, not to another site.
2. Add it to `procedencia.json` with `"tipo": "propia"`. If it adapts the concept of another public skill, add `inspirada_en` with its name, URL and license.
3. Add it to `README.md` **and** `README.es.md`.
4. Run `python3 scripts/procedencia.py comprobar` and `python3 -m unittest discover -s tests -p 'test_*.py'`.

### Adding a ClawHub skill

1. Copy it **unchanged** from ClawHub and note the author, slug and version.
2. Register it with `"tipo": "comunidad"` and the SHA-256 of every file (`archivos`). Do not modify any: the check fails if one changes.
3. Verify against the source with `python3 scripts/procedencia.py remoto`.

### Modifying a ClawHub skill

Allowed (MIT-0), but it becomes `"tipo": "derivada"`, with `modificados` and a `nota` saying what changed and why.

### Before opening the pull request

- No real keys or tokens, and no affiliate links.
- Both READMEs carrying the same information.
- If you remove or credit differently someone else's skill, explain why in the pull request.
