# 🎨 Skill: Diseño Profesional (Refero Style)

**Comando:** `/diseno-profesional`  
**Categoría:** Diseño UI/UX  
**Dificultad:** Intermedio  
**Tiempo:** 15-30 min por página/componente

---

## 📖 Descripción

Aplica principios de **diseño profesional** basados en [Refero.design](https://styles.refero.design) para crear webs/apps con nivel visual superior.

Este skill extrae patrones de diseño de productos reales y los aplica sistemáticamente: colores, tipografía, spacing, componentes y jerarquía visual.

---

## 🎯 Cuándo Usar

✅ **Usar cuando:**
- Vas a crear una landing page nueva
- Vas a rediseñar un componente existente
- El diseño se ve "amateur" o desactualizado
- Quieres nivel visual de startup/profesional

❌ **NO usar cuando:**
- Es un prototipo interno rápido
- El cliente ya tiene diseño aprobado
- Es solo funcionalidad (sin UI visible)

---

## 📋 Principios de Diseño (Refero Style)

### **1. JERARQUÍA VISUAL**

```markdown
✅ CORRECTO:
- Título principal: text-6xl a text-8xl (48-64px)
- Subtítulo: text-2xl a text-4xl (24-36px)
- Body: text-base a text-lg (16-18px)
- Secondary: text-sm (14px)

❌ INCORRECTO:
- Todo del mismo tamaño
- Títulos muy pequeños
- Sin diferenciación clara
```

### **2. ESPACIADO (WHITESPACE)**

```markdown
✅ CORRECTO:
- Secciones: py-24 (96px padding vertical)
- Contenedores: px-6 lg:px-12 (24px-48px horizontal)
- Entre elementos: gap-6 a gap-8 (24px-32px)
- Dentro de cards: p-6 a p-8 (24px-32px)

❌ INCORRECTO:
- Todo muy junto (py-4, gap-2)
- Sin aire entre secciones
- Contenido apretado
```

### **3. COLORES**

```markdown
✅ PALETA PROFESIONAL:
- Primary: 1 color principal (ej: azul-600, verde-500)
- Secondary: 1 color complementario (ej: naranja-500)
- Neutral: grays para texto (gray-900, gray-600, gray-400)
- Background: blanco o gray-50/gray-100

REGLA 60-30-10:
- 60% color dominante (background, neutro)
- 30% color secundario (primary)
- 10% color de acento (botones, CTAs)

✅ GRADIENTES MODERNOS:
- bg-gradient-to-r from-[color1] via-[color2] to-[color3]
- text-transparent bg-clip-text bg-gradient-to-r
- opacity-80 a opacity-90 para overlays

❌ INCORRECTO:
- Demasiados colores (5+)
- Colores muy saturados juntos
- Sin contraste suficiente
```

### **4. TIPOGRAFÍA**

```markdown
✅ COMBINACIONES PROFESIONALES:
- Heading: Font serif o display (Playfair, Merriweather)
- Body: Sans-serif (Inter, Roboto, System UI)

- Heading: Font bold/black (font-bold, font-black)
- Body: Font normal/medium (font-normal, font-medium)

✅ TAMAÑOS:
- Hero: text-6xl lg:text-8xl (48-64px)
- Section: text-4xl lg:text-5xl (36-48px)
- Card title: text-2xl (24px)
- Body: text-base lg:text-lg (16-18px)

❌ INCORRECTO:
- Todo font-bold (sin contraste)
- Mismo tamaño para todo
- Fuentes decorativas para body
```

### **5. COMPONENTES**

```markdown
✅ BOTONES MODERNOS:
- Primary: bg-gradient-to-r, rounded-xl/rounded-2xl, shadow-lg
- Hover: transform hover:scale-105, brightness-110
- Padding: px-8 py-4 (generoso)
- Shadow: shadow-lg shadow-[color]/30

✅ CARDS:
- Background: bg-white
- Border radius: rounded-2xl o rounded-3xl
- Shadow: shadow-xl o shadow-2xl
- Hover: hover:shadow-2xl hover:-translate-y-2
- Padding: p-6 a p-8

✅ HERO SECTIONS:
- Altura: min-h-screen o h-[800px]
- Background: gradient + overlay o imagen full
- Contenido: max-w-4xl mx-auto (centrado)
- CTAs: 2 botones (primary + secondary)

✅ NAVIGATION:
- Sticky: sticky top-0 z-50
- Background: bg-white/90 backdrop-blur-md
- Padding: py-6 (generoso)
- Mobile: hamburger menu

❌ INCORRECTO:
- Botones pequeños (px-4 py-2)
- Cards sin shadow
- Hero muy corto
- Nav sin backdrop blur
```

### **6. IMÁGENES**

```markdown
✅ CALIDAD PROFESIONAL:
- Unsplash directo: images.unsplash.com/photo-[ID]?w=[width]&q=80
- Relación de aspecto consistente (aspect-[4/3], aspect-square)
- Border radius: rounded-2xl o rounded-3xl
- Overlay: bg-gradient-to-t para texto sobre imagen

✅ LAZY LOADING:
- loading="lazy" en imágenes below the fold
- Imágenes hero: eager (carga inmediata)

❌ INCORRECTO:
- Imágenes pixeladas
- Múltiples aspect ratios
- Sin optimización
```

### **7. ANIMACIONES**

```markdown
✅ SUTILES Y PROFESIONALES:
- Transitions: transition-all duration-300/500/700
- Hover: hover:scale-105, hover:shadow-2xl
- Fade-in: opacity-0 → opacity-100 con transition
- Scroll animations: Intersection Observer

❌ EXCESIVAS:
- Demasiado movimiento
- Animaciones lentas (>1s)
- Efectos distractivos
```

### **8. RESPONSIVE**

```markdown
✅ MOBILE-FIRST:
- Base: mobile (sin breakpoint)
- Tablet: md: (768px)
- Desktop: lg: (1024px)
- Large: xl: (1280px), 2xl: (1536px)

✅ CONTAINERS:
- max-w-[1600px] a max-w-[1800px] mx-auto
- px-6 lg:px-12 (padding responsive)

✅ GRID/FLEX:
- Mobile: grid-cols-1
- Tablet: md:grid-cols-2
- Desktop: lg:grid-cols-3, lg:grid-cols-4

❌ INCORRECTO:
- Solo desktop
- Textos muy grandes en mobile
- Sin touch targets (min 44px)
```

---

## 📋 Checklist de Diseño (Antes de Entregar)

```markdown
## JERARQUÍA
[ ] Títulos claramente diferenciados (tamaño + peso)
[ ] Body legible (16px mínimo, line-height 1.5+)
[ ] Secondary text más pequeño/gris

## ESPACIADO
[ ] Secciones con py-24 (96px)
[ ] Contenedores con px-6 lg:px-12
[ ] Elementos con gap-6 mínimo
[ ] Cards con p-6 mínimo

## COLORES
[ ] Máximo 3 colores principales
[ ] Contraste suficiente (WCAG AA)
[ ] Gradientes modernos (no planos)
[ ] Backgrounds con variación sutil

## TIPOGRAFÍA
[ ] 2 fuentes máximo (heading + body)
[ ] Heading font-bold o black
[ ] Body font-normal o medium
[ ] Tamaños responsive (text-xl lg:text-2xl)

## COMPONENTES
[ ] Botones con rounded-xl y shadow-lg
[ ] Cards con rounded-2xl y hover effects
[ ] Hero con altura suficiente (min-h-screen)
[ ] Nav sticky con backdrop blur

## IMÁGENES
[ ] Unsplash/Pexels de calidad (q=80)
[ ] Aspect ratios consistentes
[ ] Lazy loading donde aplica
[ ] Overlays para legibilidad

## ANIMACIONES
[ ] Transitions suaves (300-500ms)
[ ] Hover effects en botones/cards
[ ] Sin animaciones distractivas

## RESPONSIVE
[ ] Mobile-first (base sin breakpoint)
[ ] Grid/flex responsive
[ ] Touch targets > 44px
[ ] Textos legibles en mobile
```

---

## 💡 Ejemplo de Uso

### Usuario:
```
/diseno-profesional

Voy a crear una landing para una ferretería.
```

### Agente:
```markdown
¡Perfecto! Aplicando principios de diseño profesional...

## 🎨 PALETA DE COLORES:

**Primary:** Naranja (típico ferretería)
- bg-orange-500, text-orange-600

**Secondary:** Azul (confianza, profesional)
- bg-blue-600, text-blue-900

**Neutral:** Grays
- text-gray-900 (heading)
- text-gray-600 (body)
- text-gray-400 (secondary)

**Background:**
- bg-gray-50 (secciones alternas)
- bg-white (cards)

## 📏 ESPACIADO:

- Hero: min-h-screen, py-24
- Secciones: py-24
- Contenedor: max-w-[1800px] mx-auto, px-6 lg:px-12
- Cards: p-8, gap-8

## 🔤 TIPOGRAFÍA:

- Heading: font-black, text-6xl lg:text-7xl
- Subheading: font-bold, text-2xl lg:text-3xl
- Body: font-normal, text-base lg:text-lg

## 🧩 COMPONENTES:

**Hero:**
- Background: gradient naranja + overlay
- Título: text-7xl lg:text-8xl font-black
- 2 CTAs: primary (naranja) + secondary (blanco)
- Stats: 3 columnas con números grandes

**Cards de Productos:**
- rounded-2xl, shadow-xl
- hover:shadow-2xl hover:-translate-y-2
- Aspect ratio: [4/3] para imágenes
- Precio: text-4xl font-black text-orange-600

**Nav:**
- sticky top-0 z-50
- bg-white/90 backdrop-blur-md
- py-6, gap-10

## 📱 RESPONSIVE:

- Mobile: grid-cols-1
- Tablet: md:grid-cols-2
- Desktop: lg:grid-cols-4

¿Procedo a crear el código con estos principios?
```

---

## 📊 Antes vs Después

### ANTES (Sin skill):
```jsx
// Diseño amateur
<div className="p-4">
  <h1 className="text-2xl font-bold">Ferretería López</h1>
  <p>Productos de calidad</p>
  <button className="bg-blue-500 px-4 py-2">Comprar</button>
</div>
```

### DESPUÉS (Con skill):
```jsx
// Diseño profesional
<div className="min-h-screen bg-gradient-to-br from-orange-500 to-orange-600">
  <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md">
    <div className="max-w-[1800px] mx-auto px-6 lg:px-12 py-6">
      {/* Nav content */}
    </div>
  </nav>

  <section className="py-24 px-6 lg:px-12">
    <div className="max-w-[1800px] mx-auto">
      <h1 className="text-7xl lg:text-8xl font-black text-white mb-6">
        TODO PARA TU<br/>
        <span className="text-yellow-300">CONSTRUCCIÓN</span>
      </h1>
      <p className="text-xl text-white/90 mb-10 max-w-2xl">
        Herramientas, materiales y asesoría profesional.
      </p>
      <div className="flex gap-4">
        <button className="bg-white hover:bg-gray-100 text-orange-600 
                          px-10 py-5 rounded-xl font-bold text-lg 
                          transition transform hover:scale-105 shadow-xl">
          Ver Catálogo
        </button>
      </div>
    </div>
  </section>
</div>
```

---

## ⚠️ Errores Comunes

| Error | Cómo Evitarlo |
|-------|---------------|
| Spacing muy pequeño | Usar **py-24** mínimo para secciones |
| Botones pequeños | **px-8 py-4** mínimo, rounded-xl |
| Sin jerarquía | Títulos **text-6xl+**, body **text-base** |
| Demasiados colores | Máximo **3 colores** principales |
| Imágenes pixeladas | Unsplash con **q=80**, w=1200+ |
| Sin responsive | **Mobile-first**, breakpoints md/lg |
| Cards sin shadow | **shadow-xl** mínimo, hover effects |

---

## 🎓 Principios Subyacentes

- **Refero.design** - Design systems de productos reales
- **Laws of UX** - Leyes de experiencia de usuario
- **Material Design 3** - Sistema de diseño de Google
- **Tailwind UI** - Patrones de componentes profesionales

---

## 🔗 Recursos

- [Refero Styles](https://styles.refero.design/)
- [Laws of UX](https://lawsofux.com)
- [Material Design](https://m3.material.io)
- [Tailwind UI](https://tailwindui.com)

---

*Skill creado para OpenClaw en Español - Hecho con 💚 por @avilacarlosdev*
