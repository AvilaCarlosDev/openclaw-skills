# OpenClaw Skills — coleccion curada

> Skills para [OpenClaw](https://openclaw.ai) reunidas, probadas y organizadas en un solo sitio, con un indice en espanol.

**Este repositorio es una curaduria, no una autoria.** La mayoria de las skills que encontraras aqui fueron escritas por otras personas y publicadas en [ClawHub / clawic.com](https://clawic.com). Lo que aporta este repo es la seleccion, la prueba en uso real, la organizacion por categoria y la documentacion en espanol. Cada skill conserva su frontmatter original con su `homepage` y su autoria.

Si una skill te resulta util, ve a su pagina original y apoya a quien la escribio.

---

## Skills de la comunidad

Publicadas en ClawHub por sus respectivos autores. Aqui solo estan seleccionadas y documentadas.

| Skill | Que hace | Fuente original |
|---|---|---|
| `arch-improver` | Detecta acoplamientos y violaciones de capas en el codebase | [Architecture Improver](https://clawic.com/skills/arch-improver) |
| `chat-to-prd` | Convierte la conversacion actual en un PRD y lo abre como issue | [Chat to PRD](https://clawic.com/skills/chat-to-prd) |
| `code-context` | Entiende codigo desconocido en el contexto del sistema completo | [Code Context](https://clawic.com/skills/code-context) |
| `compressed-mode` | Modo de respuesta comprimido, ~75% menos tokens | [Compressed Mode](https://clawic.com/skills/compressed-mode) |
| `content-marketing` | Calendarios editoriales, embudo y reutilizacion de contenido | [Content Marketing](https://clawic.com/skills/content-marketing) |
| `cybersecurity` | Triage de seguridad, threat modeling e incident reporting | [Cybersecurity](https://clawic.com/skills/cybersecurity) |
| `debug-diagnose` | Loop disciplinado: reproducir, minimizar, hipotetizar, verificar | [Debug Diagnose](https://clawic.com/skills/debug-diagnose) |
| `git-guardrails` | Hooks que bloquean push --force, reset --hard y clean | [Git Guardrails](https://clawic.com/skills/git-guardrails) |
| `graphic-design` | Prototipos, sistemas de diseno y trabajo UI/UX | [Graphic Design Pro](https://clawic.com/skills/graphic-design-pro) |
| `grill-me` | Entrevista implacable sobre un plan hasta cerrar cada decision | [Grill Me](https://clawic.com/skills/grill-me) |
| `grill-with-docs` | Igual que Grill Me, contrastando contra el modelo de dominio | [Grill With Docs](https://clawic.com/skills/grill-with-docs) |
| `issue-triage` | Triage de issues con maquina de estados, labels y routing | [Issue Triage](https://clawic.com/skills/issue-triage) |
| `plan-to-issues` | Parte un plan o PRD en issues independientes por vertical slice | [Plan to Issues](https://clawic.com/skills/plan-to-issues) |
| `programming` | Skill general de desarrollo, debugging y code review | [Programming](https://clawic.com/skills/programming) |
| `quick-prototype` | Prototipos desechables para explorar diseno | [Quick Prototype](https://clawic.com/skills/quick-prototype) |
| `refero-styles` | Extrae colores, tipografia y spacing de un sitio web | [Refero Styles](https://clawic.com/skills/refero-styles) |
| `seo` | Auditoria de sitio, redaccion y analisis de competencia | [SEO](https://clawic.com/skills/seo) |
| `tdd-helper` | Ciclo red-green-refactor por vertical slice | [TDD Helper](https://clawic.com/skills/tdd-helper) |
| `ai-meeting-notes` | Convierte notas de reunion en action items | [jeffjhunter.com](https://jeffjhunter.com) |
| `meeting-notes` | Estructura notas de reunion | Publicada en ClawHub |
| `safe-web` | Navegacion web con proteccion contra prompt injection | Publicada en ClawHub |

---

## Skills propias

Escritas para este repositorio:

| Skill | Que hace |
|---|---|
| `safe_search` | Busqueda web con proteccion contra prompt injection |
| `safe_fetch` | Descarga de paginas con proteccion contra prompt injection |

---

## Como usar una skill

```bash
# desde ClawHub, que es la via recomendada y mantiene la skill actualizada
clawhub install <nombre-del-skill>

# o copiando el SKILL.md a tu workspace
cp <nombre>/SKILL.md ~/.openclaw/workspace/skills/<nombre>/
```

Las skills se activan solas cuando la tarea coincide con su descripcion, o las invocas con `/usa <nombre> <tarea>`.

---

## Licencia y creditos

Cada skill pertenece a quien la escribio y se rige por los terminos de su publicacion original en ClawHub. **Este repositorio no reclama autoria sobre ellas.**

La organizacion, el indice y la documentacion en espanol son de [Carlos Avila](https://github.com/AvilaCarlosDev), bajo MIT.

Si eres autor de alguna skill incluida aqui y quieres que se retire o que cambie la forma en que se te acredita, [abre un issue](https://github.com/AvilaCarlosDev/openclaw-skills/issues) y se resuelve de inmediato.
