---
name: Refero Styles
slug: refero-styles
version: 1.0.0
homepage: https://clawic.com/skills/refero-styles
description: "Extrae y analiza estilos de diseño web: colores, tipografía, spacing, componentes y genera DESIGN.md para agentes."
changelog: "Skill inicial para análisis de estilos de diseño web inspirado en Refero Styles."
metadata: {"clawdbot":{"emoji":"🎨","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/refero-styles/"]}}
---

## When to Use

Usa este skill cuando:
- Quieres analizar el diseño de un sitio web existente
- Necesitas extraer colores, tipografía y componentes de una URL
- Buscas inspiración de diseño para un proyecto nuevo
- Quieres documentar el sistema de diseño de un sitio
- Para crear un DESIGN.md que un agente pueda usar

**NO uses** para:
- Sitios que no tienen permiso para análisis
- Copiar diseños protegidos por copyright
- Ingeniería inversa de diseños patentados

## Architecture

Memoria vive en `~/refero-styles/`.

```
~/refero-styles/
├── memory.md        # Análisis activos, proyectos
├── analyses/        # Análisis completos por URL
└── templates/       # Templates de DESIGN.md
```

## Core Workflow

### 🔍 FASE 1: ANALIZAR URL

**Objetivo:** Extraer todos los elementos de diseño de una URL.

**Elementos a extraer:**

#### 1. Colores (Color Palette)

```markdown
## 🎨 Colores

### Primarios
- `--color-primary`: #2563eb (Blue 600)
- `--color-primary-dark`: #1d4ed8 (Blue 700)
- `--color-primary-light`: #3b82f6 (Blue 500)

### Secundarios
- `--color-secondary`: #7c3aed (Violet 600)

### Neutros
- `--color-background`: #ffffff
- `--color-surface`: #f8fafc
- `--color-text`: #0f172a
- `--color-text-muted`: #64748b

### Acentos
- `--color-accent`: #10b981 (Emerald 500)
- `--color-error`: #ef4444 (Red 500)
- `--color-warning`: #f59e0b (Amber 500)
```

**Técnica de extracción:**
- Buscar variables CSS (`--color-*`, `var(--*)`)
- Extraer de Tailwind (`bg-blue-600`, `text-gray-900`)
- Analizar estilos inline (`style="color: #..."`)
- Revisar CSS custom properties

#### 2. Tipografía (Typography)

```markdown
## 🔤 Tipografía

### Fuentes
- **Principal:** Inter (Google Fonts)
  - Weights: 400, 500, 600, 700
  - URL: https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700

- **Display:** Playfair Display
  - Weights: 600, 700
  - Uso: Títulos y headings

### Escala Tipográfica
| Elemento | Size | Weight | Line-height |
|----------|------|--------|-------------|
| H1 | 3rem (48px) | 700 | 1.2 |
| H2 | 2.25rem (36px) | 600 | 1.3 |
| H3 | 1.5rem (24px) | 600 | 1.4 |
| Body | 1rem (16px) | 400 | 1.6 |
| Small | 0.875rem (14px) | 400 | 1.5 |
```

**Técnica de extracción:**
- Analizar `<link>` de Google Fonts
- Extraer `font-family` de CSS
- Buscar `font-size`, `font-weight`, `line-height`
- Identificar sistema de escala (rem, px, em)

#### 3. Spacing (Espaciado)

```markdown
## 📏 Spacing

### Sistema de Spacing (Tailwind-like)
| Token | Valor | Uso |
|-------|-------|-----|
| `--space-1` | 0.25rem (4px) | Micro spacing |
| `--space-2` | 0.5rem (8px) | Gap pequeño |
| `--space-4` | 1rem (16px) | Padding estándar |
| `--space-6` | 1.5rem (24px) | Secciones |
| `--space-8` | 2rem (32px) | Márgenes grandes |
| `--space-12` | 3rem (48px) | Hero sections |
| `--space-16` | 4rem (64px) | Secciones principales |

### Container Widths
- `--container-sm`: 640px
- `--container-md`: 768px
- `--container-lg`: 1024px
- `--container-xl`: 1280px
```

#### 4. Componentes (Components)

```markdown
## 🧩 Componentes

### Botones

#### Primary Button
```css
.btn-primary {
  background: var(--color-primary);
  color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
}
.btn-primary:hover {
  background: var(--color-primary-dark);
  transform: translateY(-1px);
}
```

#### Secondary Button
```css
.btn-secondary {
  background: transparent;
  color: var(--color-primary);
  border: 1px solid var(--color-primary);
  padding: var(--space-3) var(--space-6);
  border-radius: 0.375rem;
}
```

### Cards

#### Feature Card
```css
.feature-card {
  background: var(--color-surface);
  padding: var(--space-6);
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  transition: transform 0.2s;
}
.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
```

### Navigation
- **Tipo:** Sticky header
- **Height:** 64px
- **Background:** Blur backdrop-filter
- **Logo:** Left-aligned
- **Nav Links:** Centered
- **CTA:** Right-aligned
```

