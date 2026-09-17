# 📧 Skill: Pitch de Ventas

**Comando:** `/pitch`  
**Categoría:** Ventas  
**Dificultad:** Fácil  
**Tiempo:** 5-10 min por email

---

## 📖 Descripción

Genera emails de venta **personalizados** para ofrecer landing pages a negocios locales.

Este skill crea emails que NO parecen spam, sino que demuestran investigación genuina del negocio y ofrecen valor real.

---

## 🎯 Cuándo Usar

✅ **Usar cuando:**
- Vas a contactar un negocio por primera vez
- Tienes una landing demo lista para mostrar
- Quieres ofrecer tus servicios de forma profesional
- Necesitas seguir un patrón de ventas probado

❌ **NO usar cuando:**
- El cliente ya te conoce (usa email personalizado directo)
- Es un follow-up (usa `/seguimiento` en su lugar)
- Es una respuesta a una consulta inbound

---

## 📋 Instrucciones para el Agente

```markdown
# ROL: Eres un experto en ventas B2B para servicios web

# PROCESO:

1. **INVESTIGA el negocio** (pídeme esta info si no la tengo):
   - Nombre del negocio
   - Qué hacen/venden
   - Dónde los encontré (Instagram, Google, recomendación)
   - Nombre del dueño/encargado (si lo tengo)
   - URL de su red social o web actual

2. **IDENTIFICA el problema**:
   - ¿No tienen web propia?
   - ¿Su web es lenta/fea/no es responsive?
   - ¿Solo tienen redes sociales?
   - ¿No se encuentran en Google?

3. **PREPARA la demo**:
   - ¿Qué landing demo tengo lista para su nicho?
   - URL de la demo en Vercel
   - Características relevantes para SU negocio

4. **GENERA el email** con esta estructura:

---

**ASUNTO:** [Personalizado, menciona su negocio]

**SALUDO:** [Nombre si lo tengo, sino "Hola equipo de [Negocio]"]

**PÁRRAFO 1 - CONEXIÓN:**
- Dónde los encontré
- Qué me gustó de su negocio
- Por qué los contacto específicamente a ellos

**PÁRRAFO 2 - PROBLEMA:**
- Noté que [problema: no tienen web / web lenta / solo redes]
- Esto les está costando [consecuencia: clientes / ventas / visibilidad]

**PÁRRAFO 3 - SOLUCIÓN:**
- Creé una demo específicamente para negocios como el suyo
- URL de la demo
- Características clave (rápida, responsive, WhatsApp integrado)

**PÁRRAFO 4 - OFERTA:**
- Precio piloto (si aplica)
- Timeline de entrega
- Qué incluye

**CALL TO ACTION:**
- ¿Agendamos una llamada de 10 min?
- ¿Les envío más información?
- ¿Puedo mostrarles la demo en persona?

**FIRMA:**
- Mi nombre
- Mi portfolio
- Mi teléfono/WhatsApp

---

# TONO:

- ✅ Profesional pero cercano
- ✅ Sin jerga técnica excesiva
- ✅ Enfocado en BENEFICIOS, no características
- ✅ Corto (máximo 200 palabras)
- ✅ Personalizado (nada genérico)

# EVITAR:

- ❌ "Espero que esté bien" (muy genérico)
- ❌ "Soy el mejor desarrollador" (muy arrogante)
- ❌ "Oferta por tiempo limitado" (muy vendedor)
- ❌ Emails de 500+ palabras (muy largos)
- ❌ Jerga técnica (React, Vite, Tailwind, etc.)

# EJEMPLO DE EMAIL:

```
Asunto: 🚀 Una web profesional para [Nombre del Negocio]

Hola [Nombre],

Soy Carlos Ávila, desarrollador web aquí en [Ciudad].

Los encontré en [Instagram/Google] y me encantó [algo específico que me gustó]. 
Noté que no tienen página web propia, solo redes sociales.

Quería mostrarles algo que creé especialmente para negocios como el suyo:

👉 [URL de la demo]

Es una landing page moderna, rápida y optimizada para que más clientes 
los encuentren y contacten por WhatsApp.

¿Les gustaría que la personalice con sus fotos, colores y información real?

Precio piloto esta semana: $150-200 (normal $300+)

¿Agendamos una llamada de 10 minutos para mostrarles más detalles?

Saludos,
Carlos Ávila
📱 [Tu teléfono]
🌐 [Tu portfolio]
```
```

---

## 💡 Ejemplo de Uso

### Usuario:
```
/pitch

Quiero contactar a "Barbería El Capitán" en Punto Fijo.
Los encontré en Instagram: @barberiaelcapitan
El dueño se llama Roberto.
Tienen 5k followers pero no tienen web.
```

### Agente:
```markdown
Generando email pitch para Barbería El Capitán...

---

**ASUNTO:** 🚀 Una web profesional para Barbería El Capitán

**CUERPO:**

Hola Roberto,

Soy Carlos Ávila, desarrollador web aquí en Punto Fijo.

Los encontré en Instagram (@barberiaelcapitan) y me encantó cómo manejan 
los cortes clásicos y modernos. Noté que tienen 5k followers pero no 
tienen página web propia.

Quería mostrarles algo que creé especialmente para barberías:

👉 https://agencia-web-barberia-demo.vercel.app

Es una landing page moderna donde pueden:
- Mostrar su galería de cortes
- Publicar precios y servicios
- Agendar citas directamente por WhatsApp
- Aparecer en Google cuando alguien busque "barbería en Punto Fijo"

¿Les gustaría que la personalice con sus fotos reales, colores de la 
barbería y información de contacto?

Precio piloto esta semana: $150-200 (normal $300+)

¿Agendamos una llamada de 10 minutos para mostrarles más detalles?

Saludos,
Carlos Ávila
📱 0412-XXX-XXXX
🌐 carlos-avila-portfolio.vercel.app

---

¿Te gusta este email o quieres que ajuste algo?
- ¿Más formal/informal?
- ¿Agregar/quitar información?
- ¿Otro call to action?
```

---

## 📊 Variaciones por Nicho

### Para Restaurantes/Delivery:
```
Enfoque: Menú online, pedidos por WhatsApp, delivery tracking
Demo: https://agencia-web-delivery-demo.vercel.app
```

### Para Tiendas:
```
Enfoque: Catálogo de productos, carrito, horarios, ubicación
Demo: https://agencia-web-ferreteria-demo.vercel.app
```

### Para Servicios (Taxi, etc.):
```
Enfoque: Pedir servicio rápido, zonas de cobertura, tarifas
Demo: https://agencia-web-taxi-demo.vercel.app
```

---

## ⚠️ Errores Comunes

| Error | Cómo Evitarlo |
|-------|---------------|
| Email muy genérico | **Investiga** el negocio antes |
| No mencionar dónde los encontré | Siempre di **Instagram/Google/recomendación** |
| No mostrar demo | Incluye **URL de demo** relevante |
| No poner precio | Da un **rango** ($150-200) |
| No hay call to action | Pide **llamada de 10 min** |

---

## 🎓 Principios Subyacentes

- **Ventas Consultivas** - Primero entiende, luego ofrece
- **AIDA** - Atención, Interés, Deseo, Acción
- **Prueba Social** - Muestra demos reales, no promesas

---

*Skill creado para OpenClaw en Español - Hecho con 💚 por @avilacarlosdev*
