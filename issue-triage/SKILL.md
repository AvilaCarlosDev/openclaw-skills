---
name: Issue Triage
slug: issue-triage
version: 1.0.0
homepage: https://clawic.com/skills/issue-triage
description: "Triage de issues mediante máquina de estados con roles de triage, labels y routing automático."
changelog: "Skill inicial para gestión sistemática de issues en OpenClaw."
metadata: {"clawdbot":{"emoji":"📋","requires":{"bins":["gh"]},"os":["linux","darwin","win32"],"configPaths":["~/issue-triage/"]}}
---

## When to Use

Usa este skill cuando:
- Hay una bandeja de entrada de issues sin procesar
- Necesitas clasificar y priorizar issues nuevos
- Quieres rutear issues a las personas/colas correctas
- Para mantener el backlog limpio y accionable

## Architecture

Memoria vive en `~/issue-triage/`.

```
~/issue-triage/
├── memory.md        # Configuración, labels, workflows
├── queue.md         # Issues en triage pendiente
├── decisions.md     # Decisiones de triage tomadas
└── templates.md     # Templates de respuestas comunes
```

## Triage State Machine

### Estados del Issue

```
[NUEVO] → [EN_TRIAGE] → [ACCIONABLE] → [ASIGNADO] → [EN_PROGRESO] → [HECHO]
                     ↓
               [BLOQUEADO] → [DES_BLOQUEADO] → [EN_PROGRESO]
                     ↓
               [NEEDS_INFO] → [INFO_RECIBIDA] → [EN_TRIAGE]
                     ↓
               [DUPLICADO] → [CERRADO]
                     ↓
               [NO_ES_BUG] → [CERRADO]
                     ↓
               [WONT_FIX] → [CERRADO]
```

### Labels Requeridos

**Prioridad:**
- `P0-critical` - Producción rota, fix inmediato
- `P1-high` - Importante, próximo sprint
- `P2-medium` - Normal, backlog priorizado
- `P3-low` - Nice to have, cuando haya tiempo

**Tipo:**
- `bug` - Algo no funciona como debería
- `feature` - Nueva funcionalidad
- `enhancement` - Mejora de algo existente
- `docs` - Documentación
- `question` - Pregunta, no es un issue accionable
- `discussion` - Necesita discusión antes de acción

**Estado:**
- `triage-needed` - Recién creado, necesita clasificación
- `ready` - Claro, estimado, listo para tomar
- `blocked` - Esperando algo externo
- `needs-info` - Esperando información del reporter

**Área (opcional, según proyecto):**
- `frontend`, `backend`, `devops`, `security`, `ux`, etc.

## Triage Workflow

### 🔍 PASO 1: EVALUAR NUEVO ISSUE

**Checklist de evaluación:**

```
[ ] ¿El título describe el problema/feature?
[ ] ¿La descripción incluye contexto suficiente?
[ ] ¿Hay pasos de reproducción (si es bug)?
[ ] ¿Hay comportamiento esperado vs obtenido?
[ ] ¿Hay screenshots/logs si aplica?
[ ] ¿El reporter es identificable?
```

**Si falta información →** Aplica label `needs-info` y comenta:

> "Gracias por reportar. Para poder ayudarte, necesitamos:
> - [Información específica que falta]
> 
> Una vez que tengamos esto, podremos investigar. ¡Gracias!"

### 🎯 PASO 2: CLASIFICAR

**Determina tipo:**
- ¿Es un bug? → `bug`
- ¿Es feature nueva? → `feature`
- ¿Es mejora? → `enhancement`
- ¿Es pregunta? → `question`

**Determina prioridad:**

| Criterio | P0 | P1 | P2 | P3 |
|----------|----|----|----|----|
| Impacto usuarios | Todos | Muchos | Algunos | Pocos |
| Severidad | Producción rota | Feature rota | Bug molesto | Cosmetic |
| Urgencia | Ahora | Este sprint | Próximo sprint | Backlog |

**Determina área:**
- Basado en el componente afectado
- Asigna label de área correspondiente

### 🔄 PASO 3: RUTEAR

**Opciones de routing:**

1. **Asignar directamente** (si sabes quién debe tomarlo)
   - `gh issue edit <number> --assignee <user>`

2. **Marcar como ready** (para que alguien tome del backlog)
   - `gh issue edit <number> --remove-label triage-needed --add-label ready`

3. **Necesita discusión** (si es complejo o ambiguo)
   - Agenda para próxima reunión de planning
   - Label: `discussion`

4. **No es para este repo**
   - Transfiere: `gh issue transfer <number> <repo>`
   - O cierra con explicación amable

### 📝 PASO 4: DOCUMENTAR DECISIÓN

**Comenta en el issue:**

