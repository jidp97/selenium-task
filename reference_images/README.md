# 📸 Imágenes de Referencia

Esta carpeta debe contener la imagen del icono del evento que el bot buscará en la pantalla.

## 📝 Instrucciones

### Paso 1: Capturar la imagen del evento

1. Abre tu emulador Android (BlueStacks, LDPlayer, etc.)
2. Abre el juego **LastZ: Survival**
3. Espera a que aparezca el **icono del evento de excavación de tesoro** en la pantalla
4. Usa una herramienta de captura de pantalla para recortar **SOLO el icono del evento**

### Paso 2: Guardar la imagen

Guarda la imagen con el siguiente nombre **exacto**:
```
event_icon.png
```

La ruta completa debe ser:
```
reference_images/event_icon.png
```

## 💡 Consejos para una Captura Perfecta

### ✅ HAZ:
- Captura **SOLO** el icono/botón del evento (lo más pequeño posible)
- Asegúrate de que la imagen esté **nítida** y **clara**
- Usa formato **PNG** para mejor calidad
- Captura con el emulador en la **misma resolución** que usarás siempre
- Asegúrate de que no haya notificaciones u otros elementos sobre el icono

### ❌ NO HAGAS:
- No incluyas texto que pueda cambiar (temporizadores, contadores, etc.)
- No captures áreas grandes con otros elementos
- No uses imágenes borrosas o de baja calidad
- No captures cuando el icono está parcialmente oculto
- No incluyas el fondo si no es necesario

## 🖼️ Ejemplo Visual

```
┌────────────────────────────────────┐
│  Pantalla del Emulador (1920x1080)│
│                                    │
│     [Otros elementos del juego]    │
│                                    │
│           ╔═══════════╗            │  ← Captura SOLO este
│           ║  🏴 EVENTO ║            │    recuadro del icono
│           ╚═══════════╝            │
│                                    │
│     [Más elementos del juego]      │
└────────────────────────────────────┘

Archivo a guardar:
reference_images/event_icon.png
Tamaño aprox: 100x50 píxeles (o similar, lo más pequeño posible)
```

## 🔧 Herramientas Recomendadas para Captura

### Windows:
- **Herramienta de Recorte** (incluida en Windows)
- **Snip & Sketch** (Win + Shift + S)
- **ShareX** (gratuito, avanzado)

### Otras opciones:
- **Lightshot** (multiplataforma)
- **Greenshot** (Windows)
- Cualquier programa de captura de pantalla que permita recortar áreas específicas

## ✔️ Verificar que la Captura es Correcta

Antes de ejecutar el bot, verifica:

1. ✓ La imagen existe en: `reference_images/event_icon.png`
2. ✓ El nombre del archivo es **exactamente** `event_icon.png` (minúsculas)
3. ✓ La imagen muestra solo el icono del evento, sin elementos extra
4. ✓ La imagen es nítida y clara
5. ✓ El formato es PNG

## 🚀 ¿Listo?

Una vez que hayas guardado la imagen correctamente, ejecuta:

```bash
python game_event_bot.py
```

¡El bot comenzará a buscar el evento automáticamente!

---

**Nota**: Si el bot no detecta el evento, prueba capturar la imagen nuevamente con diferentes configuraciones de confianza en el código.
