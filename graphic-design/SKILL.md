---
name: Graphic Design Pro
slug: graphic-design-pro
version: 2.0.0
homepage: https://clawic.com/skills/graphic-design-pro
description: "Diseño UI/UX profesional inspirado en Claude Design: prototipos rápidos, sistemas de diseño, componentes, landing pages y pitch decks."
changelog: "Actualizado con capacidades de Claude Design - Ahora soporta prototipado rápido, sistemas de diseño, componentes UI, y optimización de landing pages."
metadata: {"clawdbot":{"emoji":"🎨","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/graphic-design-pro/"]}}
---

## When to Use

Usa este skill cuando:
- Necesitas diseñar o rediseñar landing pages
- Quieres crear prototipos UI/UX rápidos
- Necesitas un sistema de diseño consistente
- Para optimizar landing pages existentes
- Crear componentes UI reutilizables
- Diseñar pitch decks o one-pagers
- Mejorar conversión con diseño estratégico

**NO uses** para:
- Diseño de logos complejos (requiere herramientas especializadas)
- Ilustración artística detallada
- Diseño de impresión con CMYK/bleeds

## Claude Design Capabilities

### 🚀 Lo que puedo hacer (inspirado en Claude Design):

1. **Idea → Primer diseño en segundos**
   - Describes lo que necesitas → creo diseño estructurado
   - Aplico colores, tipografía y componentes consistentes
   - Respeto convenciones de UX para el tipo de artifact

2. **Refinamiento conversacional**
   - "Haz el hero más minimalista"
   - "Mueve el formulario a la derecha"
   - "Aumenta el espacio blanco en todas las secciones"
   - "Aplica este estilo de header en todas partes"

3. **Sistema de diseño integrado**
   - Extraigo colores, tipografía, spacing de tu marca
   - Creo componentes reutilizables (botones, cards, nav)
   - Mantengo consistencia en todos los diseños

4. **Optimización para conversión**
   - CTAs claros y visibles
   - Jerarquía visual que guía al usuario
   - Espaciado que mejora legibilidad
   - Contraste WCAG compliant

## Architecture

Memoria vive en `~/graphic-design-pro/`.

```
~/graphic-design-pro/
├── memory.md           # Sistemas de diseño activos, proyectos
├── design-systems/     # Sistemas de diseño por marca/proyecto
│   ├── colors.md       # Paletas de colores
│   ├── typography.md   # Escalas tipográficas
│   ├── components.md   # Componentes UI
│   └── spacing.md      # Sistema de spacing
├── projects/           # Proyectos de diseño
└── templates/          # Templates reutilizables
```

## Core Workflows

### Workflow 1: Landing Page Completa

**Input:** Descripción del negocio/producto

**Output:** Landing page completa con:
- Hero section con CTA claro
- Features/Beneficios
- Prueba social (testimonios, logos)
- CTA secundarios
- Footer completo

**Estructura típica:**
```
┌─────────────────────────────────┐
│  NAV: Logo + Links + CTA        │
├─────────────────────────────────┤
│  HERO:                          │
│  - Título impactante            │
│  - Subtítulo explicativo        │
│  - 2 CTAs (primario/secundario) │
│  - Imagen/Ilustración           │
├─────────────────────────────────┤
│  SOCIAL PROOF:                  │
│  - Logos de empresas            │
│  - Stats/métricas               │
├─────────────────────────────────┤
│  FEATURES (3-6 cards):          │
│  - Icono + Título + Descripción │
├─────────────────────────────────┤
│  TESTIMONIALS:                  │
│  - Quotes de clientes           │
├─────────────────────────────────┤
│  CTA FINAL:                     │
│  - Último llamado a la acción   │
├─────────────────────────────────┤
│  FOOTER:                        │
│  - Links + Redes + Copyright    │
└─────────────────────────────────┘
```

### Workflow 2: Optimización de Landing Existente

**Input:** URL o código de landing actual

**Análisis:**
1. ✅ Jerarquía visual
2. ✅ Contraste y accesibilidad
3. ✅ Espaciado y respiración
4. ✅ CTAs y conversión
5. ✅ Consistencia de marca

**Output:**
- Lista de mejoras prioritarias
- Código optimizado
- Antes/Después comparativo

### Workflow 3: Sistema de Diseño

**Input:** Sitios web, logos, o descripciones de marca

**Output:**
```markdown
## Sistema de Diseño: [Marca]

### Colores
- Primary: #2563eb (Blue 600)
- Secondary: #7c3aed (Violet 600)
- Accent: #10b981 (Emerald 500)
- Background: #ffffff
- Surface: #f8fafc
- Text: #0f172a

### Tipografía
- Headings: Inter (600, 700)
- Body: Inter (400, 500)
- Scale: 48px, 36px, 24px, 16px, 14px

### Spacing
- System: 4px base (4, 8, 12, 16, 24, 32, 48, 64)

### Componentes
- Buttons: Primary, Secondary, Outline
- Cards: Feature, Testimonial, Pricing
- Inputs: Text, Textarea, Select
- Navigation: Header, Footer, Mobile
```

### Workflow 4: Componentes UI

**Input:** Tipo de componente necesario

**Output:** Componente React/Tailwind listo para usar

