# 🔍 Skill: Diagnóstico de Bugs

**Comando:** `/diagnostico`  
**Categoría:** Ingeniería  
**Dificultad:** Intermedio  
**Tiempo:** 20-40 min por bug

---

## 📖 Descripción

Método estructurado para debuggear bugs difíciles y problemas de performance.

Este skill evita que el agente parche al azar. En su lugar, sigue un proceso científico: reproducir → minimizar → hipotetizar → instrumentar → fix → regresión.

---

## 🎯 Cuándo Usar

✅ **Usar cuando:**
- Hay un bug que no es obvio
- El código falla de forma intermitente
- Hay un problema de performance
- Los tests fallan sin razón aparente

❌ **NO usar cuando:**
- Es un error de sintaxis obvio
- El error ya está documentado
- Es un cambio cosmético menor

---

## 📋 Instrucciones para el Agente

```markdown
# ROL: Eres un experto en debugging y diagnóstico de bugs

# PROCESO CIENTÍFICO:

## FASE 1: REPRODUCIR (5-10 min)

1. **Entender el síntoma:**
   - ¿Qué debería pasar?
   - ¿Qué está pasando realmente?
   - ¿Cuándo ocurre?
   - ¿Con qué frecuencia?

2. **Reproducir consistentemente:**
   - Crear script/test que reproduzca el bug
   - Identificar pasos exactos
   - Aislar variables (datos, entorno, timing)
   - Tomar screenshots/logs del error

3. **Documentar reproducción:**
   ```markdown
   ## Pasos para reproducir:
   1. [Paso 1]
   2. [Paso 2]
   3. [Ver error]

   ## Comportamiento esperado:
   [Qué debería pasar]

   ## Comportamiento actual:
   [Qué pasa realmente]

   ## Frecuencia:
   [Siempre / 50% / Rara vez]
   ```

## FASE 2: MINIMIZAR (5-10 min)

4. **Reducir el caso:**
   - Eliminar código no relacionado
   - Crear ejemplo mínimo (MCVE)
   - Aislar el componente/problemático
   - Simplificar datos de test

5. **Identificar patrón:**
   - ¿Qué tienen en común los casos que fallan?
   - ¿Qué diferencia los casos que pasan?
   - ¿Hay un trigger específico?

## FASE 3: HIPOTETIZAR (5 min)

6. **Generar hipótesis:**
   - Lista 3-5 causas posibles
   - Ordénalas por probabilidad
   - Para cada una, define cómo verificar

7. **Ejemplo de hipótesis:**
   ```
   Hipótesis 1: Race condition en la carga de datos
   - Verificación: Agregar logs de timing

   Hipótesis 2: Estado no se actualiza correctamente
   - Verificación: Loggear estado antes/después

   Hipótesis 3: Problema de caché
   - Verificación: Limpiar caché y probar
   ```

## FASE 4: INSTRUMENTAR (5-10 min)

8. **Agregar instrumentación:**
   - Logs estratégicos (no scattergun)
   - Breakpoints o debugger
   - Métricas de performance
   - Assertions para verificar invariantes

9. **Ejecutar con instrumentación:**
   - Correr caso de reproducción
   - Capturar logs/output
   - Identificar dónde diverge de lo esperado

## FASE 5: FIX (10-20 min)

10. **Implementar fix:**
    - Basado en hipótesis confirmada
    - Fix mínimo (no over-engineer)
    - No tocar código no relacionado
    - Comentar por qué el fix funciona

11. **Verificar fix:**
    - Caso original pasa
    - Tests existentes pasan
    - No hay regresiones
    - Edge cases cubiertos

## FASE 6: REGRESIÓN (5 min)

12. **Agregar test de regresión:**
    - Test que falla SIN el fix
    - Test que pasa CON el fix
    - Cubre el caso específico del bug
    - Nombra claramente (ej: "should handle null response")

13. **Documentar learnings:**
    ```markdown
    ## Root Cause
    [Qué causó el bug]

    ## Fix
    [Cómo se arregló]

    ## Prevention
    [Cómo evitar que vuelva a pasar]
    ```

# REGLAS DE ORO:

- ✅ NUNCA parches sin entender la causa raíz
- ✅ SIEMPRE reproduce antes de fixear
- ✅ AGREGA test de regresión siempre
- ✅ DOCUMENTA el learnings
- ✅ COMPARTE el conocimiento con el equipo

# EVITAR:

- ❌ Cambiar 10 cosas a la vez (no sabrás cuál funcionó)
- ❌ Parchar síntomas (fixea la causa)
- ❌ Asumir sin verificar (testea cada hipótesis)
- ❌ Olvidar test de regresión (volverá a pasar)
```

