import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, "input[class=search-keyword]").send_keys("roo")
time.sleep(3)

#gives a list
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

#loop to click all buttons together
for result in results:
    result.find_element(By.XPATH, "div/button").click()

input("insert any  key to stop")
