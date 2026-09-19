---
name: Chat to PRD
slug: chat-to-prd
version: 1.0.0
homepage: https://github.com/AvilaCarlosDev/openclaw-skills/tree/main/chat-to-prd
description: "Sintetiza la conversación actual en un PRD y lo envía como GitHub issue. Sin entrevista, solo sintetiza lo discutido."
changelog: "Skill inicial para convertir conversaciones en PRDs ejecutables."
metadata: {"clawdbot":{"emoji":"📄","requires":{"bins":["gh"]},"os":["linux","darwin","win32"],"configPaths":["~/chat-to-prd/"]}}
---

## When to Use

Usa este skill cuando:
- Has tenido una conversación/discusión sobre un feature
- Necesitas documentar lo acordado en un PRD formal
- Quieres convertir la conversación en un issue ejecutable
- Para alinear al equipo sobre lo que se va a construir

**NO uses** para:
- Conversaciones tempranas sin conclusiones
- Cuando necesitas más descubrimiento (usa `grill-with-docs`)
- Bugs simples (usa `issue-triage` directo)

## Architecture

Memoria vive en `~/chat-to-prd/`.

```
~/chat-to-prd/
├── memory.md        # Configuración, templates
└── prds/            # PRDs generados
```

## PRD Structure

### Template Base

```markdown
# PRD: [Nombre del Feature]

## 📋 Resumen Ejecutivo

[2-3 oraciones describiendo qué se construye y por qué]

## 🎯 Problema a Resolver

[¿Qué problema tiene el usuario? ¿Por qué existe este feature?]

## 👥 Usuarios Objetivo

- [Tipo de usuario 1]: [Cómo se beneficia]
- [Tipo de usuario 2]: [Cómo se beneficia]

## ✅ Criterios de Éxito

| Métrica | Actual | Target | Timeline |
|---------|--------|--------|----------|
| [Métrica 1] | X% | Y% | [fecha] |
| [Métrica 2] | X | Y | [fecha] |

## 📐 Requisitos Funcionales

### RF-001: [Nombre del requisito]
**Descripción:** [Qué debe hacer el sistema]
**Prioridad:** Must-have | Should-have | Could-have
**Criterios de aceptación:**
- [ ] Criterio 1
- [ ] Criterio 2

### RF-002: [Nombre del requisito]
...

## 🚫 Fuera de Scope

- [Lo que NO se va a construir en esta iteración]

## 🎨 Diseño y UX

[Links a Figma, mockups, o descripción de la experiencia]

## 🔗 Dependencias

- [ ] Dependencia técnica 1
- [ ] Dependencia de equipo 2

## 📊 Métricas y Analytics

[Qué se va a trackear y cómo]

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| [Riesgo 1] | Alta | Medio | [Mitigación] |

## 📅 Timeline Propuesto

| Fase | Duración | Entregable |
|------|----------|------------|
| Desarrollo | X semanas | [Qué] |
| Testing | X días | [Qué] |
| Launch | [fecha] | [Qué] |

## 📝 Notas Adicionales

[Contexto adicional, decisiones, tradeoffs]
```

## Synthesis Workflow

### 🔍 PASO 1: EXTRAER DE LA CONVERSACIÓN

**Analiza la conversación y extrae:**

1. **Objetivo principal:**
   - "¿Qué estamos tratando de construir?"
   
2. **Problema:**
   - "¿Qué dolor tiene el usuario?"
   
3. **Usuarios:**
   - "¿Para quién es esto?"
   
4. **Requisitos mencionados:**
   - Lista todo lo discutido como "debe hacer X"
   
5. **Decisiones tomadas:**
   - "Acordamos que Y sería la solución"
   
6. **Preocupaciones/riesgos:**
   - "Nos preocupa que Z pueda fallar"

### 📝 PASO 2: SINTETIZAR

**Consolida la información:**

```
De: "El usuario necesita poder guardar sus favoritos"
A:  "RF-001: Sistema de favoritos - El usuario puede guardar items en una lista personal"

De: "Pero que no sea público al inicio"
A:  "RF-002: Privacidad de favoritos - Por defecto, las listas son privadas"

De: "Queremos lanzar en 2 semanas"
A:  "Timeline: 2 semanas para MVP"
```

### 🏷️ PASO 3: PRIORIZAR (MoSCoW)

**Clasifica cada requisito:**

- **Must-have:** Crítico, sin esto no hay feature
- **Should-have:** Importante, pero se puede lanzar sin esto
- **Could-have:** Nice to have, si alcanza el tiempo
- **Won't-have:** Explícitamente fuera de scope

### 📤 PASO 4: CREAR GITHUB ISSUE

**Título del issue:**
```
📄 PRD: [Nombre del Feature]
```

**Cuerpo del issue:**
- Usa el template de PRD completo
- Incluye link a la conversación original (si aplica)
- Label: `prd`, `feature`, prioridad

**Comando gh:**
```bash
gh issue create --title "📄 PRD: Nombre del Feature" --body-file prd.md --label prd,feature,P1-high
```

## Quality Checklist

Antes de publicar el PRD, verifica:

- [ ] El problema está claramente definido
- [ ] Los usuarios objetivo están identificados
- [ ] Los criterios de éxito son medibles
- [ ] Los requisitos son testeables
- [ ] El scope está delimitado (qué NO incluye)
- [ ] Las dependencias están identificadas
- [ ] Los riesgos están documentados
- [ ] El timeline es realista

## Adapt to the User

- **Para startups:** PRD ligero, enfocado en MVP, métricas de growth
- **Para empresas:** PRD completo, aprobaciones, compliance
- **Para equipos ágiles:** PRD vivo, actualizable por sprint
- **Para equipos distribuidos:** PRD detallado, asíncrono-first

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| PRD demasiado largo | Nadie lo lee completo | Mantén < 2 páginas, usa anexos |
| Requisitos vagos | No se sabe cuándo está hecho | Hazlos observables y testeables |
| Sin criterios de éxito | No se mide el impacto | Define métricas antes de build |
| Ignorar riesgos | Sorpresas en desarrollo | Documenta riesgos explícitamente |
| PRD como contrato | No se puede adaptar | PRD es vivo, actualiza según aprendizaje |

## Scope

Este skill SÓLO:
- Sintetiza conversaciones en PRDs estructurados
- Identifica requisitos, usuarios, criterios de éxito
- Crea GitHub issues con PRDs adjuntos
- Documenta decisiones y tradeoffs

Este skill NUNCA:
- Inventa requisitos no discutidos
- Reemplaza descubrimiento necesario (→ `grill-with-docs`)
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/chat-to-prd/`:

- `memory.md` - Configuración, templates preferidos
- `prds/` - PRDs generados, versionados

## Related Skills

- `grill-with-docs` - Para descubrimiento antes del PRD
- `plan-to-issues` - Para convertir PRD en issues ejecutables
- `to-issues` - Similar, más enfocado en slicing

## Feedback

- Si fue útil: `clawhub star chat-to-prd`
- Mantente actualizado: `clawhub sync`
