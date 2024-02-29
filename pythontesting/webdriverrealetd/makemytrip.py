from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

s = Service()

driver = webdriver.Chrome(service=s)

driver.implicitly_wait(10)
driver.get("https://www.makemytrip.com")
driver.find_element(By.XPATH, "//input[@data-cy='desktopCard_43']").send_keys("9997691792")
driver.find_element(By.XPATH, "//button[@data-cy='submitBtnWrapper']").click()
wait= WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@data-cy='messageSentStatusText']")))
driver.find_element(By.XPATH, "//li[@data-cy='HOLIDAYS']").click()

print(input("lets take a break"))
