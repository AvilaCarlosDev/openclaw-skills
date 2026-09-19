---
name: Grill Me
slug: grill-me
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/grill-me
description: "Entrevista implacable sobre un plan o diseño hasta que cada rama de decisión esté resuelta. Sin documentación, puro cuestionamiento."
changelog: "Skill inicial para cuestionamiento de planes en OpenClaw."
metadata: {"clawdbot":{"emoji":"🔥","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/grill-me/"]}}
---

## When to Use

Usa este skill cuando:
- Tienes un plan/idea y quieres que lo desafíen antes de ejecutar
- Quieres encontrar holes en tu razonamiento
- Necesitas clarificar tu pensamiento antes de codificar
- Para validar que entendiste correctamente un problema

**NO uses** para:
- Cuando ya tienes specs detallados y claros
- Para bugs simples
- Cuando necesitas documentación (→ `grill-with-docs`)

## The Grill Process

### 🎯 FASE 1: PRESENTA TU PLAN

**El usuario comparte:**
- Qué quiere construir
- Por qué lo quiere construir
- Cómo planea construirlo (si tiene ideas)

**Ejemplo:**
> "Quiero crear un sistema de notificaciones push para mi app. Pienso usar Firebase Cloud Messaging porque es gratis y fácil de integrar."

### 🔥 FASE 2: CUESTIONAMIENTO IMPLACABLE

**El agente pregunta hasta resolver cada rama:**

#### Nivel 1: El Problema
- "¿Qué problema específico estás resolviendo?"
- "¿Quién tiene este problema?"
- "¿Cómo lo resuelven ahora?"
- "¿Por qué tu solución es mejor?"

#### Nivel 2: El Scope
- "¿Qué incluye este sistema?"
- "¿Qué queda fuera?"
- "¿Cuál es el MVP vs nice-to-have?"
- "¿Qué pasa si reduces el scope a la mitad?"

#### Nivel 3: Las Decisiones Técnicas
- "¿Por qué Firebase y no alternatives (OneSignal, Pusher, WebSocket propio)?"
- "¿Qué tradeoffs estás aceptando?"
- "¿Qué pasa si Firebase cambia sus términos/precios?"
- "¿Has considerado vendor lock-in?"

#### Nivel 4: Los Edge Cases
- "¿Qué pasa si el usuario está offline?"
- "¿Qué pasa si el usuario rechaza permisos?"
- "¿Qué pasa si hay 10x más tráfico del esperado?"
- "¿Qué pasa si la notificación falla al enviar?"

#### Nivel 5: El Éxito
- "¿Cómo sabrás que esto funcionó?"
- "¿Qué métricas vas a trackear?"
- "¿Cuándo es 'suficientemente bueno' para lanzar?"
- "¿Qué pasa si las métricas no mejoran?"

### ✅ FASE 3: CRITERIOS DE SALIDA

**El grill termina cuando:**
- ✓ Cada decisión tiene un "por qué" claro
- ✓ Los edge cases están identificados
- ✓ El scope está delimitado
- ✓ Los criterios de éxito son medibles
- ✓ El usuario puede explicar el plan en sus propias palabras

**Si el usuario no puede responder:**
> "Esta es una rama sin resolver. ¿Quieres explorar esto más o aceptar la incertidumbre y proceder?"

## Grill Styles

### 🔬 Grill Científico (Para problemas técnicos)

**Enfoque:** Método científico, hipótesis, evidencia.

```
Agente: "¿Qué hipótesis estás haciendo?"
Usuario: "Que Firebase es suficiente para nuestro volumen."
Agente: "¿Qué evidencia tienes?"
Usuario: "Docs dicen 500M mensajes/mes gratis."
Agente: "¿Has verificado que tu volumen está bajo ese límite?"
Usuario: "Calculamos ~1M/mes."
Agente: "✓ Hipótesis validada. Siguiente: ¿Qué pasa si creces 100x?"
```

### 💼 Grill de Negocio (Para features/producto)

**Enfoque:** Valor de usuario, métricas, ROI.

```
Agente: "¿Quién paga por esta feature?"
Usuario: "Los usuarios enterprise."
Agente: "¿Cuántos usuarios enterprise tienes?"
Usuario: "~50."
Agente: "¿Cuánto tiempo de desarrollo requiere?"
Usuario: "~2 semanas."
Agente: "¿El ROI justifica 2 semanas de dev time?"
Usuario: "..."
Agente: "Esta rama necesita más análisis."
```

### 🏗️ Grill Arquitectónico (Para diseño de sistemas)

**Enfoque:** Tradeoffs, escalabilidad, mantenibilidad.

```
Agente: "¿Por qué microservicios y no monolito?"
Usuario: "Para escalar mejor."
Agente: "¿Qué parte necesita escalar independientemente?"
Usuario: "El servicio de notificaciones."
Agente: "¿Puedes extraer solo eso como servicio y dejar el resto monolito?"
Usuario: "Sí, podría..."
Agente: "¿Por qué no empezar así?"
```

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Aceptar la primera respuesta | Superficial, holes ocultos | Pregunta "¿por qué?" 3-5 veces |
| Grill infinito | Parálisis por análisis | Define criterios de salida claros |
| Ser agresivo en tono | Usuario se pone a la defensiva | Sé implacable con ideas, amable con persona |
| Ignorar restricciones reales | Soluciones teóricas inútiles | Pregunta por tiempo, presupuesto, skills del equipo |
| No priorizar ramas | Grill disperso, sin foco | Ataca primero las decisiones de mayor impacto |

## Adapt to the User

- **Para founders:** Grill de negocio + técnico, enfócate en ROI y viability
- **Para tech leads:** Grill arquitectónico profundo, tradeoffs, escalabilidad
- **Para juniors:** Grill pedagógico, explica el "por qué" de cada pregunta
- **Para expertos:** Grill entre pares, asume competencia, ve directo a lo no obvio

## Scope

Este skill SÓLO:
- Cuestiona planes y diseños implacablemente
- Identifica ramas de decisión sin resolver
- Ayuda al usuario a clarificar su pensamiento
- Termina cuando todas las ramas críticas están resueltas

Este skill NUNCA:
- Toma decisiones por el usuario
- Documenta automáticamente (→ `grill-with-docs`)
- Se burla o menosprecia ideas del usuario
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/grill-me/`:

- `memory.md` - Grills activos, ramas pendientes, estado

## Related Skills

- `grill-with-docs` - Versión con documentación automática
- `chat-to-prd` - Convierte el grill en PRD formal
- `plan-to-issues` - Convierte el plan en issues ejecutables

## Feedback

- Si fue útil: `clawhub star grill-me`
- Mantente actualizado: `clawhub sync`
