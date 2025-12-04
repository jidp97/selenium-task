#!/usr/bin/env python3
"""
Script de diagnóstico para verificar la configuración en macOS
Ejecuta: python3 test_mac_setup.py
"""

import sys
import platform

def print_section(title):
    """Imprime una sección formateada."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)

def check_python_version():
    """Verifica la versión de Python."""
    print("\n🐍 Verificando Python...")
    version = sys.version_info
    print(f"   Versión: Python {version.major}.{version.minor}.{version.micro}")

    if version.major >= 3 and version.minor >= 7:
        print("   ✅ Versión compatible")
        return True
    else:
        print("   ❌ Necesitas Python 3.7 o superior")
        print("   Instala con: brew install python")
        return False

def check_platform():
    """Verifica el sistema operativo."""
    print("\n💻 Verificando Sistema Operativo...")
    os_name = platform.system()
    print(f"   Sistema: {os_name}")
    print(f"   Versión: {platform.release()}")
    print(f"   Máquina: {platform.machine()}")

    if os_name == "Darwin":
        print("   ✅ macOS detectado")
        if platform.machine() == "arm64":
            print("   ℹ️  Apple Silicon (M1/M2/M3) detectado")
        return True
    else:
        print(f"   ⚠️  Este script es para macOS, detectado: {os_name}")
        return False

def check_pyautogui():
    """Verifica PyAutoGUI y permisos."""
    print("\n🖱️  Verificando PyAutoGUI...")
    try:
        import pyautogui
        print(f"   ✅ PyAutoGUI instalado (v{pyautogui.__version__})")

        # Intentar obtener posición del mouse
        try:
            pos = pyautogui.position()
            print(f"   ✅ Posición del mouse detectada: {pos}")
            print("   ✅ Permisos de Accesibilidad: OK")
            return True
        except Exception as e:
            print(f"   ❌ Error al acceder al mouse: {e}")
            print("\n   🔧 SOLUCIÓN:")
            print("   1. Ve a: Preferencias del Sistema → Seguridad y Privacidad")
            print("   2. Pestaña Privacidad → Accesibilidad")
            print("   3. Añade Terminal y Python a la lista")
            print("   4. Reinicia la Terminal")
            return False

    except ImportError:
        print("   ❌ PyAutoGUI no está instalado")
        print("   Instala con: pip3 install pyautogui")
        return False

def check_opencv():
    """Verifica OpenCV."""
    print("\n📷 Verificando OpenCV...")
    try:
        import cv2
        print(f"   ✅ OpenCV instalado (v{cv2.__version__})")

        # Verificar que puede leer imágenes
        try:
            import numpy as np
            test_img = np.zeros((100, 100, 3), dtype=np.uint8)
            result = cv2.matchTemplate(test_img, test_img, cv2.TM_CCOEFF_NORMED)
            print("   ✅ OpenCV funcionando correctamente")
            return True
        except Exception as e:
            print(f"   ⚠️  OpenCV instalado pero con advertencias: {e}")
            return True

    except ImportError:
        print("   ❌ OpenCV no está instalado")
        print("   Instala con: pip3 install opencv-python")
        return False

def check_pillow():
    """Verifica Pillow."""
    print("\n🖼️  Verificando Pillow...")
    try:
        from PIL import Image
        print(f"   ✅ Pillow instalado")
        return True
    except ImportError:
        print("   ❌ Pillow no está instalado")
        print("   Instala con: pip3 install Pillow")
        return False

def check_numpy():
    """Verifica NumPy."""
    print("\n🔢 Verificando NumPy...")
    try:
        import numpy as np
        print(f"   ✅ NumPy instalado (v{np.__version__})")
        return True
    except ImportError:
        print("   ❌ NumPy no está instalado")
        print("   Instala con: pip3 install numpy")
        return False

def check_screenshot_permission():
    """Verifica permisos de captura de pantalla."""
    print("\n📸 Verificando permisos de captura de pantalla...")
    try:
        import pyautogui
        screenshot = pyautogui.screenshot()
        if screenshot:
            print(f"   ✅ Captura de pantalla exitosa ({screenshot.size})")
            print("   ✅ Permisos de Grabación de Pantalla: OK")
            return True
        else:
            print("   ❌ No se pudo capturar pantalla")
            return False
    except Exception as e:
        print(f"   ❌ Error al capturar pantalla: {e}")
        print("\n   🔧 SOLUCIÓN:")
        print("   1. Ve a: Preferencias del Sistema → Seguridad y Privacidad")
        print("   2. Pestaña Privacidad → Grabación de Pantalla")
        print("   3. Añade Terminal a la lista")
        print("   4. Reinicia la Terminal")
        return False

def check_reference_image():
    """Verifica que existe la carpeta de imágenes de referencia."""
    print("\n🖼️  Verificando estructura de archivos...")
    from pathlib import Path

    ref_dir = Path("reference_images")
    ref_img = ref_dir / "event_icon.png"

    if ref_dir.exists():
        print(f"   ✅ Carpeta 'reference_images/' existe")
    else:
        print(f"   ❌ Carpeta 'reference_images/' no existe")
        return False

    if ref_img.exists():
        print(f"   ✅ Imagen de referencia encontrada: {ref_img}")

        # Verificar que se puede leer
        try:
            import cv2
            img = cv2.imread(str(ref_img))
            if img is not None:
                h, w = img.shape[:2]
                print(f"   ✅ Imagen válida ({w}x{h} píxeles)")
                return True
            else:
                print(f"   ❌ No se pudo leer la imagen")
                return False
        except:
            print(f"   ⚠️  No se pudo verificar la imagen")
            return True
    else:
        print(f"   ⚠️  Imagen de referencia no encontrada")
        print(f"   Guarda tu captura como: {ref_img}")
        return False

def main():
    """Función principal."""
    print_section("🍎 Diagnóstico de Configuración para macOS")
    print("\nEste script verificará que tu Mac está configurado correctamente")
    print("para ejecutar el bot de automatización de LastZ: Survival.")

    checks = {
        "Sistema Operativo": check_platform(),
        "Python": check_python_version(),
        "NumPy": check_numpy(),
        "Pillow": check_pillow(),
        "OpenCV": check_opencv(),
        "PyAutoGUI": check_pyautogui(),
        "Permisos de Captura": check_screenshot_permission(),
        "Imagen de Referencia": check_reference_image(),
    }

    print_section("📊 Resumen")

    passed = sum(checks.values())
    total = len(checks)

    print(f"\n   Pruebas pasadas: {passed}/{total}\n")

    for check_name, result in checks.items():
        status = "✅" if result else "❌"
        print(f"   {status} {check_name}")

    print("\n" + "="*60)

    if passed == total:
        print("\n🎉 ¡Todo está configurado correctamente!")
        print("\n📝 Próximos pasos:")
        print("   1. Asegúrate de tener la imagen del evento en reference_images/event_icon.png")
        print("   2. Abre tu emulador y el juego LastZ: Survival")
        print("   3. Ejecuta: python3 game_event_bot.py")
        print("\n¡Disfruta del bot! 🎮")
    elif passed >= total - 1:
        print("\n⚠️  Casi listo, solo falta un detalle.")
        print("   Revisa el paso marcado con ❌ arriba y corrígelo.")
    else:
        print("\n❌ Faltan algunas configuraciones.")
        print("\n📚 Consulta la guía completa en: MAC_SETUP.md")
        print("\n🔧 Pasos rápidos:")

        if not checks["PyAutoGUI"] or not checks["Permisos de Captura"]:
            print("\n   PERMISOS:")
            print("   • Preferencias del Sistema → Seguridad y Privacidad")
            print("   • Privacidad → Accesibilidad → Añadir Terminal")
            print("   • Privacidad → Grabación de Pantalla → Añadir Terminal")
            print("   • REINICIAR Terminal después de dar permisos")

        if not any([checks["NumPy"], checks["Pillow"], checks["OpenCV"], checks["PyAutoGUI"]]):
            print("\n   DEPENDENCIAS:")
            print("   • pip3 install -r requirements.txt")

    print("\n" + "="*60 + "\n")

    return passed == total

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Diagnóstico interrumpido por el usuario.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        sys.exit(1)
