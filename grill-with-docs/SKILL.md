---
name: Grill With Docs
slug: grill-with-docs
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/grill-with-docs
description: "Sesión de preguntas implacables que desafía tu plan contra el modelo de dominio, actualiza CONTEXT.md y ADRs antes de codificar."
changelog: "Skill inicial para alineación de requisitos y documentación de decisiones."
metadata: {"clawdbot":{"emoji":"🔥","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/grill-with-docs/"]}}
---

## When to Use

Usa este skill cuando:
- El usuario tiene una idea/vaga de lo que quiere construir
- Antes de empezar a codificar un feature complejo
- Cuando hay ambigüedad en los requisitos
- Para alinear entendimiento entre humano y agente
- Para documentar decisiones de arquitectura (ADRs)

**NO uses** para:
- Bugs simples o fixes obvios
- Cambios cosméticos menores
- Cuando el usuario ya tiene specs detallados y claros

## Architecture

Memoria vive en `~/grill-with-docs/` y en la raíz del proyecto.

```
~/grill-with-docs/
├── memory.md        # Sesiones de grill activas, estado
└── sessions/        # Historial de sesiones de grill

<project-root>/
├── CONTEXT.md       # Modelo de dominio, jerga, conceptos clave
└── docs/adr/        # Architecture Decision Records
    └── ADR-001.md
    └── ADR-002.md
```

## The Grill Process

### 🎯 FASE 1: ENTENDER EL OBJETIVO

**Primera pregunta (siempre):**
> "¿Qué problema real estás tratando de resolver? No me digas la solución, dime el problema."

**Indaga:**
- ¿Quién tiene este problema?
- ¿Qué están haciendo ahora para resolverlo?
- ¿Por qué esa solución actual es insuficiente?
- ¿Qué éxito se ve como? (métricas, comportamientos, resultados)

### 🔍 FASE 2: DESAFIAR SUPOSICIONES

**Para cada suposición en el plan del usuario:**

1. **Identifica la suposición:**
   - "Estás asumiendo que X es cierto..."
   
2. **Pregunta por evidencia:**
   - "¿Qué evidencia tienes de que X es cierto?"
   - "¿Qué pasaría si X es falso?"

3. **Explora alternativas:**
   - "¿Has considerado Y en lugar de X?"
   - "¿Por qué X sobre Y?"

4. **Presiona hasta el fondo:**
   - "¿Por qué?" (repite 3-5 veces, estilo Toyota)

### 📚 FASE 3: MAPEAR EL DOMINIO

**Objetivo:** Crear/actualizar `CONTEXT.md` con lenguaje compartido.

**Elementos a capturar:**

```markdown
# CONTEXT.md - Modelo de Dominio

## Conceptos Clave
- **Término 1:** Definición clara, ejemplos, no-ejemplos
- **Término 2:** ...

## Límites del Sistema
- Qué está dentro del scope
- Qué está fuera del scope
- Sistemas externos con los que interactuamos

## Reglas de Negocio
- Regla 1: Si X entonces Y
- Regla 2: ...

## Actores y Roles
- Quién hace qué
- Permisos y capacidades

## Flujo Principal
1. Paso 1
2. Paso 2
...
```

**Preguntas para extraer el modelo:**
- "¿Qué significa [término] en tu contexto?"
- "¿[Término A] es lo mismo que [Término B] o son diferentes?"
- "¿Quién puede hacer [acción]? ¿Quién no?"
- "¿Qué pasa si [caso edge]?"

### 🏗️ FASE 4: DOCUMENTAR DECISIONES (ADRs)

**Para cada decisión arquitectónica importante:**

```markdown
# ADR-NNN: Título de la Decisión

## Estado
Propuesto | Aceptado | Rechazado | Deprecated

## Contexto
¿Qué problema estamos decidiendo?

## Decision Drivers
- Fuerza 1 (ej: performance)
- Fuerza 2 (ej: simplicidad)
- Fuerza 3 (ej: tiempo)

## Opciones Consideradas
1. Opción A - Pros/Contras
2. Opción B - Pros/Contras
3. Opción C - Pros/Contras

## Decisión
Elegimos [Opción X] porque...

## Consecuencias
### Positivas
- ...

### Negativas (tradeoffs)
- ...

### Riesgos
- ...

## Compliance
- [ ] Esta decisión es consistente con ADR-NNN
- [ ] Las consecuencias negativas son aceptables
```

**Preguntas para forzar decisiones claras:**
- "¿Qué opciones consideraste?"
- "¿Por qué descartaste [opción Y]?"
- "¿Qué tradeoffs estás aceptando?"
- "¿Qué tendría que cambiar para que esta decisión sea incorrecta?"

### ✅ FASE 5: CRITERIOS DE SALIDA

**El grill termina cuando:**

- [ ] El problema está claramente definido
- [ ] Los criterios de éxito son medibles
- [ ] El modelo de dominio está documentado en `CONTEXT.md`
- [ ] Las decisiones arquitectónicas clave tienen ADRs
- [ ] No hay ambigüedades bloqueantes
- [ ] El usuario puede explicar el plan en sus propias palabras

**Si el usuario quiere saltar el grill:**
> "Entiendo la urgencia. Pero 30 minutos de grill ahora te ahorran 3 días de refactor después. ¿Vale la pena?"

## Adapt to the User

- **Para founders/product:** Enfócate en el problema del usuario, métricas de éxito, scope
- **Para tech leads:** Profundiza en tradeoffs arquitectónicos, escalabilidad, mantenibilidad
- **Para juniors:** Explica el "por qué" del grill, modela el pensamiento crítico
- **Para expertos:** Ve directo, asume competencia, desafía suposiciones no triviales

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Aceptar la primera descripción del problema | Suele ser una solución disfrazada | Pregunta "¿qué problema hay detrás de esta solución?" |
| Documentar después de codificar | Las decisiones se olvidan o racionalizan | Documenta ANTES, durante el grill |
| Grill infinito (parálisis) | Nunca es el momento perfecto de codificar | Define criterios de salida claros |
| Asumir que el usuario sabe lo que quiere | Nadie sabe exactamente lo que quiere al inicio | El grill existe para descubrirlo |
| Ignorar tradeoffs | Toda decisión tiene costos | Explicita consecuencias negativas |

## Scope

Este skill SÓLO:
- Facilita sesiones de grill para alinear entendimiento
- Documenta modelo de dominio en `CONTEXT.md`
- Crea ADRs para decisiones arquitectónicas
- Desafía suposiciones y explora alternativas

Este skill NUNCA:
- Toma decisiones por el usuario
- Codifica antes de que el grill complete
- Asume que entiende sin confirmar
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/grill-with-docs/`:

- `memory.md` - Sesiones activas, estado, próximos pasos
- `sessions/` - Historial de sesiones completadas

Documentación del proyecto vive en `<project-root>/`:

- `CONTEXT.md` - Modelo de dominio compartido
- `docs/adr/` - Architecture Decision Records

## Security & Privacy

- No compartas ADRs o CONTEXT.md con información sensible
- Si el proyecto es privado, mantén la documentación local
- Remueve datos sensibles antes de compartir ejemplos

## Related Skills

- `grill-me` - Versión más ligera, sin documentación
- `to-prd` - Convierte el grill en un PRD formal
- `to-issues` - Convierte el plan en issues ejecutables
- `arch-improver` - Analiza la arquitectura resultante

## Feedback

- Si fue útil: `clawhub star grill-with-docs`
- Mantente actualizado: `clawhub sync`
