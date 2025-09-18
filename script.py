from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("http://soulmv.gruposanta.com.br/mvautenticador-cas/login?service=http%3A%2F%2Fsoulreport.gruposanta.com.br%3A80%2Freport-designer%2Flogin%2Fcas")

title = driver.title 

driver.implicitly_wait(0.5)

username = driver.find_element(by=By.NAME, value="username")

password = driver.find_element(by=By.NAME, value="password")

company = driver.find_element(by=By.NAME, value="company")

submit_button = driver.find_element(by=By.NAME, value="submit")

text_box.send_keys("Selenium")

submit_button.click()

message = driver.find_element(by=By.ID, value="message")

text = message.text

print(text)

driver.quit()