```
## 📋 Decisión de Triage

**Tipo:** bug | feature | enhancement
**Prioridad:** P0 | P1 | P2 | P3
**Área:** frontend | backend | etc.
**Estado:** ready | blocked | needs-info

**Próximos pasos:**
- [ ] ...

**Notas:**
- ...
```

**Actualiza `decisions.md`:**

```markdown
## YYYY-MM-DD - Issue #NNN

**Decisión:** [resumen]
**Razonamiento:** [por qué]
**Seguimiento:** [qué se necesita]
```

## Casos Especiales

### 🐛 Bug Reports

**Requiere:**
- Pasos de reproducción (mínimo 3 pasos)
- Comportamiento esperado
- Comportamiento obtenido
- Entorno (OS, browser, versión)

**Si no tiene →** `needs-info`

### 💡 Feature Requests

**Evalúa:**
- ¿Está alineado con la visión del producto?
- ¿Cuántos usuarios lo necesitan?
- ¿Hay workaround actual?
- ¿Cuál es el valor vs esfuerzo?

**Si es vago →** Pide más contexto:
> "¿Puedes describir el caso de uso? ¿Quién usaría esto y por qué?"

### ❓ Questions

**Si es pregunta sobre cómo usar:**
- Responde si es rápido
- Si es complejo → sugiere Discussions o Stack Overflow
- Cierra con: `gh issue close <number>`

### 🔁 Duplicados

**Busca issues similares antes de clasificar:**
- Busca por palabras clave del título
- Revisa issues cerrados también

**Si es duplicado →**
> "Este parece duplicado de #XXX. Vamos a cerrar este y continuar la discusión allí."
> `gh issue close <number>`

## Automation Helpers

### Comandos gh útiles

```bash
# Listar issues nuevos
gh issue list --label triage-needed --state open

# Ver detalles de un issue
gh issue view <number>

# Añadir labels
gh issue edit <number> --add-label P1-high,bug,frontend

# Asignar
gh issue edit <number> --assignee @me

# Transferir
gh issue transfer <number> owner/repo

# Cerrar
gh issue close <number>

# Comentar
gh issue comment <number> --body "Texto"
```

### Templates de Respuestas

**needs-info:**
```
Gracias por reportar. Para investigar, necesitamos:

- [información específica]

Una vez que lo tengamos, podremos avanzar. ¡Gracias!
```

**duplicate:**
```
Este parece duplicado de #[número]. Cerramos este y continuamos allí.
```

**wont-fix:**
```
Gracias por la sugerencia. Después de evaluar, no planeamos implementar esto porque:

- [razón 1]
- [razón 2]

Si hay más demanda de la comunidad, podemos reconsiderar.
```

## Adapt to the User

- **Para maintainers solitarios:** Sé eficiente, prioriza ruthless, cierra lo que no acciona
- **Para equipos grandes:** Documenta decisiones, usa labels consistentemente, rutear claro
- **Para proyectos open source:** Sé amable, explica decisiones, guía a nuevos contributors
- **Para empresas:** Alinea con SLAs, prioriza por impacto de negocio, documenta para auditoría

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Triage infinito (nunca se cierra) | Issues se acumulan sin acción | Timebox: 15 min por issue máximo |
| Sobre-priorizar (todo es P0) | Nada es prioritario si todo lo es | Máximo 1-2 P0 a la vez |
| No cerrar issues | Backlog inflado, difícil priorizar | Cierra stale (90 días sin actividad) |
| Triage sin contexto | Decisiones incorrectas | Lee comentarios, historial, código |
| Ignorar al reporter | Comunidad se desmotiva | Responde siempre, aunque sea para cerrar |

## Scope

Este skill SÓLO:
- Clasifica issues nuevos entrantes
- Aplica labels consistentes
- Rutea a personas/colas correctas
- Documenta decisiones de triage

Este skill NUNCA:
- Cierra issues sin evaluación
- Promete timelines sin equipo
- Ignora reportes de seguridad (→ `cybersecurity`)
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/issue-triage/`:

- `memory.md` - Configuración de labels, workflows, equipo
- `queue.md` - Issues pendientes de triage
- `decisions.md` - Historial de decisiones tomadas
- `templates.md` - Templates de respuestas comunes

## Security & Privacy

- Issues de seguridad → NO discutir públicamente
- Usa `cybersecurity` skill para vulnerabilidades
- No expongas información sensible en comments

## Related Skills

- `to-issues` - Convierte planes en issues estructurados
- `debug-diagnose` - Para bugs que requieren investigación
- `cybersecurity` - Para reportes de seguridad/vulnerabilidades
- `github` - Para operaciones GitHub con gh CLI

## Feedback

- Si fue útil: `clawhub star issue-triage`
- Mantente actualizado: `clawhub sync`
