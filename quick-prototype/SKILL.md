---
name: Quick Prototype
slug: quick-prototype
version: 1.0.0
homepage: https://clawic.com/skills/quick-prototype
description: "Build de prototipos desechables para explorar diseño: apps de terminal para lógica, UIs múltiples para diseño visual."
changelog: "Skill inicial para prototipado rápido en OpenClaw."
metadata: {"clawdbot":{"emoji":"🚀","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["~/quick-prototype/"]}}
---

## When to Use

Usa este skill cuando:
- Quieres explorar un diseño antes de comprometerte
- Hay incertidumbre sobre cómo debería funcionar algo
- Necesitas validar una idea rápidamente
- Para comparar múltiples enfoques side-by-side
- Cuando "pensar con las manos" es más efectivo que discutir

**NO uses** para:
- Código de producción
- Cuando los requisitos son claros y estables
- Features críticas que necesitan tests completos

## Architecture

Memoria vive en `~/quick-prototype/`.

```
~/quick-prototype/
├── memory.md        # Prototipos activos, aprendizajes
└── prototypes/      # Prototipos creados (desechables)
```

## Prototyping Strategies

### 🖥️ ESTRATEGIA A: Terminal App (Para Lógica/Estado)

**Cuándo:** Para explorar state machines, flujos de negocio, algoritmos.

**Ejemplo:**
```bash
# Prototipo en Python para explorar flujo de checkout
mkdir /tmp/checkout-prototype
cd /tmp/checkout-prototype

cat > checkout.py << 'EOF'
# Estado del carrito
cart = {
    'items': [],
    'discount': 0,
    'shipping': 0
}

def add_item(name, price, qty=1):
    cart['items'].append({'name': name, 'price': price, 'qty': qty})
    print(f"Agregado: {name} x{qty}")

def apply_discount(code):
    if code == 'VIP20':
        cart['discount'] = 0.2
        print("Descuento VIP aplicado: 20%")
    else:
        print("Código inválido")

def calculate_total():
    subtotal = sum(item['price'] * item['qty'] for item in cart['items'])
    discount_amt = subtotal * cart['discount']
    total = subtotal - discount_amt + cart['shipping']
    return total

# Explorar flujo
add_item('Producto A', 100, 2)
add_item('Producto B', 50)
apply_discount('VIP20')
print(f"Total: ${calculate_total()}")
EOF

python checkout.py
```

**Ventajas:**
- ✅ Rápido de crear y modificar
- ✅ Fácil de probar diferentes escenarios
- ✅ Sin distracciones de UI
- ✅ Enfocado en lógica pura

### 🎨 ESTRATEGIA B: UI Múltiple (Para Diseño Visual)

**Cuándo:** Para explorar diferentes enfoques de UI/UX.

**Ejemplo:**
```bash
# Crear 3 variaciones de un dashboard
mkdir -p /tmp/dashboard-prototype/{v1,v2,v3}

# v1: Minimalista
cat > /tmp/dashboard-prototype/v1/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Dashboard v1 - Minimal</title></head>
<body style="font-family: system-ui; padding: 2rem;">
  <h1>Dashboard</h1>
  <div style="display: grid; gap: 1rem; grid-template-columns: repeat(3, 1fr);">
    <div style="padding: 2rem; background: #f0f0f0; border-radius: 8px;">
      <h3>Usuarios</h3>
      <p style="font-size: 2rem; font-weight: bold;">1,234</p>
    </div>
    <!-- Más cards... -->
  </div>
</body>
</html>
EOF

# v2: Con sidebar
# v3: Con tabs

# Abrir en browser
open /tmp/dashboard-prototype/v1/index.html
open /tmp/dashboard-prototype/v2/index.html
open /tmp/dashboard-prototype/v3/index.html
```

**Ventajas:**
- ✅ Compara enfoques visualmente
- ✅ Stakeholders pueden ver y dar feedback
- ✅ Itera rápido basado en reacción
- ✅ Desechable: no te encariñas

### 🧪 ESTRATEGIA C: Spike Técnico

**Cuándo:** Para validar viabilidad técnica de un enfoque.

**Ejemplo:**
```bash
# ¿Podemos usar WebSockets para notificaciones en tiempo real?
mkdir /tmp/websocket-spike
cd /tmp/websocket-spike

# Server mínimo
npm init -y
npm install ws

cat > server.js << 'EOF'
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', ws => {
  console.log('Cliente conectado');
  
  ws.on('message', message => {
    console.log('Recibido:', message.toString());
    ws.send(`Echo: ${message}`);
  });
  
  // Simular notificación push
  setInterval(() => {
    ws.send(JSON.stringify({
      type: 'notification',
      data: { message: '¡Nueva orden!' }
    }));
  }, 5000);
});

console.log('Server corriendo en ws://localhost:8080');
EOF

node server.js
```

**Output:**
- ✅ Confirma que la tecnología funciona
- ✅ Identifica problemas tempranos
- ✅ Proporciona código base si se aprueba

## Prototyping Workflow

### 1️⃣ DEFINIR LA PREGUNTA

**Antes de prototipar, clarifica:**
- ¿Qué estamos tratando de aprender?
- ¿Qué incertidumbre queremos resolver?
- ¿Qué criterio de éxito tiene este prototipo?

**Ejemplos:**
- "¿Este flujo de checkout es intuitivo?"
- "¿Podemos procesar 1000 eventos/segundo con WebSockets?"
- "¿Qué layout de dashboard es más scannable?"

### 2️⃣ TIMEBOX

**Regla de oro:** Un prototipo no debe tomar más de:
- 🕐 1-2 horas para exploraciones simples
- 🕐 1 día para spikes técnicos complejos

**Si toma más →** Se está convirtiendo en código de producción prematuro.

### 3️⃣ BUILD RÁPIDO

**Principios:**
- Hardcodea valores (no necesitas configuración)
- Ignora edge cases (explora el happy path)
- Sin tests (el prototipo es el test)
- Sin error handling (si falla, lo arreglas o lo descartas)
- Copia y pega está OK (no hay refactor)

### 4️⃣ PROBAR Y APRENDER

**Para prototipos de UI:**
- Muestra a usuarios/stakeholders
- Observa dónde hacen clic
- Pregunta: "¿Qué esperas que pase aquí?"

**Para prototipos de lógica:**
- Ejecuta diferentes escenarios
- Verifica que el output sea el esperado
- Identifica edge cases no considerados

**Para spikes técnicos:**
- ¿Funciona la tecnología?
- ¿Cuáles son los límites?
- ¿Qué complejidad oculta descubriste?

### 5️⃣ DECIDIR Y DESECHAR

**Después de prototipar:**

| Resultado | Decisión |
|-----------|----------|
| ✅ Funciona, aprendimos | Descarta prototipo, implementa versión real con lo aprendido |
| ⚠️ Funciona parcial | Itera con otro prototipo más enfocado |
| ❌ No funciona | Descarta, elige otro enfoque, prototipa de nuevo |

**Regla crítica:** El prototipo SE DESCARTA. No se mergea a producción.

## Documentation

**Después de cada prototipo, documenta:**

```markdown
# Prototipo: [Nombre]
**Fecha:** YYYY-MM-DD
**Pregunta:** ¿Qué queríamos aprender?

## Enfoque
[Qué construimos y por qué]

## Aprendizajes
- ✅ [Lo que funcionó]
- ⚠️ [Lo que no funcionó]
- 💡 [Insights sorpresa]

## Decisión
[Qué haremos basado en esto]

## Código
[Ubicación del prototipo, si se guarda como referencia]
```

## Common Traps

| Trap | Por qué falla | Mejor movimiento |
|------|---------------|------------------|
| Prototipo se vuelve producción | Deuda técnica, atajos se vuelven permanentes | Timebox estricto, descarta siempre |
| Sobre-ingeniería del prototipo | Pierdes velocidad, te encariñas | Hardcodea, ignora edge cases |
| No definir la pregunta | Prototipo sin dirección, no aprendes nada | Clarifica qué quieres aprender primero |
| No compartir aprendizajes | El equipo no se beneficia | Documenta y comunica resultados |
| Prototipar demasiado tarde | Ya tomaste decisiones, prototipo es teatro | Prototipa temprano, antes de comprometerte |

## Adapt to the User

- **Para designers:** UI múltiple, feedback visual rápido
- **Para devs:** Terminal apps, spikes técnicos
- **Para PMs:** Prototipos para validar con usuarios
- **Para founders:** Prototipos para validar ideas con inversores

## Scope

Este skill SÓLO:
- Crea prototipos desechables para explorar
- Timeboxea exploraciones
- Documenta aprendizajes
- Ayuda a decidir entre enfoques

Este skill NUNCA:
- Mergea prototipos a producción
- Promete que el prototipo es el producto final
- Modifica su propio archivo de skill

## Data Storage

Estado local vive en `~/quick-prototype/`:

- `memory.md` - Prototipos activos, aprendizajes
- `prototypes/` - Prototipos creados (desechables)

## Related Skills

- `grill-with-docs` - Para clarificar qué prototipar
- `tdd-helper` - Para implementar versión real después del prototipo
- `arch-improver` - Para evaluar arquitectura del prototipo vs producción

## Feedback

- Si fue útil: `clawhub star quick-prototype`
- Mantente actualizado: `clawhub sync`
