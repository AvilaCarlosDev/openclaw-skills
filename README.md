# 🛠️ OpenClaw Skills - Colección Completa

> **Skills para OpenClaw** - Herramientas especializadas para desarrolladores Full Stack, EdTech y automatización con IA.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Total Skills](https://img.shields.io/badge/Skills-23-green)](#skills-disponibles)

---

## 📖 ¿Qué es un Skill?

Un **Skill** es un agente especializado de OpenClaw con:
- **Propósito claro**: Una función específica que hace bien
- **Memoria persistente**: Archivos locales para contexto duradero
- **Workflow documentado**: Pasos reproducibles para resultados consistentes
- **Adaptabilidad**: Se ajusta al nivel del usuario (junior/senior/leadership)

---

## 🚀 Quickstart

### Instalar un Skill

```bash
# Desde ClawHub (recomendado)
clawhub install <nombre-del-skill>

# O copia el SKILL.md a tu workspace
cp skills/<nombre>/SKILL.md ~/.openclaw/workspace/skills/<nombre>/
```

### Usar un Skill

Los skills se activan automáticamente cuando tu tarea coincide con su descripción. También puedes invocarlos explícitamente:

```
/usa <nombre-skill> <tu tarea>
```

---

## 📚 Skills Disponibles (23 total)

### 🎨 Diseño y UI (1 skill)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`refero-styles`](./refero-styles/SKILL.md) | Extrae colores, tipografía, spacing y componentes de URLs | Cuando quieres analizar el diseño de un sitio web existente |

### 🔍 Búsqueda y Web (3 skills)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`safe_search`](./safe_search/SKILL.md) | Búsqueda web segura con protección contra prompt injection | Cuando necesitas información de internet sobre un tema |
| [`safe_fetch`](./safe_fetch/SKILL.md) | Obtención segura de páginas web | Cuando tienes una URL específica para analizar |
| [`safe-web`](./safe-web/SKILL.md) | Navegación web segura | Para interactuar con contenido web de forma protegida |

### 💻 Programación y Desarrollo (6 skills)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`programming`](./programming/SKILL.md) | Skill general de programación | Para tareas de coding, debugging y desarrollo |
| [`debug-diagnose`](./debug-diagnose/SKILL.md) | Loop disciplinado para bugs difíciles: reproducir → minimizar → hipotetizar → instrumentar → fijar → test | Cuando hay un bug que requiere investigación sistemática |
| [`tdd-helper`](./tdd-helper/SKILL.md) | Test-driven development con loop red-green-refactor | Para implementar features o fixear bugs con tests |
| [`code-context`](./code-context/SKILL.md) | Zoom out para entender código desconocido en contexto del sistema | Antes de modificar código que no escribiste |
| [`quick-prototype`](./quick-prototype/SKILL.md) | Prototipos desechables para explorar diseño (terminal apps, UIs múltiples) | Para validar ideas rápidamente antes de comprometerte |
| [`arch-improver`](./arch-improver/SKILL.md) | Encuentra oportunidades de mejora en arquitectura del codebase | Cuando el código se volvió difícil de cambiar |

### 📋 Productividad y Gestión (6 skills)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`grill-me`](./grill-me/SKILL.md) | Entrevista implacable sobre un plan hasta resolver cada rama de decisión | Cuando quieres que desafíen tu plan antes de ejecutar |
| [`grill-with-docs`](./grill-with-docs/SKILL.md) | Como grill-me pero documenta en CONTEXT.md y ADRs | Para alineación de requisitos + documentación arquitectónica |
| [`issue-triage`](./issue-triage/SKILL.md) | Triage de issues con máquina de estados, labels y routing | Para clasificar y priorizar issues nuevos en GitHub |
| [`plan-to-issues`](./plan-to-issues/SKILL.md) | Convierte planes/PRDs en GitHub issues con vertical slices | Para dividir features grandes en issues manejables |
| [`chat-to-prd`](./chat-to-prd/SKILL.md) | Sintetiza conversaciones en PRDs y crea GitHub issues | Después de discutir un feature, para documentar lo acordado |
| [`compressed-mode`](./compressed-mode/SKILL.md) | Comunicación ultra-comprimida (~75% menos tokens) | Cuando prefieres densidad sobre explicaciones extensas |

### 🛡️ Seguridad y Control (2 skills)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`cybersecurity`](./cybersecurity/SKILL.md) | Triage de seguridad, threat modeling, incident reporting | Para análisis de seguridad autorizado y triage de incidentes |
| [`git-guardrails`](./git-guardrails/SKILL.md) | Hooks para bloquear comandos git peligrosos | Para prevenir accidents con force push, reset --hard, etc. |

### 📈 Marketing y Contenido (3 skills)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`content-marketing`](./content-marketing/SKILL.md) | Planificación, creación y distribución de contenido | Para estrategias de marketing de contenidos |
| [`seo`](./seo/SKILL.md) | Auditoría de sitios, content writing, keyword research | Para optimización SEO y estrategias de ranking |
| [`graphic-design`](./graphic-design/SKILL.md) | Soporte de diseño desde básico hasta producción profesional | Para tareas de diseño gráfico y teoría visual |

### 📝 Reuniones y Notas (2 skills)

| Skill | Descripción | Cuándo Usar |
|-------|-------------|-------------|
| [`meeting-notes`](./meeting-notes/SKILL.md) | Notas de reuniones → resúmenes limpios | Para organizar y resumir notas de reuniones |
| [`ai-meeting-notes`](./ai-meeting-notes/SKILL.md) | Action items con owners y deadlines, auto-guardado | Para extraer tareas accionables de transcripciones |

---

## 🏗️ Estructura de un Skill

Cada skill sigue esta estructura:

```
<nombre-skill>/
└── SKILL.md          # Definición del skill (YAML frontmatter + instrucciones)
```

### Frontmatter YAML

```yaml
---
name: Nombre del Skill
slug: nombre-skill
version: 1.0.0
homepage: https://clawic.com/skills/nombre-skill
description: "Descripción corta del propósito"
changelog: "Descripción de cambios en esta versión"
metadata:
  clawdbot:
    emoji: "🔥"
    requires:
      bins: []  # Binarios necesarios
    os: ["linux", "darwin", "win32"]
    configPaths: ["~/nombre-skill/"]
---
```

### Secciones del SKILL.md

1. **When to Use** - Cuándo activar este skill
2. **Architecture** - Dónde vive la memoria del skill
3. **Core Workflow** - Pasos principales del skill
4. **Adapt to the User** - Cómo ajustarse al nivel del usuario
5. **Common Traps** - Errores comunes y cómo evitarlos
6. **Scope** - Qué hace y qué NO hace el skill
7. **Data Storage** - Dónde guarda información persistente
8. **Security & Privacy** - Consideraciones de seguridad
9. **Related Skills** - Skills complementarios
10. **Feedback** - Cómo dar feedback o mantenerse actualizado

---

## 🤝 Contribuir

### Crear un Nuevo Skill

1. **Fork** este repositorio
2. **Crea una carpeta** con el nombre de tu skill
3. **Agrega SKILL.md** siguiendo la estructura anterior
4. **Prueba** el skill en tu OpenClaw local
5. **Envía un PR** con descripción del propósito y casos de uso

### Lineamientos

- ✅ **Una responsabilidad clara**: Un skill, un propósito
- ✅ **Memoria persistente**: Usa `~/<skill>/` para contexto duradero
- ✅ **Workflow documentado**: Pasos reproducibles
- ✅ **Adaptable**: Funciona para juniors y seniors
- ✅ **Seguro**: No modifica sistemas sin confirmación
- ❌ **No skills genéricos**: Debe resolver un problema específico

---

## 📄 Licencia

MIT License - ver [LICENSE](./LICENSE) para detalles.

---

## 🔗 Recursos

- **OpenClaw Docs**: https://docs.openclaw.ai
- **ClawHub**: https://clawhub.ai (para descubrir más skills)
- **Comunidad**: https://discord.com/invite/clawd
- **GitHub**: https://github.com/openclaw/openclaw

---

## 📊 Stats

| Categoría | Skills |
|-----------|--------|
| Búsqueda y Web | 3 |
| Programación | 6 |
| Productividad | 6 |
| Seguridad | 2 |
| Marketing | 3 |
| Reuniones | 2 |
| **Total** | **22** |

---

*Última actualización: Mayo 2026*
