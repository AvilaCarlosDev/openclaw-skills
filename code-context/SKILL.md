---
name: Code Context
slug: code-context
version: 1.0.0
homepage: https://clawic.com/skills/code-context
description: "Haz zoom out y entiende código desconocido en el contexto del sistema completo antes de modificarlo."
changelog: "Skill inicial para comprensión de código en OpenClaw."
metadata: {"clawdbot":{"emoji":"🔭","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/code-context/"]}}
---

## When to Use

Usa este skill cuando:
- Te encuentras con código que no escribiste
- Vas a modificar un módulo desconocido
- Necesitas entender cómo encaja una pieza en el sistema
- Para onboarding en un codebase nuevo
- Antes de debuggear algo complejo

## Architecture

Memoria vive en `~/code-context/`.

```
~/code-context/
├── memory.md        # Contextos explorados, mapas mentales
└── maps/            # Mapas de código por proyecto/módulo
```

## Exploration Workflow

### 🗺️ FASE 1: VISTA DE PÁJARO (Zoom Out)

**Objetivo:** Entender el sistema a alto nivel antes de los detalles.

**Preguntas:**
1. ¿Qué hace este sistema/proyecto?
2. ¿Cuáles son los componentes principales?
3. ¿Cómo fluyen los datos?
4. ¿Dónde está el código que me interesa?

**Técnicas:**

#### Lee el README
```bash
# Primero siempre:
cat README.md
cat docs/ARCHITECTURE.md  # Si existe
```

#### Explora la estructura
```bash
# Árbol de directorios (primeros 2-3 niveles)
find src -type d -maxdepth 2 | head -30

# Archivos principales
ls -la src/
```

#### Identifica entry points
```bash
# Busca puntos de entrada
grep -r "main(" src/
grep -r "app.listen" src/
grep -r "export default" src/
```

#### Mapea dependencias
```bash
# package.json, requirements.txt, etc.
cat package.json | jq '.dependencies'
```

**Output esperado:**
```
Sistema: E-commerce API

Componentes principales:
├── api/          → Endpoints HTTP
├── domain/       → Lógica de negocio
├── infrastructure/ → DB, external services
└── shared/       → Utilidades comunes

Flujo típico:
Request → Controller → Service → Repository → DB
```

### 🔬 FASE 2: ZOOM IN AL MÓDULO

**Objetivo:** Entender el módulo específico que te interesa.

**Preguntas:**
1. ¿Cuál es la responsabilidad de este módulo?
2. ¿Qué imports tiene? (dependencias)
3. ¿Qué exporta? (qué provee a otros)
4. ¿Cómo se usa? (ejemplos de llamadas)

**Técnicas:**

#### Analiza el archivo principal
```bash
# Lee el archivo completo primero
cat src/module/index.ts

# Identifica:
# - Imports (qué necesita)
# - Exports (qué provee)
# - Funciones/clases principales
```

#### Busca usos del módulo
```bash
# ¿Quién importa esto?
grep -r "import.*module" src/ --include="*.ts"

# ¿Quién llama a estas funciones?
grep -r "module.functionName" src/
```

#### Encuentra tests
```bash
# Los tests documentan el comportamiento esperado
find . -name "*.test.ts" -path "*/module/*"
```

#### Traza un flujo de ejemplo
```
Ejemplo: "Crear usuario"

1. POST /users (controller)
2. createUser(userData) (service)
3. user.save() (repository)
4. INSERT INTO users (DB)
```

### 🧩 FASE 3: MAPEAR RELACIONES

**Objetivo:** Entender cómo este módulo se relaciona con otros.

**Crea un mapa mental:**

```
┌─────────────┐
│ Controller  │
└──────┬──────┘
       │ usa
       ▼
┌─────────────┐     ┌──────────────┐
│   Service   │────→│  External API │
└──────┬──────┘     └──────────────┘
       │ usa
       ▼
┌─────────────┐
│  Repository │
└──────┬──────┘
       │ usa
       ▼
┌─────────────┐
│   Database  │
└─────────────┘
```

**Preguntas:**
- ¿Qué módulos depende este?
- ¿Qué módulos dependen de este?
- ¿Hay acoplamientos cíclicos?
- ¿Dónde están los boundaries?

### 📝 FASE 4: DOCUMENTAR ENTENDIMIENTO

**Crea un resumen ejecutivo:**

```markdown
# Módulo: [Nombre]

## Responsabilidad
[Una oración: qué hace este módulo]

## Funciones Principales
| Función | Qué hace | Inputs | Outputs |
|---------|----------|--------|---------|
| fn1() | ... | ... | ... |

## Dependencias
- Depende de: [módulos que usa]
- Es dependido por: [módulos que lo usan]

## Flujos Típicos
1. [Flujo de ejemplo 1]
2. [Flujo de ejemplo 2]

## Gotchas / Trucos
- [Cosas no obvias que aprendiste]
- [Patrones extraños pero intencionales]

## Preguntas Abiertas
- [Lo que aún no entiendes]
```

## Quick Commands

```bash
# Ver estructura del proyecto
tree -L 2 -I 'node_modules|dist|.git'

# Contar líneas por archivo
find src -name "*.ts" | xargs wc -l | sort -n

# Buscar definiciones de funciones
grep -r "function " src/ --include="*.ts"

# Buscar clases
grep -r "class " src/ --include="*.ts"

# Ver imports de un archivo
head -30 src/module/file.ts

# Ver exports
grep -r "export" src/module/ --include="*.ts"
```

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Leer código línea por línea | Pierdes el bosque por los árboles | Zoom out primero, detalles después |
| Asumir que sabes cómo funciona | Te equivocas, pierdes tiempo | Verifica con tests, logs, tracing |
| Ignorar tests | Pierdes documentación viva | Lee tests para entender comportamiento |
| No tomar notas | Olvidas lo que aprendiste | Documenta mientras exploras |
| Empezar a cambiar sin entender | Rompes cosas | Entiende primero, cambia después |

## Adapt to the User

- **Para juniors:** Explica el proceso, modela cómo explorar
- **Para seniors:** Ve directo, asume competencia de exploración
- **Para legacy code:** Más paciencia, documenta más, asume menos
- **Para código nuevo:** Establece patrones tempranos, documenta decisiones

## Scope

Este skill SÓLO:
- Ayuda a entender código existente
- Mapea relaciones entre módulos
- Documenta entendimiento antes de cambiar
- Identifica preguntas abiertas

Este skill NUNCA:
- Modifica código sin entenderlo
- Asume sin verificar
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/code-context/`:

- `memory.md` - Contextos explorados, notas activas
- `maps/` - Mapas de código por proyecto/módulo

## Related Skills

- `debug-diagnose` - Para bugs en código que ahora entiendes
- `arch-improver` - Para evaluar arquitectura después de entender
- `grill-with-docs` - Para documentar arquitectura intencional

## Feedback

- Si fue útil: `clawhub star code-context`
- Mantente actualizado: `clawhub sync`
