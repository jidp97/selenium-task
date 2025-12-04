# 🍎 Guía de Instalación y Configuración para macOS

Esta guía te ayudará a configurar el bot de automatización en tu Mac.

## ⚠️ Diferencias Clave en macOS

El bot **SÍ funciona en Mac**, pero requiere algunos pasos adicionales de configuración que Windows no necesita.

---

## 📦 Instalación en macOS

### 1. Instalar Python 3

Verifica si ya tienes Python instalado:
```bash
python3 --version
```

Si no lo tienes, instálalo con Homebrew:
```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python
```

### 2. Instalar dependencias del sistema

OpenCV necesita algunas librerías del sistema:
```bash
brew install opencv
```

### 3. Instalar dependencias de Python

```bash
# Desde la carpeta del proyecto
pip3 install -r requirements.txt
```

**Nota**: En Mac, usa `pip3` y `python3` en lugar de `pip` y `python`.

---

## 🔐 Configuración de Permisos (MUY IMPORTANTE)

macOS requiere permisos especiales para que el bot pueda controlar el mouse y capturar la pantalla.

### Paso 1: Dar permisos de Accesibilidad

1. **Abre Preferencias del Sistema** → **Seguridad y Privacidad**
2. Ve a la pestaña **Privacidad**
3. Selecciona **Accesibilidad** en el panel izquierdo
4. Haz clic en el candado 🔒 para hacer cambios (necesitarás tu contraseña)
5. Haz clic en **+** y añade:
   - **Terminal** (o **iTerm2** si lo usas)
   - **Python** (puede estar en `/usr/local/bin/python3` o `/opt/homebrew/bin/python3`)

### Paso 2: Dar permisos de Grabación de Pantalla

1. En la misma ventana de **Seguridad y Privacidad**
2. Selecciona **Grabación de Pantalla** en el panel izquierdo
3. Añade **Terminal** (o **iTerm2**)

**⚠️ Importante**: Después de añadir estos permisos, **reinicia la Terminal** para que surtan efecto.

---

## 🎮 Emuladores Recomendados para Mac

No todos los emuladores de Android funcionan bien en Mac. Estos son los más recomendados:

