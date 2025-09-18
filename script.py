from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import os

load_dotenv()


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 2)

driver.get(os.getenv("REPORT_URL"))

driver.implicitly_wait(1)

username = wait.until(
    ec.element_to_be_clickable((By.ID, "username"))
)

username.send_keys(os.getenv("USUARIO"))

username = wait.until(
    ec.element_to_be_clickable((By.ID, "password"))
)
username.send_keys(os.getenv("SENHA"))


company = Select(driver.find_element(by=By.ID, value="companies"))

wait.until(lambda d: len(company.options) > 1)

company.select_by_value("1")

submit_button = driver.find_element(by=By.NAME, value="submit")

submit_button.click()

driver.quit()