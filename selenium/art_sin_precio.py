from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("http://192.168.0.218/CONBRA/servlet/com.conbra.login")

# ingresar con usuario y contraseña
driver.implicitly_wait(10)
user = driver.find_element(by=By.ID, value="vUSUARIO")
password = driver.find_element(by=By.ID, value="vPASSWORD")
confirm = driver.find_element(by=By.NAME, value="BUTTON2")
user.send_keys("juanc")
password.send_keys("conbra1")
confirm.click()

# ruta al reporte

consultas = driver.find_element(by=By.CLASS_NAME, value="smoothHeader").click()
art_sin_precio = driver.find_element(by=By.XPATH, value="//a[text()=' Productos Sin Precio']").click()

# descarga del reporte
driver.switch_to.frame("EMBPAGE1")
wait = WebDriverWait(driver, timeout=20)
driver.implicitly_wait(10)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

"""
boton = wait.until(EC.presence_of_element_located((By.ID, "ReportViewerControl_ctl06_ctl04_ctl00")))
boton.click()
csv = driver.find_element(by=By.XPATH, value="//a[text()='CSV (delimitado por comas)']").click()
"""