---
name: Plan to Issues
slug: plan-to-issues
version: 1.0.0
homepage: https://clawic.com/skills/plan-to-issues
description: "Convierte cualquier plan, spec o PRD en GitHub issues independientes usando vertical slices."
changelog: "Skill inicial para descomposición de planes en issues ejecutables."
metadata: {"clawdbot":{"emoji":"📦","requires":{"bins":["gh"]},"os":["linux","darwin","win32"],"configPaths":["~/plan-to-issues/"]}}
---

## When to Use

Usa este skill cuando:
- Tienes un plan/spec/PRD y necesitas ejecutarlo
- Quieres dividir un feature grande en issues manejables
- Necesitas crear un backlog accionable
- Para estimar esfuerzo de un proyecto

## Architecture

Memoria vive en `~/plan-to-issues/`.

```
~/plan-to-issues/
├── memory.md        # Configuración, templates
├── plans/           # Plans/PRDs procesados
└── output/          # Issues generados
```

## Vertical Slicing Principles

### ¿Qué es una Vertical Slice?

Una vertical slice es un incremento de funcionalidad que:
- ✅ Atraviesa todas las capas (UI → Backend → DB)
- ✅ Entrega valor observable al usuario
- ✅ Se puede desarrollar y testear independientemente
- ✅ Se puede deployar sin romper nada

### ❌ Horizontal Slicing (EVITAR)

```
Issue 1: Crear modelos de base de datos
Issue 2: Crear API endpoints
Issue 3: Crear componentes UI
Issue 4: Integrar todo
```
**Problema:** Ningún issue entrega valor por sí solo.

### ✅ Vertical Slicing (CORRECTO)

```
Issue 1: Usuario puede registrarse con email/password
Issue 2: Usuario puede loguearse y ver su perfil
Issue 3: Usuario puede actualizar su nombre
Issue 4: Usuario puede cambiar su password
```
**Ventaja:** Cada issue entrega valor completo.

## Decomposition Workflow

### 🔍 PASO 1: ENTENDER EL PLAN

**Lee el plan completo y identifica:**
- ¿Cuál es el objetivo final?
- ¿Quiénes son los usuarios/actores?
- ¿Cuáles son las features principales?
- ¿Hay dependencias externas?

**Preguntas clarificadoras:**
- "¿Qué es lo más pequeño que podríamos entregar que tenga valor?"
- "¿Qué depende de qué?"
- "¿Hay algo que podamos eliminar del scope inicial?"

### 📊 PASO 2: MAPEAR USER STORIES

**Formato:**
```
Como [tipo de usuario]
Quiero [acción/capacidad]
Para [beneficio/valor]
```

**Ejemplos:**
```
Como visitante
Quiero ver una lista de productos
Para saber qué pueden comprar

Como cliente registrado
Quiero agregar productos al carrito
Para comprar múltiples items juntos

Como administrador
Quiero ver órdenes pendientes
Para procesarlas y enviarlas
```

### 🔪 PASO 3: CORTAR EN SLICES

**Técnicas de slicing:**

#### 1. Por Workflow (Recomendado)
```
Workflow: "Comprar producto"
├── Slice 1: Ver producto
├── Slice 2: Agregar al carrito
├── Slice 3: Checkout como invitado
├── Slice 4: Checkout registrado
└── Slice 5: Ver historial de órdenes
```

#### 2. Por Regla de Negocio
```
Feature: "Descuentos"
├── Slice 1: Descuento fijo por producto
├── Slice 2: Descuento por cantidad
├── Slice 3: Cupones de descuento
└── Slice 4: Descuentos por tipo de usuario
```

#### 3. Por Canal/Plataforma
```
Feature: "Notificaciones"
├── Slice 1: Notificaciones en UI
├── Slice 2: Notificaciones por email
├── Slice 3: Notificaciones push
└── Slice 4: Notificaciones SMS
```

