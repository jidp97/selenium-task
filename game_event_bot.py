#!/usr/bin/env python3
"""
Bot de Automatización para Eventos de LastZ: Survival
Detecta automáticamente el evento de excavación de tesoro y hace clic.
"""

import pyautogui
import cv2
import numpy as np
import time
import logging
from datetime import datetime
from pathlib import Path
import sys

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game_bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class GameEventBot:
    """Bot para detectar y hacer clic automáticamente en eventos del juego."""

    def __init__(self, event_image_path, confidence=0.8, check_interval=2):
        """
        Inicializa el bot.

        Args:
            event_image_path: Ruta a la imagen del icono del evento
            confidence: Nivel de confianza para el reconocimiento (0.0-1.0)
            check_interval: Intervalo en segundos entre cada verificación
        """
        self.event_image_path = Path(event_image_path)
        self.confidence = confidence
        self.check_interval = check_interval
        self.running = False
        self.clicks_count = 0

        # Verificar que existe la imagen de referencia
        if not self.event_image_path.exists():
            raise FileNotFoundError(
                f"No se encuentra la imagen de referencia: {event_image_path}\n"
                f"Por favor, captura una imagen del icono del evento y guárdala en: {event_image_path}"
            )

        logger.info(f"Bot inicializado con imagen: {event_image_path}")
        logger.info(f"Confianza: {confidence}, Intervalo: {check_interval}s")

    def find_event_on_screen(self):
        """
        Busca el icono del evento en la pantalla.

        Returns:
            Tuple con (x, y) del centro del icono si se encuentra, None si no.
        """
        try:
            # Capturar la pantalla
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # Cargar la imagen del evento a buscar
            event_template = cv2.imread(str(self.event_image_path))

            if event_template is None:
                logger.error(f"No se pudo cargar la imagen: {self.event_image_path}")
                return None

            # Buscar la imagen en la pantalla usando template matching
            result = cv2.matchTemplate(screenshot, event_template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Si la confianza es suficiente, retornar la posición
            if max_val >= self.confidence:
                h, w = event_template.shape[:2]
                # Calcular el centro del área encontrada
                center_x = max_loc[0] + w // 2
                center_y = max_loc[1] + h // 2
                logger.info(f"¡Evento encontrado! Confianza: {max_val:.2%} en posición ({center_x}, {center_y})")
                return (center_x, center_y)

            return None

        except Exception as e:
            logger.error(f"Error al buscar evento en pantalla: {e}")
            return None

    def click_event(self, position):
        """
        Hace clic en la posición del evento.

        Args:
            position: Tuple (x, y) donde hacer clic
        """
        try:
            x, y = position
            logger.info(f"Haciendo clic en posición ({x}, {y})")

            # Mover el mouse y hacer clic
            pyautogui.moveTo(x, y, duration=0.3)
            time.sleep(0.2)
            pyautogui.click()

            self.clicks_count += 1
            logger.info(f"✓ Clic exitoso #{self.clicks_count}")

            # Esperar un poco más después de hacer clic
            # para dar tiempo a que se cargue el evento
            time.sleep(3)

        except Exception as e:
            logger.error(f"Error al hacer clic: {e}")

    def start(self):
        """Inicia el monitoreo automático."""
        self.running = True
        logger.info("="*60)
        logger.info("🎮 Bot de eventos iniciado - Presiona Ctrl+C para detener")
        logger.info("="*60)

        try:
            while self.running:
                logger.info("Buscando evento de excavación...")

                # Buscar el evento en la pantalla
                position = self.find_event_on_screen()

                if position:
                    # Si se encuentra, hacer clic
                    self.click_event(position)
                else:
                    logger.info("Evento no detectado. Esperando...")

                # Esperar antes de la siguiente verificación
                time.sleep(self.check_interval)

        except KeyboardInterrupt:
            logger.info("\n" + "="*60)
            logger.info("Bot detenido por el usuario")
            logger.info(f"Total de clics realizados: {self.clicks_count}")
            logger.info("="*60)
            self.running = False
        except Exception as e:
            logger.error(f"Error crítico: {e}")
            self.running = False

    def stop(self):
        """Detiene el bot."""
        self.running = False
        logger.info("Deteniendo bot...")


def main():
    """Función principal."""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║  Bot de Automatización - LastZ: Survival                  ║
    ║  Evento: Excavación de Tesoro                             ║
    ╚════════════════════════════════════════════════════════════╝
    """)

    # Configuración
    event_image = "reference_images/event_icon.png"
    confidence = 0.8  # 80% de confianza
    check_interval = 2  # Verificar cada 2 segundos

    # Instrucciones si no existe la imagen
    if not Path(event_image).exists():
        print("⚠️  CONFIGURACIÓN NECESARIA:")
        print(f"    1. Captura una imagen del icono del evento de excavación")
        print(f"    2. Guárdala como: {event_image}")
        print(f"    3. Vuelve a ejecutar este script")
        print()
        print("💡 Consejo: La imagen debe mostrar SOLO el icono/botón del evento,")
        print("   lo más pequeña y precisa posible para mejor reconocimiento.")
        return

    print(f"📁 Imagen de referencia: {event_image}")
    print(f"🎯 Nivel de confianza: {confidence:.0%}")
    print(f"⏱️  Intervalo de verificación: {check_interval}s")
    print()
    print("Tienes 5 segundos para cambiar al emulador...")

    for i in range(5, 0, -1):
        print(f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print("\n")

    # Crear e iniciar el bot
    try:
        bot = GameEventBot(
            event_image_path=event_image,
            confidence=confidence,
            check_interval=check_interval
        )
        bot.start()
    except FileNotFoundError as e:
        logger.error(str(e))
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")


if __name__ == "__main__":
    main()
