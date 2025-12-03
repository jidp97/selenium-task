# 🎮 Bot de Automatización - LastZ: Survival

Bot automático para detectar y participar en el evento de **Excavación de Tesoro** en LastZ: Survival, incluso cuando no estás presente.

## 📋 Descripción

Este programa monitorea constantemente la pantalla de tu emulador Android y detecta automáticamente cuando aparece el icono del evento de excavación de tesoro. Cuando lo detecta, hace clic automáticamente para que puedas participar sin estar presente.

## ✨ Características

- ✅ Detección automática del icono del evento mediante reconocimiento de imágenes
- ✅ Clic automático en el evento cuando se detecta
- ✅ Registro detallado de todas las acciones (log)
- ✅ Configuración ajustable de sensibilidad y frecuencia
- ✅ Contador de clics realizados
- ✅ Fácil de pausar/detener (Ctrl+C)

## 🔧 Requisitos

### Software Necesario

1. **Python 3.7 o superior**
2. **Emulador Android** (BlueStacks, LDPlayer, NoxPlayer, etc.)
3. **LastZ: Survival** instalado en el emulador

### Bibliotecas Python

Todas las dependencias se instalan automáticamente con el comando de instalación (ver más abajo).

## 📦 Instalación

### 1. Clonar o descargar este repositorio

```bash
git clone <tu-repositorio>
cd selenium-task
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

**Nota para Windows**: Si tienes problemas instalando opencv-python, prueba:
```bash
pip install opencv-python-headless
```

### 3. Configurar la imagen de referencia

Este es el paso **MÁS IMPORTANTE**:

1. **Abre tu emulador y LastZ: Survival**
2. **Espera a que aparezca el icono del evento de excavación** en la pantalla
3. **Captura solo el icono del evento** (puedes usar la herramienta de recortes de Windows o cualquier capturador de pantalla)
4. **Guarda la imagen** como: `reference_images/event_icon.png`

#### 💡 Consejos para la captura:

- ✅ Captura **SOLO** el icono/botón del evento, sin elementos extra
- ✅ La imagen debe ser lo más **pequeña y precisa** posible
- ✅ Asegúrate de que la captura sea **nítida** (no borrosa)
- ✅ Formato recomendado: PNG
- ❌ No incluyas texto o elementos que cambien
- ❌ No captures cuando el icono esté medio oculto

**Ejemplo de estructura esperada:**
```
selenium-task/
├── game_event_bot.py
├── requirements.txt
├── README.md
└── reference_images/
    └── event_icon.png  ← Tu captura aquí
```

## 🚀 Uso

### Ejecución Básica

1. **Abre tu emulador y el juego LastZ: Survival**
2. **Ejecuta el bot:**

```bash
python game_event_bot.py
```

3. **El bot te dará 5 segundos** para cambiar a la ventana del emulador
4. **Mantén el emulador visible** en la pantalla (puede estar en segundo plano pero debe ser visible)
5. **El bot comenzará a monitorear** y hará clic automáticamente cuando detecte el evento

### Detener el Bot

- Presiona **Ctrl + C** en la terminal donde está corriendo el bot
- El bot mostrará un resumen de clics realizados

## ⚙️ Configuración Avanzada

Puedes ajustar los parámetros dentro de `game_event_bot.py` en la función `main()`:

```python
# Configuración
event_image = "reference_images/event_icon.png"  # Ruta de la imagen
confidence = 0.8          # Confianza del reconocimiento (0.0 - 1.0)
check_interval = 2        # Segundos entre cada verificación
```

### Parámetros Explicados:

- **`confidence`** (0.0 - 1.0):
  - `0.9` = Muy estricto, menos falsos positivos pero puede perder detecciones
  - `0.8` = Balanceado (recomendado)
  - `0.7` = Más permisivo, detecta mejor pero puede tener falsos positivos

- **`check_interval`** (segundos):
  - Intervalo entre verificaciones de pantalla
  - `2` segundos es recomendado para no consumir muchos recursos
  - Puedes bajar a `1` para respuesta más rápida (usa más CPU)

## 📊 Logs y Monitoreo

El bot genera un archivo `game_bot.log` con todas las acciones realizadas:

- Cada detección del evento
- Cada clic realizado
- Errores o problemas encontrados
- Timestamps de todas las acciones

Puedes revisar este archivo para ver el historial de actividad.

## 🎯 Emuladores Recomendados

El bot funciona con cualquier emulador, pero estos son los más populares:

1. **BlueStacks** - [descargar](https://www.bluestacks.com/)
2. **LDPlayer** - [descargar](https://www.ldplayer.net/)
3. **NoxPlayer** - [descargar](https://www.bignox.com/)
4. **MEmu** - [descargar](https://www.memuplay.com/)

**Recomendación**: Configura el emulador en modo ventana (no pantalla completa) para mejor detección.

## ❓ Solución de Problemas

### El bot no encuentra el evento (incluso cuando está visible)

1. **Verifica la imagen de referencia**: Asegúrate de que `reference_images/event_icon.png` sea una captura precisa del icono
2. **Baja el nivel de confianza**: Cambia `confidence` a `0.7` o `0.75`
3. **Recaptura la imagen**: Puede que las condiciones de captura hayan cambiado (resolución, zoom, etc.)
4. **Verifica que el emulador esté visible**: El bot solo detecta lo que se ve en pantalla

### El bot hace clic en lugares incorrectos

1. **Sube el nivel de confianza**: Cambia `confidence` a `0.85` o `0.9`
2. **Mejora la imagen de referencia**: Captura solo el icono, sin elementos extra

### Error "No se encuentra la imagen de referencia"

- Verifica que hayas creado la carpeta `reference_images/`
- Verifica que la imagen se llame exactamente `event_icon.png`
- Verifica la ruta en el código si la cambiaste

### El bot consume mucha CPU

- Aumenta el `check_interval` a `3` o `5` segundos
- Reduce la resolución del emulador si es muy alta

## 🛡️ Consideraciones de Seguridad

- Este bot **NO modifica** el juego, solo automatiza clics en la pantalla
- **Usa bajo tu propio riesgo**: Verifica los términos de servicio del juego
- El bot solo funciona localmente en tu PC, no envía datos a internet
- Recomendado usar en cuenta secundaria primero para pruebas

## 📝 Notas Importantes

- ⚠️ **Mantén el emulador visible**: El bot captura lo que se ve en pantalla
- ⚠️ **No muevas el emulador** una vez configurado y en funcionamiento
- ⚠️ **Supervisa ocasionalmente**: Verifica que el bot esté funcionando correctamente
- 💡 **Prueba primero**: Ejecuta el bot por unos minutos para verificar que funciona antes de dejarlo desatendido

## 🤝 Contribuciones

Si tienes mejoras o encuentras bugs, siéntete libre de:
- Abrir un Issue
- Enviar un Pull Request
- Compartir tus configuraciones óptimas

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🎮 ¡Disfruta del bot!

Si el bot te ayuda a no perder eventos de excavación, ¡dale una ⭐ al repositorio!

---

**Disclaimer**: Este bot es una herramienta de automatización de pantalla. El uso de bots puede violar los términos de servicio de algunos juegos. Usa bajo tu propio riesgo y responsabilidad.
