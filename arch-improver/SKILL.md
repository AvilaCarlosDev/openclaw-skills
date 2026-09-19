---
name: Architecture Improver
slug: arch-improver
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/arch-improver
description: "Encuentra oportunidades de mejora en la arquitectura del codebase: acoplamientos, violaciones de capas, deuda técnica."
changelog: "Skill inicial para análisis y mejora de arquitectura en OpenClaw."
metadata: {"clawdbot":{"emoji":"🏗️","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/arch-improver/"]}}
---

## When to Use

Usa este skill cuando:
- Sientes que el código se volvió difícil de cambiar
- Hay acoplamientos extraños entre módulos
- Quieres evaluar la arquitectura antes de agregar una feature grande
- Necesitas identificar deuda técnica prioritaria
- Para refactorings estratégicos (no cosméticos)

## Architecture

Memoria vive en `~/arch-improver/`.

```
~/arch-improver/
├── memory.md        # Análisis activos, hallazgos
├── assessments/     # Evaluaciones arquitectónicas
└── improvements/    # Mejoras propuestas y su estado
```

## Analysis Framework

### 1️⃣ MAPEAR LA ARQUITECTURA ACTUAL

**Objetivo:** Entender cómo está organizado el sistema hoy.

**Preguntas:**
- ¿Cuáles son los módulos/componentes principales?
- ¿Cómo se comunican entre sí?
- ¿Hay una arquitectura intencional (layers, hex, etc.)?
- ¿Dónde está la lógica de negocio?

**Técnicas:**
- Revisa la estructura de directorios
- Identifica patrones de importación
- Busca archivos "god" (muy grandes, muchas responsabilidades)
- Mapea flujos de datos principales

**Output esperado:**
```
Arquitectura actual (observada):

src/
├── controllers/  → Lógica HTTP
├── services/     → Lógica de negocio (¿o es orquestación?)
├── models/       → DB + lógica de dominio (¿mezcladas?)
├── utils/        → ¿Qué hay aquí realmente?
└── config/       → Configuración

Flujos principales:
Request → Controller → Service → Model → DB
```

### 2️⃣ IDENTIFICAR SMELLS ARQUITECTÓNICOS

**Busca estos patrones:**

#### 🔴 Acoplamiento Cíclico
```
Module A → Module B → Module C → Module A
```
**Señal:** Cambiar A requiere cambiar B y C, que afectan A.

**Fix:** Introducir interfaz común, invertir dependencia.

#### 🔴 Violación de Capas
```
Controller → Model directamente (saltando Service)
Model → Controller (callback inverso)
UI → DB (sin capa intermedia)
```
**Señal:** Atajos que rompen la arquitectura intencional.

**Fix:** Respetar capas, extraer intermediarios.

#### 🔴 God Object / God Class
```
UserService tiene 2000 líneas y:
- Valida usuarios
- Envía emails
- Genera reportes
- Maneja sesiones
- Procesa pagos
```
**Señal:** Una clase/módulo que "hace todo".

**Fix:** Extraer responsabilidades a clases separadas.

#### 🔴 Feature Envy
```
// En OrderController:
const discount = user.calculateDiscount(order);
```
**Señal:** Un objeto usa intensivamente los datos de otro.

**Fix:** Mover el método al objeto que tiene los datos.

#### 🔴 Shotgun Surgery
```
Para agregar un campo, necesitas cambiar:
- Controller
- Service
- Model
- DTO
- Validator
- Test (5 archivos)
```
**Señal:** Un cambio lógico requiere muchas modificaciones.

**Fix:** Consolidar responsabilidad, reducir puntos de cambio.

#### 🔴 Arquitectura Implícita
```
No hay estructura clara, los archivos se organizan "como salió".
```
**Señal:** Nuevos devs no saben dónde poner código nuevo.

**Fix:** Documentar arquitectura intencional, refactorizar hacia ella.

### 3️⃣ EVALUAR IMPACTO Y ESFUERZO

**Matriz de priorización:**

| Hallazgo | Impacto | Esfuerzo | Prioridad |
|----------|---------|----------|-----------|
| Acoplamiento cíclico en payments | Alto | Medio | 🔴 P0 |
| God class en UserService | Alto | Alto | 🟡 P1 |
| Violación de capas en reports | Medio | Bajo | 🟢 P2 |

**Criterios:**
- **Impacto:** ¿Cuánto mejora la mantenibilidad?
- **Esfuerzo:** ¿Cuánto trabajo requiere?
- **Riesgo:** ¿Qué puede romperse?
- **Urgencia:** ¿Bloquea features futuros?

### 4️⃣ PROPONER MEJORAS

**Formato de propuesta:**

```markdown
## Mejora: [Nombre]

### Problema
[Descripción del smell arquitectónico]

### Impacto Actual
- [Cómo afecta el desarrollo hoy]
- [Riesgos si no se fixea]

### Propuesta
[Qué cambiar, paso a paso]

### Beneficios
- [Mejora 1 esperada]
- [Mejora 2 esperada]

### Esfuerzo Estimado
- Tiempo: [X días/semanas]
- Riesgo: [Bajo/Medio/Alto]
- Breaking changes: [Sí/No, cuáles]

### Plan de Ejecución
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

### Métricas de Éxito
- [Cómo sabremos que funcionó]
```

### 5️⃣ ESTRATEGIAS DE REFACTOR

#### Estrategia A: Boy Scout Rule
**"Deja el código mejor de como lo encontraste"**

- Pequeñas mejoras en cada cambio
- Bajo riesgo, acumula con el tiempo
- Ideal para deuda técnica dispersa

#### Estrategia B: Strangler Fig Pattern
**"Reemplaza gradualmente el sistema legacy"**

- Crea nueva arquitectura en paralelo
- Migra funcionalidad por funcionalidad
- Ideal para reescrituras parciales

#### Estrategia C: Big Refactor
**"Detén todo y refactoriza"**

- Requiere buy-in del equipo
- Alto riesgo, alta recompensa
- Solo para problemas críticos

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Refactor sin tests | Rompes cosas sin saber | Tests primero, refactor después |
| Refactor perfecto | Nunca termina, no entrega valor | Mejora incremental > perfección |
| Arquitectura astronauta | Sobre-ingeniería para problemas futuros | YAGNI: construye para hoy |
| Culpar al código anterior | No entendías el contexto entonces | Asume buenas intenciones, mejora desde ahí |
| Ignorar deuda técnica | Interés compuesto te alcanza | Paga deuda regularmente |

## Adapt to the User

- **Para startups:** Enfócate en velocidad, deuda aceptable si es consciente
- **Para scale-ups:** Invierte en arquitectura, la deuda frena el growth
- **Para legacy:** Refactor incremental, strangler pattern
- **Para greenfield:** Establece arquitectura intencional temprano

## Scope

Este skill SÓLO:
- Analiza arquitectura existente
- Identifica smells y deuda técnica
- Propone mejoras priorizadas
- Sugiere estrategias de refactor

Este skill NUNCA:
- Refactoriza sin tests o plan
- Impone arquitectura sin contexto
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/arch-improver/`:

- `memory.md` - Análisis activos, hallazgos
- `assessments/` - Evaluaciones arquitectónicas completas
- `improvements/` - Mejoras propuestas, estado, progreso

## Related Skills

- `debug-diagnose` - Para bugs causados por mala arquitectura
- `tdd-helper` - Para crear tests antes de refactor
- `grill-with-docs` - Para documentar arquitectura intencional
- `code-context` - Para entender código antes de analizar

## Feedback

- Si fue útil: `clawhub star arch-improver`
- Mantente actualizado: `clawhub sync`
