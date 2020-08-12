from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:/Program Files (x86)/Google/Chrome/chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.ccee.org.br/portal/faces/pages_publico/o-que-fazemos/como_ccee_atua/precos/preco_sombra")
print(driver.title)

search = driver.find_element_by_id("datefilterSombra")
search.clear()
search.send_keys("09/08/2020 - 10/08/2020")
search.send_keys(Keys.RETURN)

button = driver.find_element_by_id("btnFiltrarContratoCcee")
button.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
