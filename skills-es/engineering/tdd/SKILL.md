# 🧪 Skill: TDD (Test-Driven Development)

**Comando:** `/tdd`  
**Categoría:** Ingeniería  
**Dificultad:** Intermedio  
**Tiempo:** 15-30 min por feature

---

## 📖 Descripción

Desarrollo guiado por tests usando el ciclo **Red-Green-Refactor**.

Este skill fuerza al agente a escribir tests PRIMERO, luego el código mínimo para pasarlos, y finalmente refactorizar. Resultado: código más limpio, menos bugs, y documentación viva.

---

## 🎯 Cuándo Usar

✅ **Usar cuando:**
- Vas a implementar una feature nueva
- Vas a fixear un bug (primero escribe el test que falla)
- Quieres asegurar que el código no se rompa en el futuro
- Estás trabajando en código crítico (pagos, auth, datos)

❌ **NO usar cuando:**
- Es un cambio cosmético (CSS, textos)
- Es un prototipo rápido que vas a desechar
- El deadline es PARA YA (aunque deberías usar TDD igual)

---

## 🔄 El Ciclo TDD

```
1. ROJO 🟥
   - Escribe un test que falle
   - Ejecuta tests → debe fallar
   - NO escribas código de producción aún

2. VERDE 🟩
   - Escribe el código MÍNIMO para pasar el test
   - Ejecuta tests → debe pasar
   - No importa si el código es feo

3. REFACTOR 🛠️
   - Mejora el código (sin cambiar comportamiento)
   - Ejecuta tests → debe seguir pasando
   - Elimina duplicación, mejora nombres, simplifica

4. REPITE 🔄
   - Vuelve al paso 1 con el siguiente caso
```

---

## 📋 Instrucciones para el Agente

```markdown
# ROL: Eres un experto en TDD

# PROCESO:

1. **PRIMERO:** Pídeme que describa la feature o bug a fixear
   - ¿Qué debe hacer?
   - ¿Cuáles son los casos borde?
   - ¿Qué inputs/outputs esperamos?

2. **SEGUNDO:** Escribe UN test que falle
   - Un solo caso de prueba
   - Test unitario, aislado, rápido
   - Nombra claramente qué está probando

3. **TERCERO:** Ejecuta el test
   - Debe fallar (si pasa, el test está mal)
   - Muestra el error claramente

4. **CUARTO:** Escribe código MÍNIMO para pasar
   - No over-engineer
   - Hardcodea si es necesario
   - Solo lo necesario para pasar ESTE test

5. **QUINTO:** Ejecuta tests
   - Debe pasar (100% green)
   - Si falla, debuggea

6. **SEXTO:** Refactoriza
   - ¿Hay duplicación?
   - ¿Nombres claros?
   - ¿Se puede simplificar?
   - Tests deben seguir pasando

7. **SÉPTIMO:** Repite desde el paso 1
   - Siguiente caso de prueba
   - Siguiente feature
   - Siguiente bug

# REGLAS DE ORO:

- 🚫 NUNCA escribas código de producción sin un test fallando primero
- 🚫 NUNCA escribas múltiples tests a la vez (uno por uno)
- 🚫 NUNCA refactorices sin tests pasando
- ✅ SIEMPRE ejecuta tests después de cada cambio
- ✅ SIEMPRÉ muestra el output de los tests (rojo o verde)
- ✅ SIEMPRE pregunta si quiero continuar al siguiente test

# STACK:

- Framework de tests: [preguntar]
- Runner: [preguntar]
- Lenguaje: [preguntar]
```

---

## 💡 Ejemplo de Uso

### Usuario:
```
/tdd

Quiero implementar una función que valide emails.
```

### Agente (siguiendo el skill):
```markdown
¡Perfecto! Vamos a usar TDD.

## Paso 1: Entender requerimientos

Antes de escribir código, necesito saber:

1. **¿Qué reglas de validación aplican?**
   - ¿Solo formato (algo@algo.algo)?
   - ¿Verificar dominios específicos?
   - ¿Bloquear emails desechables?

2. **¿Cuáles son los casos borde?**
   - `test@example.com` ✅
   - `test@example` ❌
   - `@example.com` ❌
   - `test @example.com` ❌
   - Mayúsculas: `Test@Example.com` ¿?

3. **¿Qué framework de tests usamos?**
   - Jest, Vitest, Mocha, pytest?

Por favor responde para escribir el PRIMER test.
```

### Usuario:
```
1. Solo formato básico
2. Los casos que mencionaste están bien
3. Vitest

El primer test debería ser: email válido → true
```

### Agente:
```typescript
// Paso 2: Escribir test que falle (ROJO 🟥)

// email.test.ts
import { describe, it, expect } from 'vitest'
import { validarEmail } from './email'

describe('validarEmail', () => {
  it('debe retornar true para email válido', () => {
    expect(validarEmail('test@example.com')).toBe(true)
  })
})
```

```bash
# Paso 3: Ejecutar test
$ npm run test

❌ FAIL  email.test.ts
   validarEmail
     × debe retornar true para email válido

Error: validarEmail is not a function
```

Perfecto, el test falla como esperamos. Ahora escribo el código MÍNIMO:

```typescript
// email.ts
export function validarEmail(email: string): boolean {
  return email === 'test@example.com' // Hardcodeado, solo para pasar
}
```

```bash
# Paso 5: Ejecutar tests
$ npm run test

✅ PASS  email.test.ts
   validarEmail
     ✓ debe retornar true para email válido
```

¡Verde! 🟩 Ahora refactorizamos:

```typescript
// email.ts - REFACTOR
export function validarEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
}
```

```bash
# Ejecutar tests después de refactor
$ npm run test

✅ PASS  email.test.ts
   validarEmail
     ✓ debe retornar true para email válido
```

## ¿Continuamos con el siguiente caso?

Siguiente test: email inválido (sin @) → false

¿Procedo?
```

---

## 📚 Recursos

- [Red-Green-Refactor Explained](https://en.wikipedia.org/wiki/Test-driven_development)
- [Vitest Documentation](https://vitest.dev)
- [Jest Documentation](https://jestjs.io)

---

## ⚠️ Errores Comunes

| Error | Cómo Evitarlo |
|-------|---------------|
| Escribir múltiples tests antes del código | **UN test a la vez**, disciplina |
| Código de producción muy complejo | Escribe código **mínimo** para pasar |
| Saltarse el refactor | El refactor es **obligatorio**, no opcional |
| Tests lentos o acoplados | Tests unitarios = **rápidos y aislados** |

---

## 🎓 Principios Subyacentes

- **The Pragmatic Programmer** - "Always take small, deliberate steps"
- **Extreme Programming** - TDD es una práctica central de XP
- **Clean Code** - Tests como documentación viva

---

*Skill creado para OpenClaw en Español - Hecho con 💚 por @avilacarlosdev*
