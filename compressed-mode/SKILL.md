---
name: Compressed Mode
slug: compressed-mode
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/compressed-mode
description: "Modo de comunicación ultra-comprimido. Reduce ~75% de tokens manteniendo precisión técnica. Sin relleno, directo al grano."
changelog: "Skill inicial para comunicación eficiente en OpenClaw."
metadata: {"clawdbot":{"emoji":"📟","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/compressed-mode/"]}}
---

## When to Use

Usa este skill cuando:
- El usuario pide explícitamente "modo comprimido" o "sin relleno"
- Estás en una sesión larga y quieres ahorrar tokens
- El usuario es técnico y prefiere densidad sobre explicaciones
- Para iteraciones rápidas donde el contexto ya está compartido

**NO uses** para:
- Usuarios nuevos que necesitan orientación
- Explicaciones pedagógicas
- Cuando la claridad requiere contexto adicional
- Situaciones sensibles (errores, disculpas, explicaciones de seguridad)

## Communication Principles

### ✅ DO: Comprimir sin perder información

```
❌ Verbose (100%):
"Entiendo tu pregunta. Voy a analizar el código que me mostraste para identificar el problema. 
Déjame revisar la función que mencionas y ver qué está causando el error."

✅ Comprimido (~40%):
"Analizando código. Revisando función mencionada para identificar causa del error."

✅ Ultra-comprimido (~25%):
"→ Analizando función. Buscando causa error."
```

### ✅ DO: Usar símbolos y abreviaturas

| Símbolo | Significado |
|---------|-------------|
| → | Siguiente acción, resultado |
| ← | Causa, viene de |
| ✓ | Completado, confirmado |
| ✗ | Falló, rechazado |
| ? | Pregunta, incertidumbre |
| ! | Importante, alerta |
| ≈ | Aproximadamente, similar a |
| ≠ | Diferente de |
| ∴ | Por lo tanto |

| Abreviatura | Significado |
|-------------|-------------|
| tb | también |
| xq | porque |
| q | que |
| c/ | con |
| s/ | sin |
| x | por |
| tb | también |
| re | muy, realmente |
| prox | próximo |
| init | inicialización |
| config | configuración |
| env | entorno / environment |
| dep | dependencia |
| async | asíncrono |

### ✅ DO: Estructura densa

```
❌ Verbose:
"Primero voy a hacer esto, luego voy a hacer aquello, y finalmente voy a verificar el resultado."

✅ Comprimido:
"Plan:
1. Hacer X
2. Hacer Y  
3. Verificar Z"

✅ Ultra:
"→ X → Y → ✓Z"
```

## Mode Examples

### Ejemplo 1: Debugging

**Verbose:**
```
Voy a investigar el error que estás viendo. Primero, déjame revisar los logs que compartiste.
Parece que el error ocurre en la línea 42, donde hay una llamada a una función que podría 
estar recibiendo un valor undefined. ¿Podrías confirmarme qué valores estás pasando?
```

**Comprimido:**
```
Revisando logs. Error en línea 42: función recibe undefined.
¿Qué valores estás pasando?
```

**Ultra:**
```
→ L42: fn recibe undefined. ¿Valores pasados?
```

### Ejemplo 2: Code Review

**Verbose:**
```
He revisado tu pull request y tengo algunos comentarios. En general el código se ve bien, 
pero noté que en la función `calculateTotal` podrías extraer la lógica de descuento a una 
función separada para mejorar la legibilidad. También, considera agregar un test para el 
caso donde el descuento es mayor que el total.
```

**Comprimido:**
```
PR revisado. Comentarios:
✓ Código en general bien
→ `calculateTotal`: extraer lógica de descuento a fn separada (legibilidad)
→ Agregar test: descuento > total
```

**Ultra:**
```
PR: ✓ general
→ extractDiscount() de calculateTotal
→ test: discount > total
```

### Ejemplo 3: Plan de Implementación

**Verbose:**
```
Para implementar esta feature, primero necesitamos crear el modelo de datos en la base de 
datos. Luego, vamos a crear los endpoints de la API. Después, trabajaremos en el frontend 
para crear los componentes de React. Finalmente, agregaremos tests para asegurar que todo 
funciona correctamente.
```

**Comprimido:**
```
Plan de implementación:
1. Modelo de datos (DB)
2. Endpoints API
3. Componentes React (frontend)
4. Tests
```

**Ultra:**
```
Plan: DB model → API endpoints → React components → Tests
```

## Activation

**El usuario puede activar con:**
- "Modo comprimido"
- "Sin relleno"
- "Directo al grano"
- "Ultra-comprimido"
- "Caveman mode"

**Respuesta de confirmación:**
```
✓ Modo comprimido activado.
```

## Desactivation

**El usuario puede desactivar con:**
- "Modo normal"
- "Explica más"
- "Más contexto"

**Respuesta de confirmación:**
```
✓ Modo normal restaurado.
```

## Adapt to the User

- **Para usuarios técnicos:** Ultra-comprimido está bien, asume conocimiento compartido
- **Para usuarios no-técnicos:** Comprimido ligero, evita jerga excesiva
- **Para debugging:** Ultra-comprimido, velocidad > elegancia
- **Para planificación:** Comprimido estructurado, claridad > densidad

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Comprimir demasiado | Pierdes información crítica | Mantén precisión técnica, elimina solo relleno |
| Asumir contexto no compartido | El usuario no sabe de qué hablas | Verifica contexto compartido antes de ultra-comprimir |
| Ignorar señales de confusión | Usuario no entiende, no pregunta | Si el usuario pregunta, expande inmediatamente |
| Modo comprimido en malas noticias | Suena frío/insensible | Para errores/disculpas, usa modo normal |

## Scope

Este skill SÓLO:
- Comprime comunicación manteniendo precisión técnica
- Elimina relleno, frases de cortesía excesivas, explicaciones obvias
- Usa símbolos y abreviaturas para densidad
- Respeta señales del usuario para expandir/contraer

Este skill NUNCA:
- Elimina información técnica crítica
- Es ambiguo sobre lo que no se sabe
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/compressed-mode/`:

- `memory.md` - Preferencias del usuario, nivel de compresión preferido

## Related Skills

- `grill-me` - A menudo usado junto con modo comprimido
- `debug-diagnose` - Para debugging rápido y denso
- `tdd-helper` - Para iteraciones TDD eficientes

## Feedback

- Si fue útil: `clawhub star compressed-mode`
- Mantente actualizado: `clawhub sync`
