---
name: TDD Helper
slug: tdd-helper
version: 1.0.0
homepage: https://clawic.com/skills/tdd-helper
description: "Test-driven development con loop red-green-refactor. Construye features o fixea bugs una vertical slice a la vez."
changelog: "Skill inicial para TDD en OpenClaw."
metadata: {"clawdbot":{"emoji":"🧪","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/tdd-helper/"]}}
---

## When to Use

Usa este skill cuando:
- Vas a implementar una feature nueva
- Vas a fixear un bug
- Quieres asegurar cobertura de tests antes de codificar
- Necesitas refactorizar con confianza

**NO uses** para:
- Prototipos desechables
- Scripts one-off
- Cuando el test es más complejo que el código (excepcional)

## Architecture

Memoria vive en `~/tdd-helper/`.

```
~/tdd-helper/
├── memory.md        # Sesiones TDD activas, coverage goals
├── sessions/        # Historial de sesiones TDD
└── patterns/        # Patrones de test reutilizables
```

## The Red-Green-Refactor Loop

### 🔴 FASE 1: RED (Test Fallando)

**Objetivo:** Escribir un test que falla y define el comportamiento deseado.

**Reglas:**
1. Escribe el test MÁS PEQUEÑO que puedas
2. El test debe fallar por la razón correcta
3. No escribas código de producción aún

**Checklist:**
- [ ] El test describe un comportamiento específico
- [ ] El test es autocontenido (no depende de otros tests)
- [ ] El test tiene nombre claro (should_do_X_when_Y)
- [ ] El test falla antes de implementar

**Ejemplo:**
```typescript
// ❌ Muy grande
describe('User authentication', () => {
  // 20 tests aquí...
});

// ✅ Tamaño correcto
it('should return user id when login succeeds with valid credentials', () => {
  // Test específico y pequeño
});
```

### 🟢 FASE 2: GREEN (Test Pasando)

**Objetivo:** Hacer pasar el test lo más rápido posible.

**Reglas:**
1. Escribe el código MÁS SIMPLE que haga pasar el test
2. No te preocupes por elegancia o duplicación
3. Si el test pasa, PARA de codificar

**Mentalidad:**
- "Fake it till you make it" está OK
- Hardcodear valores está OK (por ahora)
- La duplicación está OK (se limpia en refactor)

**Ejemplo:**
```typescript
// Test
expect(calculateDiscount(100, 'VIP')).toBe(20);

// ✅ Implementación más simple (aunque sea hardcoded)
function calculateDiscount(amount: number, type: string): number {
  if (type === 'VIP') return 20;
  return 0;
}
```

### 🔵 FASE 3: REFACTOR (Limpiar Código)

**Objetivo:** Mejorar el código manteniendo los tests pasando.

**Reglas:**
1. Los tests deben pasar ANTES de refactorizar
2. Cambios pequeños y frecuentes
3. Tests pasan después de cada cambio

**Refactors comunes:**
- Eliminar duplicación
- Renombrar para claridad
- Extraer funciones/métodos
- Simplificar condicionales
- Mejorar estructura de datos

**Checklist:**
- [ ] Tests pasan después del refactor
- [ ] Código es más legible que antes
- [ ] No hay duplicación obvia
- [ ] Nombres son descriptivos
- [ ] Funciones son pequeñas (<20 líneas ideal)

## TDD Workflow Completo

### Paso 1: Entender el Requerimiento

**Antes de escribir tests:**
- ¿Qué comportamiento se necesita?
- ¿Cuáles son los edge cases?
- ¿Qué inputs y outputs?

**Escribe una lista de tests potenciales:**
```
Tests para "calcular descuento":
- [ ] 0% para cliente normal
- [ ] 10% para cliente premium
- [ ] 20% para cliente VIP
- [ ] 0% para monto negativo
- [ ] Maneja monto 0
- [ ] Redondea a 2 decimales
```

### Paso 2: Ordenar Tests

**Orden sugerido:**
1. Happy path (caso normal)
2. Edge cases (límites)
3. Error cases (inputs inválidos)

### Paso 3: Iterar sobre cada test

```
PARA CADA test en la lista:
  1. Escribe el test (RED)
  2. Ejecuta tests → debe fallar solo este
  3. Implementa mínimo para pasar (GREEN)
  4. Ejecuta tests → todos deben pasar
  5. Refactor si es necesario
  6. Commit pequeño
```

### Paso 4: Coverage Check

**Después de completar todos los tests:**
- [ ] ¿Todos los paths están cubiertos?
- [ ] ¿Edge cases están testeados?
- [ ] ¿Error handling está cubierto?

## Test Patterns

### AAA Pattern (Arrange-Act-Assert)

```typescript
it('should return discounted price for VIP customer', () => {
  // Arrange
  const price = 100;
  const customerType = 'VIP';
  
  // Act
  const result = calculateDiscount(price, customerType);
  
  // Assert
  expect(result).toBe(20);
});
```

### Given-When-Then

```typescript
it('should return discounted price for VIP customer', () => {
  // Given
  const price = 100;
  const customerType = 'VIP';
  
  // When
  const result = calculateDiscount(price, customerType);
  
  // Then
  expect(result).toBe(20);
});
```

### Test Doubles

**Mock:** Verifica interacciones
```typescript
const mockRepo = {
  save: jest.fn().mockResolvedValue({ id: 1 })
};
// ... después verifica
expect(mockRepo.save).toHaveBeenCalledWith(expected);
```

**Stub:** Provee datos predefinidos
```typescript
const stubUser = {
  id: 1,
  name: 'Test',
  type: 'VIP'
};
```

**Spy:** Observa llamadas sin modificar comportamiento
```typescript
const spy = jest.spyOn(console, 'log');
// ... ejecuta código
expect(spy).toHaveBeenCalledWith('expected');
```

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Tests muy grandes | Difícil saber qué falla | Tests pequeños, uno por comportamiento |
| Testear implementación | Tests frágiles a refactors | Testea comportamiento, no implementación |
| Green sin refactor | Deuda técnica acumulada | Siempre refactor después de green |
| Mockear todo | Tests no reflejan realidad | Mockea solo boundaries externos |
| Ignorar edge cases | Bugs en producción | Lista edge cases antes de empezar |

## Adapt to the User

- **Para juniors:** Explica el loop paso a paso, modela la mentalidad TDD
- **Para seniors:** Enfócate en diseño emergente, patrones, tradeoffs
- **Para legacy code:** Usa "Sprout Method" pattern, test alrededor del cambio
- **Para equipos:** Establece estándares de naming, estructura, coverage mínimo

## Scope

Este skill SÓLO:
- Guía el loop red-green-refactor
- Sugiere patrones de test apropiados
- Ayuda a identificar qué test escribir después
- Mantiene disciplina TDD

Este skill NUNCA:
- Escribe tests que no sean necesarios
- Ignora el refactor después de green
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/tdd-helper/`:

- `memory.md` - Sesiones TDD activas, goals de coverage
- `sessions/` - Historial de sesiones completadas
- `patterns/` - Patrones de test reutilizables

## Related Skills

- `debug-diagnose` - Cuando un test falla inesperadamente
- `plan-to-issues` - Para convertir specs en tests
- `arch-improver` - Para evaluar diseño del código testeado

## Feedback

- Si fue útil: `clawhub star tdd-helper`
- Mantente actualizado: `clawhub sync`
