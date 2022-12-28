from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Carga el archivo de configuración
with open("../config.json", "r") as f:
    config = json.load(f)

# Accede a las credenciales de inicio de sesión
username = config["username"]
password = config["password"]

# Configurar el Webdriver
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("http://192.168.0.218/CONBRA/servlet/com.conbra.login")

# ingresar con usuario y contraseña
title = driver.title
driver.implicitly_wait(10)
usuario = driver.find_element(by=By.ID, value="vUSUARIO")
contraseña = driver.find_element(by=By.ID, value="vPASSWORD")
confirm = driver.find_element(by=By.NAME, value="BUTTON2")
usuario.send_keys(username)
contraseña.send_keys(password)
confirm.click()

# ruta al reporte

consultas = driver.find_element(by=By.CLASS_NAME, value="smoothHeader").click()
reporte_stock_locales = driver.find_element(by=By.XPATH, value="//a[text()=' En que local esta?']").click()

# descarga del reporte

driver.switch_to.frame("EMBPAGE1")

wait = WebDriverWait(driver, timeout=5)
producto = wait.until(EC.presence_of_element_located((By.ID, "ReportViewerControl_ctl04_ctl05_txtValue")))
producto.send_keys(110017901)
ver_informe = driver.find_element(by=By.ID, value='ReportViewerControl_ctl04_ctl00')
ver_informe.click()
