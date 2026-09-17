# OpenClaw Skills — coleccion curada (en espanol)

> Skills para [OpenClaw](https://openclaw.ai) reunidas, probadas y organizadas en un solo sitio. [Read in English](README.md).

**Este repositorio es una curaduria, no una autoria** para la mayoria de las skills. La mayoria fueron escritas por otras personas y publicadas en [ClawHub / clawic.com](https://clawic.com). Lo que aporta este repo es la seleccion, la prueba en uso real, la organizacion por categoria y esta documentacion en espanol. Cada skill conserva su frontmatter original con su `homepage` y su autoria.

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
| `meeting-notes` | Estructura notas de reunion | Publicada en ClawHub — autor no identificable, este slug lo comparten 3 autores distintos en ClawHub y no hay forma de confirmar de cual de los 3 viene esta copia |
| `safe-web` | Navegacion web con proteccion contra prompt injection | [adamnaghs](https://clawhub.ai/adamnaghs/skills/safe-web) |

### Skills de lenguajes e infraestructura, de [ivangdavila](https://clawhub.ai/ivangdavila)

Nueve skills detalladas "que hacer cuando X se rompe" del mismo autor, agregadas porque coinciden con el stack de este repo (Next.js/TypeScript/React) y con el enfoque de evitar fallas reales y especificas en vez de tutoriales genericos.

| Skill | Que hace | Fuente original |
|---|---|---|
| `typescript` | Errores de tipos, narrowing, generics, tsconfig, archivos de declaracion | [TypeScript](https://clawic.com/skills/typescript) |
| `nextjs` | App Router, server components, caching, Server Actions, deploy | [NextJS](https://clawic.com/skills/nextjs) |
| `react` | Hooks, estado, re-renders, hydration mismatches, testing | [React](https://clawic.com/skills/react) |
| `sql` | Queries lentas, bugs de JOIN, migraciones, indices, diseno de schema | [SQL](https://clawic.com/skills/sql) |
| `git` | Conflictos, rebases, historial perdido, hooks, worktrees | [Git](https://clawic.com/skills/git) |
| `nginx` | Reverse proxy, terminacion SSL, 502/504, WebSockets a traves del proxy | [Nginx](https://clawic.com/skills/nginx) |
| `devops` | Pipelines CI/CD, estrategia de rollout, on-call, SLOs, metricas DORA | [DevOps](https://clawic.com/skills/devops) |
| `terraform` | HCL, fallos de plan/apply, cirugia de state, drift, pinning de providers | [Terraform](https://clawic.com/skills/terraform) |
| `playwright` | Tests inestables, locators, traces, corridas en CI, control de navegador por MCP | [Playwright](https://clawic.com/skills/playwright) |

---

## Skills propias en espanol

Escritas originalmente en espanol por [Carlos Avila](https://github.com/AvilaCarlosDev) para este repositorio. No son traducciones de las skills de la tabla anterior; son contenido propio, incluso cuando cubren un tema parecido (por ejemplo `skills-es/landings/diseno-profesional` es una toma independiente sobre extraccion de estilos, escrita en paralelo a `refero-styles`).

| Skill | Comando | Que hace |
|---|---|---|
| [`skills-es/engineering/diagnostico`](skills-es/engineering/diagnostico/SKILL.md) | `/diagnostico` | Depurar bugs dificiles con proceso estructurado: reproducir, minimizar, hipotetizar, instrumentar, fix, regresion |
| [`skills-es/engineering/tdd`](skills-es/engineering/tdd/SKILL.md) | `/tdd` | Desarrollo guiado por tests, ciclo Red-Green-Refactor |
| [`skills-es/github/contribucion`](skills-es/github/contribucion/SKILL.md) | `/contribucion` | Preparar contribuciones a proyectos open source: buscar issue, fix, tests, PR |
| [`skills-es/landings/diseno-profesional`](skills-es/landings/diseno-profesional/SKILL.md) | `/diseno-profesional` | Aplicar principios de diseno de Refero.design a paginas y componentes |
| [`skills-es/ventas/pitch`](skills-es/ventas/pitch/SKILL.md) | `/pitch` | Generar emails de venta personalizados para landing pages, sin sonar a spam |

Estas 5 son las unicas skills en espanol que existen hoy en este repositorio. (Una version anterior de este contenido vivia en un repo aparte, `openclaw-skills-es`, que prometia mas de una docena adicionales que nunca se escribieron — se elimino ese repo y se dejaron aqui solo las que son reales.)

---

## Skills propias (sin idioma especifico)

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
# las skills en espanol usan la misma ruta relativa: skills-es/<categoria>/<nombre>/SKILL.md
```

Las skills se activan solas cuando la tarea coincide con su descripcion, o las invocas con `/usa <nombre> <tarea>`.

---

## Licencia y creditos

Cada skill de la seccion "comunidad" pertenece a quien la escribio y se rige por los terminos de su publicacion original en ClawHub. **Este repositorio no reclama autoria sobre ellas.**

Las skills de `skills-es/` y la organizacion/documentacion del repo son de [Carlos Avila](https://github.com/AvilaCarlosDev), bajo MIT.

Si eres autor de alguna skill incluida aqui y quieres que se retire o que cambie la forma en que se te acredita, [abre un issue](https://github.com/AvilaCarlosDev/openclaw-skills/issues) y se resuelve de inmediato.
