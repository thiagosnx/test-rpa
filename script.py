from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os

load_dotenv()


driver = webdriver.Chrome()


driver.get("http://mvsoulsml.corp.medgrupo.net:81/report-designer")

driver.implicitly_wait(5)

username = driver.find_element(by=By.NAME, value="username").send_keys(os.getenv("USUARIO"))

password = driver.find_element(by=By.NAME, value="password").send_keys(os.getenv("SENHA"))

company = driver.find_element(by=By.NAME, value="company")

submit_button = driver.find_element(by=By.NAME, value="submit")

submit_button.click()

message = driver.find_element(by=By.ID, value="message")

text = message.text

print(text)

driver.quit()