# Bibliotecas responsáveis por controlar o navegador
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Define a variável Browser
browser = webdriver.Chrome(ChromeDriverManager().install())
# Acessa a URL Definida
browser.get("https://10.10.0.1:7777/")

# Localizam elementos da pagina e insere as informações de login
browser.find_element(By.ID, "details-button").click()
browser.find_element(By.ID, "proceed-link").click()
browser.find_element(By.ID, "usernamefld").send_keys("admin")
browser.find_element(By.ID, "passwordfld").send_keys("pfsense")
browser.find_element(By.XPATH, "//input[@name='login']").click()

# Redireciona para outra página onde sera selecionada a opção de reboot após o login
browser.get("https://10.10.0.1:7777/diag_reboot.php")
browser.find_element(By.XPATH, "//button[@title='Reboot the system']").click()

browser.switch_to.alert.accept()
sleep(3)
browser.quit()