#### 4. Por Criterio de Aceptación
```
Feature: "Búsqueda"
├── Slice 1: Búsqueda por título exacto
├── Slice 2: Búsqueda parcial (contains)
├── Slice 3: Búsqueda por múltiples campos
└── Slice 4: Búsqueda con filtros avanzados
```

### 📝 PASO 4: ESCRIBIR ISSUES

**Template de issue:**

```markdown
## 📋 Descripción

[Descripción clara de qué se va a construir]

## 🎯 Criterios de Aceptación

- [ ] Criterio 1 (observable y testeable)
- [ ] Criterio 2
- [ ] Criterio 3

## 🔗 Dependencias

- Depende de: #[número] (si aplica)
- Bloquea a: #[número] (si aplica)

## 📐 Notas Técnicas

- [Notas relevantes para implementación]

## 🧪 Tests

- [ ] Test para criterio 1
- [ ] Test para criterio 2

## 📸 Mockups (si aplica)

[Links o descripciones de diseños]
```

### 🏷️ PASO 5: PRIORIZAR Y LABELAR

**Prioridad:**
- P0: Crítico para el MVP
- P1: Importante para launch
- P2: Post-launch
- P3: Nice to have

**Labels:**
- Tipo: `feature`, `bug`, `enhancement`
- Área: `frontend`, `backend`, `design`
- Tamaño: `XS`, `S`, `M`, `L`, `XL` (para estimación)

### 🔗 PASO 6: CREAR DEPENDENCIAS

**Mapea dependencias:**
```
Issue 1 → Issue 2 → Issue 4
              ↓
            Issue 3 → Issue 5
```

**En GitHub:**
- Usa "blocked by" y "blocks" en la descripción
- O usa GitHub Projects con dependencias

## Estimation Guidelines

### T-Shirt Sizing

| Tamaño | Esfuerzo | Descripción |
|--------|----------|-------------|
| XS | < 2 horas | Trivial, casi sin riesgo |
| S | 0.5 - 1 día | Pequeño, claro, bajo riesgo |
| M | 1 - 3 días | Moderado, algunos unknowns |
| L | 3 - 5 días | Grande, varios unknowns |
| XL | > 1 semana | Muy grande, necesita más slicing |

**Si es XL →** Divide en issues más pequeños.

## Automation with gh CLI

```bash
# Crear issue desde template
gh issue create --title "Título" --body-file issue.md --label P1-high,feature

# Crear múltiples issues desde archivo
cat issues.txt | while read title; do
  gh issue create --title "$title" --label backlog
done

# Ver issues creados
gh issue list --author @me --state open
```

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Slices muy grandes | Difícil estimar, riesgo alto | Divide hasta que sea < 3 días |
| Slices horizontales | No entregan valor individual | Corta por workflow/feature completa |
| Dependencias circulares | Bloqueo mutuo | Reestructura para eliminar ciclos |
| Criterios vagos | No se sabe cuándo está hecho | Hazlos observables y testeables |
| Ignorar dependencias | Sorpresas durante desarrollo | Mapea dependencias antes de empezar |

## Adapt to the User

- **Para PMs:** Enfócate en valor de usuario, criterios de aceptación claros
- **Para devs:** Incluye notas técnicas, dependencias, estimaciones
- **Para equipos pequeños:** Menos burocracia, más acción
- **Para empresas:** Alinea con procesos existentes, JIRA, etc.

## Scope

Este skill SÓLO:
- Convierte planes en vertical slices
- Crea issues con criterios claros
- Identifica dependencias
- Prioriza por valor entregado

Este skill NUNCA:
- Crea issues sin valor observable
- Ignora dependencias críticas
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/plan-to-issues/`:

- `memory.md` - Configuración, templates preferidos
- `plans/` - Plans/PRDs originales procesados
- `output/` - Issues generados, tracking

## Related Skills

- `to-prd` - Crea PRD antes de convertir a issues
- `issue-triage` - Para triage de issues creados
- `grill-with-docs` - Para clarificar el plan antes de slice

## Feedback

- Si fue útil: `clawhub star plan-to-issues`
- Mantente actualizado: `clawhub sync`