**Ejemplo - Button:**
```jsx
export function Button({ 
  variant = 'primary', 
  size = 'md', 
  children,
  onClick 
}) {
  const base = 'inline-flex items-center justify-center font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2';
  
  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
    secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
    outline: 'border-2 border-blue-600 text-blue-600 hover:bg-blue-50 focus:ring-blue-500',
  };
  
  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };
  
  return (
    <button
      className={`${base} ${variants[variant]} ${sizes[size]}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

## Design Principles

### 1. Jerarquía Visual Clara
- Títulos > Subtítulos > Body
- CTAs destacan sobre el resto
- Espacio blanco guía la atención

### 2. Contraste y Accesibilidad
- Texto sobre fondo: mínimo 4.5:1 (WCAG AA)
- CTAs con contraste alto
- No depender solo del color

### 3. Espaciado Consistente
- Sistema de 4px (4, 8, 12, 16, 24, 32, 48, 64)
- Espacio blanco = lujo y claridad
- Padding generoso en containers

### 4. Tipografía Legible
- Máximo 2-3 fuentes
- Line-height: 1.5-1.7 para body
- Line-length: 60-80 caracteres

### 5. Consistencia de Marca
- Mismos colores en toda la página
- Mismos estilos de botones
- Mismos bordes y sombras

## Landing Page Optimization

### ✅ Checklist de Optimización

**Hero Section:**
- [ ] Título claro en < 10 palabras
- [ ] Subtítulo explica el valor
- [ ] 1-2 CTAs visibles
- [ ] Imagen relevante o ilustración
- [ ] Carga < 3 segundos

**Features:**
- [ ] 3-6 features máximo
- [ ] Icono + título + descripción corta
- [ ] Beneficios, no solo características
- [ ] Ordenados por importancia

**Prueba Social:**
- [ ] Testimonios reales con foto
- [ ] Logos de empresas (si aplica)
- [ ] Stats/métricas concretas
- [ ] Casos de éxito

**CTAs:**
- [ ] Color contrastante
- [ ] Texto de acción claro ("Comienza gratis", no "Enviar")
- [ ] Múltiples CTAs en página larga
- [ ] Above the fold + al final

**Mobile:**
- [ ] Responsive probado
- [ ] Touch targets > 44px
- [ ] Texto legible sin zoom
- [ ] Forms optimizados

### 🎨 Colores que Convierten

| Color | Uso | Psicología |
|-------|-----|------------|
| Azul (#2563eb) | Primary CTA | Confianza, profesional |
| Verde (#10b981) | Success, Pricing | Crecimiento, positivo |
| Naranja (#f97316) | Secondary CTA | Energía, urgencia |
| Rojo (#ef4444) | Error, Urgencia | Atención, acción |
| Violeta (#7c3aed) | Premium, Creative | Creatividad, lujo |

### 📐 Layouts que Funcionan

**Landing Clásica:**
```
Hero → Features → Social Proof → CTA → Footer
```

**Landing con Pricing:**
```
Hero → Features → Pricing → Testimonials → FAQ → CTA → Footer
```

**Landing de Producto:**
```
Hero → Problem → Solution → Features → Demo → Pricing → CTA → Footer
```

## Adapt to the User

- **Para founders:** Enfócate en conversión, claridad, time-to-market
- **Para designers:** Usa terminología técnica, sistemas de diseño, componentes
- **Para devs:** Código limpio, Tailwind, React, reutilizable
- **Para marketers:** Copy + diseño, A/B testing, métricas de conversión

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Demasiados colores | Diluye la marca, confunde | 1 primary, 1 secondary, 1 accent |
| CTAs genéricos | "Enviar" no motiva | Usa acción + beneficio |
| Sin espacio blanco | Saturado, difícil de leer | Padding generoso, respira |
| Tipografía inconsistente | Amateur, difícil de leer | Máx 2-3 fuentes, escala clara |
| Ignorar mobile | 50%+ del tráfico es mobile | Mobile-first siempre |
| Sin prueba social | No genera confianza | Testimonios, logos, stats |

## Scope

Este skill SÓLO:
- Crea y optimiza landing pages
- Diseña componentes UI reutilizables
- Crea sistemas de diseño consistentes
- Optimiza para conversión y accesibilidad
- Genera código React/Tailwind listo para usar

Este skill NUNCA:
- Diseña logos complejos (usa herramientas especializadas)
- Crea ilustraciones artísticas detalladas
- Reemplaza diseñadores profesionales para proyectos críticos
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/graphic-design-pro/`:

- `memory.md` - Sistemas de diseño activos, proyectos en curso
- `design-systems/` - Sistemas de diseño organizados por marca
- `projects/` - Proyectos de diseño completados
- `templates/` - Templates reutilizables de landing pages y componentes

## Security & Privacy

- No uses datos sensibles de clientes en ejemplos
- Respeta copyrights de diseños existentes
- Inspírate, no copies diseños protegidos
- Verifica licencias de fuentes e iconos

## Related Skills

- `refero-styles` - Extrae estilos de sitios existentes
- `quick-prototype` - Prototipa ideas rápidamente
- `programming` - Implementa los diseños en código
- `seo` - Optimiza para search engines
- `content-marketing` - Alinea diseño con estrategia de contenido

## Feedback

- Si fue útil: `clawhub star graphic-design-pro`
- Mantente actualizado: `clawhub sync`

---

*Skill actualizado con capacidades inspiradas en Claude Design - Abril 2026*
