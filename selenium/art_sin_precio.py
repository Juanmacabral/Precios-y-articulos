from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("http://192.168.0.218/CONBRA/servlet/com.conbra.login")

# ingresar con usuario y contraseña
title = driver.title
driver.implicitly_wait(10)
user = driver.find_element(by=By.ID, value="vUSUARIO")
password = driver.find_element(by=By.ID, value="vPASSWORD")
confirm = driver.find_element(by=By.NAME, value="BUTTON2")
user.send_keys("juanc")
password.send_keys("conbra1")
confirm.click()

# ruta al reporte

reporte_stock_locales = driver.find_element(by=By.XPATH, value="//a[text()=' En que local esta?']").click()


# descarga del reporte


wait = WebDriverWait(driver, timeout=30)
producto = wait.until(EC.element_to_be_clickable((By.ID, "ReportViewerControl_ctl04_ctl00")))
producto.click()