### 1. **BlueStacks** (Recomendado)
- [Descargar BlueStacks para Mac](https://www.bluestacks.com/download.html)
- Funciona bien en Mac Intel y Apple Silicon (M1/M2/M3)
- Mejor compatibilidad con el bot

### 2. **Android Studio Emulator**
- Más técnico pero muy estable
- Requiere instalación de Android Studio
- Ideal si ya desarrollas apps

### 3. **Genymotion**
- Opción profesional
- Requiere cuenta (hay versión gratuita)

**❌ NO recomendados en Mac:**
- LDPlayer (no disponible para Mac)
- NoxPlayer (versión Mac es inestable)
- MEmu (no disponible para Mac)

---

## 🚀 Ejecutar el Bot en Mac

```bash
# Desde la carpeta del proyecto
python3 game_event_bot.py
```

---

## 🔧 Solución de Problemas Específicos de Mac

### Error: "Operation not permitted" o "No permission"

**Causa**: Faltan permisos de accesibilidad.

**Solución**:
1. Verifica que Terminal/iTerm2 tenga permisos de Accesibilidad
2. Verifica que Terminal/iTerm2 tenga permisos de Grabación de Pantalla
3. **Reinicia la Terminal completamente** después de dar permisos

### Error: "ImportError: No module named '_tkinter'"

**Causa**: Python no tiene soporte para Tkinter (necesario para PyAutoGUI).

**Solución**:
```bash
# Instalar Python con Tkinter
brew install python-tk@3.11
```

### El bot no detecta el emulador

**Causa**: El emulador puede estar en un espacio/escritorio diferente.

**Solución**:
- Mantén el emulador en el **mismo escritorio/espacio** donde ejecutas el bot
- No uses Mission Control para cambiar de espacio mientras el bot está corriendo
- Asegúrate de que el emulador esté **visible** (no minimizado ni en pantalla completa)

### El mouse no se mueve o no hace clic

**Causa**: Falta el permiso de Accesibilidad para Python o Terminal.

**Solución**:
1. Ve a **Preferencias del Sistema** → **Seguridad y Privacidad** → **Accesibilidad**
2. Busca `Python` en la lista
   - Si no está, añádelo: busca en `/usr/local/bin/python3` o `/opt/homebrew/bin/python3`
3. Marca la casilla junto a Python y Terminal
4. **Reinicia la Terminal**

### Rendimiento lento en Mac con Apple Silicon (M1/M2/M3)

**Causa**: Algunas librerías pueden correr en modo Rosetta 2.

**Solución**:
```bash
# Instalar versiones nativas para Apple Silicon
arch -arm64 brew install python opencv
arch -arm64 pip3 install -r requirements.txt
```

---

## 🍎 Consejos Específicos para Mac

1. **Usa Terminal nativa o iTerm2**: Son más estables que otros terminales
2. **Desactiva Mission Control automático**: Ve a Preferencias del Sistema → Mission Control → desactiva "Reorganizar espacios automáticamente"
3. **Desactiva el protector de pantalla**: Para que el bot pueda correr sin interrupciones
4. **Modo "No molestar"**: Actívalo para evitar notificaciones que cubran la pantalla
5. **Mantén el Mac conectado a corriente**: Para evitar que entre en reposo

---

## 🧪 Probar que Todo Funciona

Ejecuta este script de prueba para verificar los permisos:

```bash
python3 -c "import pyautogui; print('✓ PyAutoGUI funciona'); pyautogui.position(); print('✓ Permisos OK')"
```

Si ves "✓ PyAutoGUI funciona" y "✓ Permisos OK", ¡estás listo!

---

## 📝 Diferencias con Windows

| Aspecto | Windows | macOS |
|---------|---------|-------|
| Comando Python | `python` | `python3` |
| Comando pip | `pip` | `pip3` |
| Permisos | No requiere configuración | Requiere permisos de Accesibilidad |
| Emuladores | Más opciones (BlueStacks, LDPlayer, Nox) | Limitado (principalmente BlueStacks) |
| Instalación | Más directa | Requiere Homebrew |

---

## ✅ Checklist de Configuración en Mac

Antes de ejecutar el bot, verifica:

- [ ] Python 3.7+ instalado (`python3 --version`)
- [ ] Dependencias instaladas (`pip3 install -r requirements.txt`)
- [ ] Permisos de **Accesibilidad** dados a Terminal/Python
- [ ] Permisos de **Grabación de Pantalla** dados a Terminal
- [ ] Terminal reiniciada después de dar permisos
- [ ] Emulador instalado (BlueStacks recomendado)
- [ ] Imagen de referencia guardada en `reference_images/event_icon.png`
- [ ] Emulador en modo ventana (no pantalla completa)

---

## 🆘 ¿Sigues Teniendo Problemas?

Si después de seguir todos estos pasos el bot no funciona:

1. Ejecuta el script de diagnóstico:
```bash
python3 -c "
import sys
print(f'Python: {sys.version}')
try:
    import pyautogui
    print('✓ PyAutoGUI: OK')
    pos = pyautogui.position()
    print(f'✓ Mouse position: {pos}')
except Exception as e:
    print(f'✗ PyAutoGUI: {e}')
try:
    import cv2
    print(f'✓ OpenCV: {cv2.__version__}')
except Exception as e:
    print(f'✗ OpenCV: {e}')
"
```

2. Revisa los logs del sistema:
```bash
tail -f ~/Library/Logs/Python/game_bot.log
```

3. Verifica los permisos nuevamente en Preferencias del Sistema

---

## 💡 Consejo Final

**Mac es más restrictivo con permisos de seguridad que Windows**, pero una vez configurado correctamente, el bot funciona igual de bien. Sé paciente con la configuración inicial de permisos.

Si todo lo demás falla, considera ejecutar el bot en una **máquina virtual con Windows** usando Parallels Desktop o VMware Fusion, donde la configuración es más directa.

---

¡Listo para automatizar en Mac! 🍎🎮
