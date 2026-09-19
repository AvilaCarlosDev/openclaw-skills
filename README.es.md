# OpenClaw Skills — colección curada (en español)

> Skills para [OpenClaw](https://openclaw.ai) reunidas, probadas y organizadas en un solo sitio. [Read in English](README.md).

Este repositorio tiene **tres tipos de skills, y cada una está etiquetada como lo que realmente es**:

1. **Skills de la comunidad**: archivos publicados en [ClawHub](https://clawhub.ai) por otras personas, copiados aquí byte a byte. ClawHub publica todas sus skills bajo [MIT-0](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md#license), que permite usarlas, modificarlas y redistribuirlas, también con fines comerciales, sin exigir atribución. Igualmente se acreditan, con enlace a su autor.
2. **Skills derivadas**: una skill de ClawHub que se modificó aquí. La modificación se indica.
3. **Skills propias**: escritas para este repositorio. Algunas adaptan el *concepto* de una skill de [mattpocock/skills](https://github.com/mattpocock/skills) (MIT); los textos se reescribieron y tradujeron, no se copia ningún archivo, y cada una lo dice.

De dónde sale cada skill está en [`procedencia.json`](procedencia.json), y la CI lo comprueba (ver [Procedencia y verificación](#procedencia-y-verificación)). Verificado el 2026-09-19.

Si una skill te resulta útil, ve a la página de su autor y apóyalo.

---

## Skills de la comunidad (copiadas sin cambios de ClawHub)

### Varios autores

| Skill | Qué hace | Autor | Original | Versión |
|---|---|---|---|---|
| `ai-meeting-notes` | Convierte notas de reunion en action items | [jeffjhunter](https://clawhub.ai/jeffjhunter) | [ai-meeting-notes](https://clawhub.ai/jeffjhunter/skills/ai-meeting-notes) | 1.0.3 |
| `meeting-notes` | Estructura notas de reunión | [tinadu-ai](https://clawhub.ai/tinadu-ai) | [meeting-notes](https://clawhub.ai/tinadu-ai/skills/meeting-notes) | 1.0.1 |
| `safe-web` | Navegación web con protección contra prompt injection | [adamnaghs](https://clawhub.ai/adamnaghs) | [safe-web](https://clawhub.ai/adamnaghs/skills/safe-web) | 1.0.8 |

### Skills de lenguajes e infraestructura, de [ivangdavila](https://clawhub.ai/ivangdavila)

| Skill | Qué hace | Autor | Original | Versión |
|---|---|---|---|---|
| `content-marketing` | Calendarios editoriales, embudo y reutilización de contenido | [ivangdavila](https://clawhub.ai/ivangdavila) | [content-marketing](https://clawhub.ai/ivangdavila/skills/content-marketing) | 1.0.0 |
| `cybersecurity` | Triage de seguridad, threat modeling e incident reporting | [ivangdavila](https://clawhub.ai/ivangdavila) | [cybersecurity](https://clawhub.ai/ivangdavila/skills/cybersecurity) | 1.0.0 |
| `devops` | Pipelines CI/CD, estrategia de rollout, on-call, SLOs, metricas DORA | [ivangdavila](https://clawhub.ai/ivangdavila) | [devops](https://clawhub.ai/ivangdavila/skills/devops) | 1.0.2 |
| `git` | Conflictos, rebases, historial perdido, hooks, worktrees | [ivangdavila](https://clawhub.ai/ivangdavila) | [git](https://clawhub.ai/ivangdavila/skills/git) | 1.0.12 |
| `nextjs` | App Router, server components, caching, Server Actions, deploy | [ivangdavila](https://clawhub.ai/ivangdavila) | [nextjs](https://clawhub.ai/ivangdavila/skills/nextjs) | 1.1.2 |
| `nginx` | Reverse proxy, terminación SSL, 502/504, WebSockets a traves del proxy | [ivangdavila](https://clawhub.ai/ivangdavila) | [nginx](https://clawhub.ai/ivangdavila/skills/nginx) | 1.0.5 |
| `playwright` | Tests inestables, locators, traces, corridas en CI, control de navegador por MCP | [ivangdavila](https://clawhub.ai/ivangdavila) | [playwright](https://clawhub.ai/ivangdavila/skills/playwright) | 1.0.4 |
| `react` | Hooks, estado, re-renders, hydration mismatches, testing | [ivangdavila](https://clawhub.ai/ivangdavila) | [react](https://clawhub.ai/ivangdavila/skills/react) | 1.0.7 |
| `seo` | Auditoría de sitio, redacción y análisis de competencia | [ivangdavila](https://clawhub.ai/ivangdavila) | [seo](https://clawhub.ai/ivangdavila/skills/seo) | 1.0.3 |
| `sql` | Queries lentas, bugs de JOIN, migraciones, índices, diseño de schema | [ivangdavila](https://clawhub.ai/ivangdavila) | [sql](https://clawhub.ai/ivangdavila/skills/sql) | 1.0.4 |
| `terraform` | HCL, fallos de plan/apply, cirugía de state, drift, pinning de providers | [ivangdavila](https://clawhub.ai/ivangdavila) | [terraform](https://clawhub.ai/ivangdavila/skills/terraform) | 1.0.4 |
| `typescript` | Errores de tipos, narrowing, generics, tsconfig, archivos de declaracion | [ivangdavila](https://clawhub.ai/ivangdavila) | [typescript](https://clawhub.ai/ivangdavila/skills/typescript) | 1.0.5 |

---

## Skills derivadas (modificadas aquí)

| Skill | Qué hace | Basada en | Qué cambió |
|---|---|---|---|
| `graphic-design` | Prototipos, sistemas de diseño y trabajo UI/UX | [ivangdavila/graphic-design@1.0.0](https://clawhub.ai/ivangdavila/skills/graphic-design) | Reescrita como v2.0.0 con las capacidades de Claude Design. |
| `programming` | Skill general de desarrollo, debugging y code review | [leowing/programming@1.0.0](https://clawhub.ai/leowing/skills/programming) | `SKILL.md` reescrito en español; el resto de los archivos son los originales. |

---

## Skills propias

Escritas para este repositorio por [Carlos Avila](https://github.com/AvilaCarlosDev), bajo MIT. **No** vienen de ClawHub. Cuando un concepto coincide con una skill de otro repositorio público, se acredita.

| Skill | Qué hace | Concepto |
|---|---|---|
| `arch-improver` | Detecta acoplamientos y violaciones de capas en el codebase | Concepto adaptado de [mattpocock/skills · improve-codebase-architecture](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) (MIT) |
| `chat-to-prd` | Convierte la conversación actual en un PRD y lo abre como issue | Concepto adaptado de [mattpocock/skills · to-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec) (MIT) |
| `code-context` | Entiende código desconocido en el contexto del sistema completo | — |
| `compressed-mode` | Modo de respuesta comprimido, ~75% menos tokens | — |
| `debug-diagnose` | Loop disciplinado: reproducir, minimizar, hipotetizar, verificar | Concepto adaptado de [mattpocock/skills · diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) (MIT) |
| `git-guardrails` | Hooks que bloquean push --force, reset --hard y clean | Concepto adaptado de [mattpocock/skills · git-guardrails-claude-code](https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code) (MIT) |
| `grill-me` | Entrevista implacable sobre un plan hasta cerrar cada decisión | Concepto adaptado de [mattpocock/skills · grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) (MIT) |
| `grill-with-docs` | Igual que Grill Me, contrastando contra el modelo de dominio | Concepto adaptado de [mattpocock/skills · grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) (MIT) |
| `issue-triage` | Triage de issues con máquina de estados, labels y routing | Concepto adaptado de [mattpocock/skills · triage](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) (MIT) |
| `plan-to-issues` | Parte un plan o PRD en issues independientes por vertical slice | Concepto adaptado de [mattpocock/skills · to-tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets) (MIT) |
| `quick-prototype` | Prototipos desechables para explorar diseño | Concepto adaptado de [mattpocock/skills · prototype](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) (MIT) |
| `refero-styles` | Extrae colores, tipografía y spacing de un sitio web | Idea inspirada en [Refero Styles](https://refero.design) |
| `safe_fetch` | Descarga de páginas con protección contra prompt injection | — |
| `safe_search` | Búsqueda web con protección contra prompt injection | — |
| `tdd-helper` | Ciclo red-green-refactor por vertical slice | Concepto adaptado de [mattpocock/skills · tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) (MIT) |

### Skills propias en español

| Skill | Comando | Qué hace |
|---|---|---|
| [`skills-es/engineering/diagnostico`](skills-es/engineering/diagnostico/SKILL.md) | `/diagnostico` | Depurar bugs difíciles con proceso estructurado: reproducir, minimizar, hipotetizar, instrumentar, fix, regresion |
| [`skills-es/engineering/tdd`](skills-es/engineering/tdd/SKILL.md) | `/tdd` | Desarrollo guiado por tests, ciclo Red-Green-Refactor |
| [`skills-es/github/contribucion`](skills-es/github/contribucion/SKILL.md) | `/contribucion` | Preparar contribuciones a proyectos open source: buscar issue, fix, tests, PR |
| [`skills-es/landings/diseno-profesional`](skills-es/landings/diseno-profesional/SKILL.md) | `/diseno-profesional` | Aplicar principios de diseño de Refero.design a páginas y componentes |
| [`skills-es/ventas/pitch`](skills-es/ventas/pitch/SKILL.md) | `/pitch` | Generar emails de venta personalizados para landing pages, sin sonar a spam |

Estas 5 son las únicas skills en español que existen hoy en este repositorio. (Una versión anterior de este contenido vivía en un repo aparte, `openclaw-skills-es`, que prometía más de una docena adicionales que nunca se escribieron — se eliminó ese repo y se dejaron aquí solo las que son reales.)


---

## Cómo usar una skill

```bash
# desde ClawHub, lo recomendado para las skills de la comunidad, las mantiene al día
clawhub install <nombre-de-la-skill>

# o copiando el SKILL.md (y el resto de la carpeta) a tu workspace
cp -r <nombre> ~/.openclaw/workspace/skills/
# Las skills en español usan la misma ruta relativa: skills-es/<categoría>/<nombre>/
```

Las skills se activan solas cuando una tarea coincide con su descripción, o puedes invocarlas con `/use <nombre> <tarea>`.

Algunas skills incluyen scripts (`safe-web`, `programming`). Léelos antes de ejecutarlos, como con cualquier código que no escribiste.

---

## Procedencia y verificación

`procedencia.json` registra, para cada skill, su tipo, autor, versión, URL de origen y el SHA-256 de cada archivo tomado de un tercero.

```bash
python3 scripts/procedencia.py comprobar   # sin red: registro, hashes, README y homepage coinciden
python3 scripts/procedencia.py remoto      # con red: compara contra lo que ClawHub sirve hoy
```

La primera comprobación corre en cada pull request; la segunda, una vez por semana, porque depende de un servicio externo. Cómo se estableció el origen: cada archivo se pidió a la API pública de ClawHub en la versión exacta y se comparó byte a byte. `_meta.json` y `.clawhub/` los genera el registro y se excluyen.

---

## Licencia y créditos

- **Skills de la comunidad:** © sus autores, publicadas en ClawHub bajo MIT-0. Copiadas sin cambios. Este repositorio no reclama autoría sobre ellas.
- **Skills derivadas:** los archivos originales conservan los términos de su autor (MIT-0); las modificaciones están bajo MIT.
- **Skills propias, curaduría y documentación:** © Carlos Avila, MIT (ver [LICENSE](LICENSE)). Los avisos de terceros están en [NOTICE.md](NOTICE.md).
- Desarrollado con el apoyo de Claude (Anthropic) como asistente de redacción y de verificación de fuentes; la selección y la revisión final son del autor.

Si escribiste una skill incluida aquí y quieres que se quite o se acredite de otra forma, [abre un issue](https://github.com/AvilaCarlosDev/openclaw-skills/issues) y se resuelve de inmediato. Para reportar un problema de seguridad, ver [SECURITY.md](SECURITY.md).
