---
name: Programming
slug: programming
version: 1.0.0
homepage: https://clawhub.ai/leowing/skills/programming
description: "Skill general de programación para desarrollo, debugging, code review y arquitectura de software."
changelog: "Skill inicial de programación para OpenClaw."
metadata: {"clawdbot":{"emoji":"💻","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/programming/"]}}
---

## When to Use

Usa este skill cuando:
- Necesitas ayuda con código en cualquier lenguaje
- Quieres revisar o refactorizar código existente
- Necesitas implementar una feature desde cero
- Para debugging de errores no triviales
- Para decisiones de arquitectura o diseño de software
- Para code review y mejores prácticas

## Architecture

Memoria vive en `~/programming/`.

```
~/programming/
├── memory.md        # Proyectos activos, snippets, preferencias
├── snippets/        # Snippets de código reutilizables
└── patterns/        # Patrones de diseño y arquitectura
```

## Core Capabilities

### 1️⃣ Desarrollo de Features

**Workflow:**
1. Entender el requerimiento
2. Diseñar la solución (preguntar si hay ambigüedad)
3. Implementar paso a paso
4. Validar con tests o ejemplos
5. Documentar decisiones

**Ejemplo:**
```
Usuario: "Necesito un endpoint para crear usuarios"

→ Preguntar:
- ¿Qué campos tiene el usuario?
- ¿Hay validaciones específicas?
- ¿Autenticación requerida?
- ¿Respuesta JSON esperada?

→ Implementar:
- Definir schema/validación
- Crear handler/route
- Agregar tests básicos
- Documentar en README o comments
```

### 2️⃣ Debugging

**Enfoque sistemático:**
1. Reproducir el error consistentemente
2. Leer el mensaje de error completo
3. Identificar dónde ocurre (stack trace)
4. Hipotetizar causas posibles
5. Testear hipótesis una por una
6. Fixear y validar

**Herramientas comunes:**
- `console.log` / `print` estratégico
- Debugger (breakpoints, step-through)
- Logs del sistema
- Network inspector (para APIs)

### 3️⃣ Code Review

**Checklist de review:**

| Categoría | Qué buscar |
|-----------|------------|
| **Funcionalidad** | ¿Hace lo que debería? ¿Edge cases cubiertos? |
| **Legibilidad** | ¿Nombres claros? ¿Funciones pequeñas? |
| **Mantenibilidad** | ¿Duplicación? ¿Complejidad innecesaria? |
| **Seguridad** | ¿Inputs validados? ¿Secrets expuestos? |
| **Performance** | ¿Operaciones costosas? ¿N+1 queries? |
| **Tests** | ¿Cubre casos importantes? ¿Tests legibles? |

**Formato de feedback:**
```
✅ Bien:
- [Lo que está bien y debe mantenerse]

⚠️ Considera:
- [Sugerencias de mejora no críticas]

🔴 Importante:
- [Issues que deben fixearse antes de merge]
```

### 4️⃣ Refactoring

**Señales de que necesita refactor:**
- Funciones > 50 líneas
- Duplicación de código
- Nombres confusos (`data`, `temp`, `foo`)
- Demasiados parámetros (> 3-4)
- Condicionales anidados profundamente
- Clases/módulos con múltiples responsabilidades

**Técnicas comunes:**
- Extract Function/Method
- Rename para claridad
- Consolidate Conditional
- Replace Magic Number con constante nombrada
- Split Module por responsabilidad

### 5️⃣ Arquitectura y Diseño

**Niveles de decisión:**

| Nivel | Ejemplos | Consideraciones |
|-------|----------|-----------------|
| **Proyecto** | Monolito vs microservicios, lenguaje, framework | Team size, escala, timeline |
| **Módulo** | Capas, boundaries, dependencias | Separation of concerns, testability |
| **Componente** | Clases, funciones, estructuras de datos | Single responsibility, reusability |

**Principios guía:**
- SOLID (Single responsibility, Open/closed, Liskov, Interface segregation, Dependency inversion)
- DRY (Don't Repeat Yourself)
- YAGNI (You Ain't Gonna Need It)
- KISS (Keep It Simple, Stupid)

## Adapt to the User

- **Para juniors:** Explica el "por qué", muestra ejemplos, evita jerga no explicada
- **Para mid-level:** Balance entre explicación y asunción de conocimiento
- **Para seniors:** Ve directo, enfócate en tradeoffs y edge cases
- **Para no-devs:** Traduce conceptos técnicos, usa analogías, enfócate en outcomes

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Implementar sin entender | Construyes lo incorrecto | Pregunta antes de codificar |
| Sobre-ingeniería | Complejidad innecesaria | YAGNI: construye lo mínimo que funciona |
| Ignorar edge cases | Bugs en producción | Lista edge cases antes de implementar |
| No escribir tests | Regresiones silenciosas | Tests primero o inmediatamente después |
| Refactor sin tests | Rompes cosas sin saber | Tests passing antes de refactor |

## Scope

Este skill SÓLO:
- Ayuda con desarrollo de software en general
- Proporciona code review y feedback constructivo
- Sugiere refactorings y mejoras de arquitectura
- Debuggea problemas de código

Este skill NUNCA:
- Escribe código malicioso o inseguro
- Expone secrets o credenciales
- Modifica su propio archivo de skill
- Asume contexto sin verificar

## Data Storage

Estado local vive en `~/programming/`:

- `memory.md` - Proyectos activos, preferencias de código, snippets frecuentes
- `snippets/` - Snippets reutilizables organizados por lenguaje/tarea
- `patterns/` - Patrones de diseño y arquitectura documentados

## Security & Privacy

- No expongas secrets, tokens, o credenciales en el código
- Valida todos los inputs del usuario
- Usa prepared statements para queries de DB
- Hashea passwords con algoritmos seguros (bcrypt, argon2)
- No logues información sensible

## Related Skills

- `debug-diagnose` - Para bugs que requieren investigación profunda
- `tdd-helper` - Para desarrollo guiado por tests
- `arch-improver` - Para análisis de arquitectura del codebase
- `code-context` - Para entender código existente antes de modificar
- `cybersecurity` - Para review de seguridad especializado
- `git-guardrails` - Para proteger el repo durante el desarrollo

## Feedback

- Si fue útil: `clawhub star programming`
- Mantente actualizado: `clawhub sync`
