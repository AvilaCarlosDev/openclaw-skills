# 🐙 Skill: Contribución GitHub

**Comando:** `/contribucion`  
**Categoría:** GitHub  
**Dificultad:** Intermedio  
**Tiempo:** 30-60 min por contribución

---

## 📖 Descripción

Prepara contribuciones a proyectos open source en GitHub siguiendo **mejores prácticas** para maximizar aceptación.

Este skill guía todo el proceso: buscar issues, analizar código, hacer fix, testear, y crear PR profesional.

---

## 🎯 Cuándo Usar

✅ **Usar cuando:**
- Quieres contribuir a open source
- Buscas ganar reputación en GitHub
- Quieres hacer networking con maintainers
- Necesitas contenido para tu portfolio

❌ **NO usar cuando:**
- Es tu primer día con Git/GitHub
- No tienes tiempo para hacer la contribución bien
- El proyecto no tiene guidelines de contribución

---

## 📋 Instrucciones para el Agente

```markdown
# ROL: Eres un experto en contribuciones open source

# PROCESO PASO A PASO:

## FASE 1: BÚSQUEDA (15 min)

1. **Buscar issues** con estas etiquetas:
   - `good first issue`
   - `help wanted`
   - `beginner friendly`
   - `documentation`

2. **Filtrar proyectos** por:
   - Lenguaje: JavaScript/TypeScript/React/Python
   - Stars: 10-500 (ni muy grandes ni muy pequeños)
   - Actividad: Commits en últimos 30 días
   - Maintainers: Responden issues (< 1 semana)

3. **Seleccionar 3-5 issues** potenciales y presentármelos:
   - Link al issue
   - Link al repo
   - Qué hay que hacer
   - Dificultad estimada (1-5)
   - Tiempo estimado

## FASE 2: ANÁLISIS (15 min)

4. **Para el issue seleccionado:**
   - Leer issue completo y comentarios
   - Revisar CONTRIBUTING.md del proyecto
   - Ver issues similares cerrados (cómo los resolvieron)
   - Entender estructura del código base
   - Identificar archivos a modificar

5. **Preparar plan de acción:**
   - Qué archivos tocar
   - Qué tests ejecutar
   - Cómo testear localmente
   - Posibles riesgos

## FASE 3: EJECUCIÓN (30-60 min)

6. **Clonar y configurar:**
   ```bash
   git clone [repo]
   cd [repo]
   npm install / pip install -r requirements.txt
   npm run dev / python app.py
   ```

7. **Reproducir el issue:**
   - Verificar que el bug existe
   - O entender qué feature falta
   - Tomar screenshots si es visual

8. **Implementar fix:**
   - Código mínimo para resolver
   - Seguir estilo del proyecto
   - No refactorizar código no relacionado
   - Comentar si es necesario

9. **Testear:**
   - Tests existentes pasan
   - Agregar tests si aplica
   - Testear manualmente
   - Verificar en diferentes escenarios

## FASE 4: PR (15 min)

10. **Preparar commit:**
    ```bash
    git checkout -b fix/issue-123
    git add .
    git commit -m "fix: [descripción corta]"
    git push origin fix/issue-123
    ```

11. **Crear PR con esta plantilla:**
    ```markdown
    ## Descripción
    [Qué hace este PR y por qué]

    ## Cambios
    - [ ] Archivo 1: [qué cambié]
    - [ ] Archivo 2: [qué cambié]

    ## Testing
    - [ ] Tests pasan
    - [ ] Probado localmente
    - [ ] Screenshots (si es visual)

    ## Issue
    Fixes #[número del issue]
    ```

12. **Monitorear respuesta:**
    - Responder en < 24 horas
    - Hacer cambios solicitados
    - Ser amable y profesional

# REGLAS DE ORO:

- ✅ Leer CONTRIBUTING.md SIEMPRE
- ✅ Seguir convenciones del proyecto
- ✅ Tests pasan antes de hacer PR
- ✅ Descripción clara y detallada
- ✅ Responder rápido a feedback
- ✅ Ser humilde y agradecer

# EVITAR:

- ❌ Cambios gigantes sin discutir
- ❌ Refactorizar código no relacionado
- ❌ Ignorar feedback de maintainers
- ❌ Ser defensivo si rechazan el PR
- ❌ Spam (múltiples PRs de baja calidad)
```

---

## 💡 Ejemplo de Uso

### Usuario:
```
/contribucion

Quiero contribuir hoy. Busca issues de JavaScript/React.
```

### Agente:
```markdown
¡Excelente! Buscando issues...

## 🔍 5 Issues Encontrados:

### 1. Fix typo in documentation
- **Repo:** https://github.com/example/react-lib
- **Issue:** https://github.com/example/react-lib/issues/234
- **Qué:** Corregir error ortográfico en README
- **Dificultad:** ⭐ (muy fácil)
- **Tiempo:** 15 min
- **Maintainer:** Responde en 1-2 días

### 2. Add unit tests for utils
- **Repo:** https://github.com/example/js-utils
- **Issue:** https://github.com/example/js-utils/issues/89
- **Qué:** Agregar tests para funciones utilitarias
- **Dificultad:** ⭐⭐⭐ (intermedio)
- **Tiempo:** 45 min
- **Maintainer:** Responde en < 24h

### 3. Improve accessibility on button component
- **Repo:** https://github.com/example/ui-kit
- **Issue:** https://github.com/example/ui-kit/issues/156
- **Qué:** Agregar aria-labels a botones
- **Dificultad:** ⭐⭐ (fácil-intermedio)
- **Tiempo:** 30 min
- **Maintainer:** Muy activo

[... 2 más ...]

¿Cuál quieres atacar primero?

Te recomiendo el #1 o #3 para empezar (fáciles, maintainers activos).
```

### Usuario:
```
El #3 de accessibility. Vamos con ese.
```

### Agente:
```markdown
¡Perfecto! Vamos con el issue de accesibilidad.

## 📋 PLAN DE ACCIÓN:

**Issue:** Improve accessibility on button component
**Repo:** https://github.com/example/ui-kit
**Files a modificar:** `src/components/Button.jsx`

### Pasos:

1. Clonar repo
2. Instalar dependencias
3. Entender estructura del Button component
4. Agregar aria-labels según issue
5. Testear con screen reader (o verificar código)
6. Correr tests existentes
7. Crear PR

¿Procedo a clonar?
```

[... continúa guiando paso a paso ...]

---

## 📊 Checklist de Calidad

Antes de hacer push, verificar:

```
[ ] Código sigue estilo del proyecto
[ ] Tests pasan (npm test / pytest)
[ ] No hay console.log o debug code
[ ] Commit message sigue convenciones
[ ] PR description está completa
[ ] Issue está linkeado (Fixes #123)
```

---

## ⚠️ Errores Comunes

| Error | Cómo Evitarlo |
|-------|---------------|
| No leer CONTRIBUTING.md | **Siempre** leer primero |
| Cambios muy grandes | Empezar con issues pequeños |
| Ignorar feedback | Responder en < 24h |
| No testear | Tests locales **siempre** |
| PR sin descripción | Usar plantilla siempre |

---

## 🎓 Principios Subyacentes

- **Open Source Etiquette** - Respeto y gratitud
- **Convencional Commits** - Mensajes estandarizados
- **PR Best Practices** - Descripciones claras, tests incluidos

---

## 🔗 Recursos

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Contributions](https://github.com/firstcontributions/first-contributions)
- [Good First Issues](https://goodfirstissues.com)

---

*Skill creado para OpenClaw en Español - Hecho con 💚 por @avilacarlosdev*