---

## 💡 Ejemplo de Uso

### Usuario:
```
/diagnostico

La app se cuelga a veces cuando cargo la página de perfil.
No pasa siempre, como 30% de las veces.
```

### Agente:
```markdown
Entendido. Bug intermitente en carga de perfil.

## FASE 1: REPRODUCIR

Necesito más información:

1. **¿Qué significa "se cuelga"?**
   - ¿Pantalla blanca?
   - ¿Loading infinito?
   - ¿Error en consola?
   - ¿Navegador se congela?

2. **¿Cuándo ocurre?**
   - ¿Siempre en el mismo perfil?
   - ¿Con ciertos datos?
   - ¿Después de hacer algo específico?

3. **¿Entorno?**
   - ¿Qué navegador?
   - ¿Qué dispositivo?
   - ¿Red rápida/lenta?

Por favor dame detalles para intentar reproducir.
```

### Usuario:
```
Es loading infinito.
Pasa en Chrome desktop.
No parece depender del perfil, pasa aleatoriamente.
En la consola veo: "Cannot read property 'name' of undefined"
```

### Agente:
```markdown
Perfecto. Ya tenemos información valiosa.

## HIPÓTESIS:

El error "Cannot read property 'name' of undefined" sugiere que:

1. **Hipótesis 1:** La API a veces no devuelve datos
   - Verificación: Loggear response de la API

2. **Hipótesis 2:** El estado se inicializa antes de tener datos
   - Verificación: Revisar orden de ejecución

3. **Hipótesis 3:** Hay una race condition
   - Verificación: Agregar logs de timing

## SIGUIENTE PASO:

Voy a agregar instrumentación para capturar más información:

```javascript
// En el componente de perfil
useEffect(() => {
  console.log('🔍 Iniciando carga de perfil...');
  
  fetchProfile()
    .then(data => {
      console.log('✅ Datos recibidos:', data);
      console.log('📝 data.name:', data?.name);
      setProfile(data);
    })
    .catch(err => {
      console.error('❌ Error en fetch:', err);
    });
}, []);
```

¿Puedes:
1. Recargar la página 5-10 veces
2. Copiar los logs de la consola
3. Enviármelos para analizar?

Esto nos dirá si el problema es:
- La API no responde (no hay logs de "✅")
- Los datos llegan mal (data.name es undefined)
- El estado se setea antes de tiempo
```

[... continúa el proceso de diagnóstico ...]

---

## 📊 Plantilla de Reporte de Bug

```markdown
# Bug: [Título corto]

## Resumen
[Descripción en 1-2 oraciones]

## Reproducción
1. [Paso 1]
2. [Paso 2]
3. [Ver error]

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué pasa realmente]

## Frecuencia
[Siempre / 50% / Rara vez]

## Root Cause
[Qué causó el bug]

## Fix Aplicado
[Qué código se cambió]

## Test de Regresión
[Qué test asegura que no volverá a pasar]

## Prevention
[Cómo evitar que vuelva a ocurrir]
```

---

## ⚠️ Errores Comunes

| Error | Cómo Evitarlo |
|-------|---------------|
| Parchar sin entender | **Reproducir** primero |
| Cambiar muchas cosas | **Una variable** a la vez |
| No agregar test | Test de **regresión** obligatorio |
| No documentar | Escribir **learnings** |

---

## 🎓 Principios Subyacentes

- **Método Científico** - Hipótesis → Experimento → Conclusión
- **Rubber Duck Debugging** - Explicar el problema ayuda a entenderlo
- **The Pragmatic Programmer** - "Always take small, deliberate steps"

---

## 🔗 Recursos

- [The Art of Debugging](https://jvns.ca/debugging/)
- [Rubber Duck Problem Solving](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

---

*Skill creado para OpenClaw en Español - Hecho con 💚 por @avilacarlosdev*
