---
name: Debug Diagnose
slug: debug-diagnose
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/debug-diagnose
description: "Loop disciplinado para diagnosticar bugs difíciles: reproducir → minimizar → hipotetizar → instrumentar → fijar → test de regresión."
changelog: "Skill inicial para diagnóstico sistemático de bugs en OpenClaw."
metadata: {"clawdbot":{"emoji":"🐛","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/debug-diagnose/"]}}
---

## When to Use

Usa este skill cuando:
- Hay un bug que no es obvio y requiere investigación sistemática
- El usuario reporta un comportamiento inesperado
- Necesitas aislar la causa raíz de un problema
- Quieres evitar fixes parche y entender el problema a fondo

## Architecture

Memoria vive en `~/debug-diagnose/`. Si no existe, créalo.

```
~/debug-diagnose/
├── memory.md        # Bugs activos, hipótesis y estado
├── repro-steps.md   # Pasos de reproducción documentados
├── hypotheses.md    # Hipótesis probadas y descartadas
└── fixes.md         # Fixes aplicados y lecciones aprendidas
```

## Core Workflow: Debug Loop

### 1️⃣ REPRODUCIR (Reproduce)
**Objetivo:** Confirmar que el bug existe y es consistente.

**Acciones:**
- [ ] Documenta pasos exactos para reproducir
- [ ] Identifica condiciones necesarias (entorno, datos, estado)
- [ ] Confirma frecuencia: ¿siempre? ¿intermitente? ¿bajo carga?
- [ ] Captura output/error exacto
- [ ] Aísla el mínimo contexto necesario

**Preguntas clave:**
- ¿Qué comportamiento esperabas vs qué obtuviste?
- ¿Cuándo fue la última vez que funcionó?
- ¿Qué cambió desde entonces?

### 2️⃣ MINIMIZAR (Minimize)
**Objetivo:** Reducir el problema a su forma más simple.

**Acciones:**
- [ ] Elimina código/dependencias no relacionadas
- [ ] Crea un caso de prueba mínimo (MRE - Minimal Reproducible Example)
- [ ] Aísla el componente afectado
- [ ] Identifica el boundary exacto donde falla

**Técnicas:**
- Binary search en el código (git bisect si aplica)
- Comentar secciones hasta aislar el problema
- Reemplazar dependencias con mocks/stubs

### 3️⃣ HIPOTETIZAR (Hypothesize)
**Objetivo:** Generar explicaciones posibles del bug.

**Acciones:**
- [ ] Lista 3-5 hipótesis plausibles
- [ ] Para cada una: ¿qué evidencia la apoyaría? ¿qué la refutaría?
- [ ] Ordena por probabilidad y facilidad de test
- [ ] Documenta suposiciones explícitamente

**Ejemplo de hipótesis:**
```
H1: Race condition en la inicialización (probabilidad: media)
    - Evidencia necesaria: logs de timing, reproducir con delays
    - Se refuta si: falla consistentemente sin concurrencia

H2: Estado corrupto en memoria/cache (probabilidad: alta)
    - Evidencia necesaria: limpiar cache y probar
    - Se refuta si: persiste después de clean state
```

### 4️⃣ INSTRUMENTAR (Instrument)
**Objetivo:** Obtener datos para confirmar/refutar hipótesis.

**Acciones:**
- [ ] Agrega logging estratégico (no a ciegas)
- [ ] Inserta checkpoints/affirmations
- [ ] Usa debugger si es viable
- [ ] Captura estado antes/después del punto de falla

**Principios:**
- Instrumenta cerca del boundary del bug, no en todo el código
- Captura tanto inputs como outputs
- Incluye timestamps y contexto (user, session, request id)

### 5️⃣ FIJAR (Fix)
**Objetivo:** Aplicar el fix correcto para la causa raíz.

**Acciones:**
- [ ] Confirma la hipótesis con evidencia
- [ ] Diseña el fix que aborda la causa, no el síntoma
- [ ] Considera edge cases y efectos secundarios
- [ ] Documenta el "por qué" del fix (no solo el "qué")

**Criterios de buen fix:**
- ✅ Aborda la causa raíz, no el síntoma
- ✅ No introduce nuevos bugs (regresiones)
- ✅ Es simple y comprensible
- ✅ Incluye test que prevenga regresión

### 6️⃣ TEST DE REGRESIÓN (Regression Test)
**Objetivo:** Asegurar que el bug no vuelva.

**Acciones:**
- [ ] Crea test automatizado que reproduzca el bug original
- [ ] Confirma que el test falla sin el fix
- [ ] Confirma que el test pasa con el fix
- [ ] Agrega el test al suite permanente
- [ ] Documenta el bug en `fixes.md`

## Adapt to the User

- **Para juniors:** Explica el proceso paso a paso, modela el pensamiento sistemático
- **Para seniors:** Ve directo al grano, enfócate en evidencia y tradeoffs
- **Para debugging en producción:** Prioriza preservación de evidencia y minimizar downtime
- **Para debugging local:** Sé más agresivo con instrumentación y cambios

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Cambiar cosas al azar | Gasta tiempo, no genera conocimiento | Sigue el loop: reproduce → hipotetiza → test |
| Asumir la causa sin evidencia | Lleva a fixes incorrectos | Instrumenta primero, concluye después |
| Fixear el síntoma | El bug vuelve de otra forma | Encuentra la causa raíz |
| No crear test de regresión | El mismo bug regresará | Test automatizado es obligatorio |
| Debuggear sin reproducir consistente | No puedes confirmar fixes | Estabiliza la reproducción primero |

## Scope

Este skill SÓLO:
- Soporta diagnóstico sistemático de bugs y comportamientos inesperados
- Sigue el loop: reproducir → minimizar → hipotetizar → instrumentar → fijar → test
- Documenta hipótesis, evidencia y fixes en `~/debug-diagnose/`

Este skill NUNCA:
- Cambia código sin entender la causa raíz
- Aplica fixes parche sin test de regresión
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/debug-diagnose/`:

- `memory.md` - Bugs activos, estado actual, próximos pasos
- `repro-steps.md` - Pasos de reproducción documentados y verificados
- `hypotheses.md` - Hipótesis generadas, evidencia, resultados de tests
- `fixes.md` - Fixes aplicados, causa raíz, lecciones aprendidas

## Security & Privacy

- No compartas logs con datos sensibles (tokens, passwords, PII)
- Si el bug involucra seguridad, sigue el skill `cybersecurity` primero
- Preserva evidencia pero sanitiza antes de compartir

## Related Skills

- `cybersecurity` - Si el bug es de seguridad o vulnerabilidad
- `tdd-helper` - Para crear tests de regresión
- `code-context` - Para entender código desconocido antes de debuggear
- `git-guardrails` - Para evitar commits peligrosos durante el fix

## Feedback

- Si fue útil: `clawhub star debug-diagnose`
- Mantente actualizado: `clawhub sync`
