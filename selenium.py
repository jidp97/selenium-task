from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicialización del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Navegar a YouTube
driver.get("https://www.youtube.com/")

# Esperar a que se cargue la página de inicio
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contents")))

# Buscar el video "The Weekend - Blinding Lights" (change this for your desired video)
search_box = driver.find_element(By.XPATH, "//input[@id='search']")
search_box.send_keys("The Weeknd - Blinding Lights")
search_box.submit()

# Esperar a que se carguen los resultados de la búsqueda
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contents")))

# Hacer clic en el primer video de la lista de resultados de búsqueda
video_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer[2]//a[@id='video-title']")))
video_title.click()


time.sleep(60)

# Cerrar el navegador al finalizar la prueba
driver.quit()