#### 5. Layout (Estructura)

```markdown
## 📐 Layout

### Grid System
- **Columns:** 12
- **Gutter:** 1.5rem (24px)
- **Margin:** 1rem (16px) mobile, 2rem (32px) desktop

### Breakpoints
| Nombre | Min-width | Uso |
|--------|-----------|-----|
| sm | 640px | Mobile landscape |
| md | 768px | Tablets |
| lg | 1024px | Laptops |
| xl | 1280px | Desktops |
| 2xl | 1536px | Large screens |

### Secciones Típicas
1. **Hero** - Full viewport height, centered content
2. **Features** - Grid 3 columns, cards
3. **Testimonials** - Grid 2 columns, quotes
4. **CTA** - Full width, background color
5. **Footer** - 4 columns, links + social
```

### 📝 FASE 2: GENERAR DESIGN.md

**Template de DESIGN.md:**

```markdown
# DESIGN.md - [Nombre del Sitio]

**URL:** https://ejemplo.com
**Análisis:** YYYY-MM-DD
**Por:** [Tu nombre/agente]

---

## 🎨 Colores

[Colores extraídos]

## 🔤 Tipografía

[Fuentes y escala]

## 📏 Spacing

[Sistema de spacing]

## 🧩 Componentes

[Componentes principales]

## 📐 Layout

[Layout y breakpoints]

## 💡 Notas de Diseño

- **Mood:** Modern, clean, professional
- **Estilo:** Minimalista con acentos de color
- **Accesibilidad:** WCAG AA (contraste verificado)
- **Responsive:** Mobile-first

## 🚀 Cómo Usar Este DESIGN.md

1. Copia las variables CSS a tu proyecto
2. Importa las fuentes de Google Fonts
3. Usa los componentes como referencia
4. Adapta el spacing a tu sistema

---

*Generado por OpenClaw - Refero Styles Skill*
```

### ✅ FASE 3: APLICAR AL PROYECTO

**Opciones de implementación:**

#### Opción A: Variables CSS Globales

```css
/* styles/design-tokens.css */
:root {
  /* Colores */
  --color-primary: #2563eb;
  --color-secondary: #7c3aed;
  
  /* Tipografía */
  --font-main: 'Inter', sans-serif;
  --font-display: 'Playfair Display', serif;
  
  /* Spacing */
  --space-4: 1rem;
  --space-6: 1.5rem;
}
```

#### Opción B: Tailwind Config

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#2563eb',
        secondary: '#7c3aed',
      },
      fontFamily: {
        main: ['Inter', 'sans-serif'],
        display: ['Playfair Display', 'serif'],
      },
      spacing: {
        '4': '1rem',
        '6': '1.5rem',
      }
    }
  }
}
```

#### Opción C: Componentes React

```jsx
// components/ui/Button.jsx
export function Button({ variant = 'primary', children }) {
  const baseStyles = 'px-6 py-3 rounded-md font-medium transition-all';
  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'border border-blue-600 text-blue-600 hover:bg-blue-50'
  };
  
  return (
    <button className={`${baseStyles} ${variants[variant]}`}>
      {children}
    </button>
  );
}
```

## Adapt to the User

- **Para designers:** Enfócate en colores, tipografía, principios de diseño
- **Para devs:** Enfócate en variables, componentes reutilizables, código
- **Para founders:** Enfócate en mood, branding, diferenciadores
- **Para equipos:** Documenta todo, usa DESIGN.md como fuente de verdad

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Copiar exacto | Problemas de copyright | Inspírate, no copies |
| Ignorar contexto | No funciona para tu caso | Adapta a tu audiencia |
| Sobre-analizar | Parálisis por análisis | Extrae lo esencial, itera |
| Sin DESIGN.md | Conocimiento se pierde | Documenta siempre |
| Ignorar accesibilidad | Excluye usuarios | Verifica contraste WCAG |

## Scope

Este skill SÓLO:
- Analiza diseños de sitios web públicos
- Extrae colores, tipografía, spacing, componentes
- Genera DESIGN.md documentado
- Sugiere implementación

Este skill NUNCA:
- Copia diseños protegidos
- Ignora copyright o licencias
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/refero-styles/`:

- `memory.md` - Análisis activos, proyectos en curso
- `analyses/` - Análisis completos organizados por URL
- `templates/` - Templates de DESIGN.md reutilizables

## Security & Privacy

- **Solo analiza sitios públicos** - No accedas a áreas con login
- **Respeta copyright** - Usa como inspiración, no copies
- **No almacenes datos sensibles** - Solo tokens de diseño
- **Cita la fuente** - Menciona el sitio original

## Related Skills

- `graphic-design` - Para principios de diseño general
- `quick-prototype` - Para prototipar con el estilo extraído
- `programming` - Para implementar los componentes
- `seo` - Para optimizar el diseño para search engines

## Feedback

- Si fue útil: `clawhub star refero-styles`
- Mantente actualizado: `clawhub sync`
