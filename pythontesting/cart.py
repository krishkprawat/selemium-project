import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("roo")
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# starts a new page
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode]").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button[class=promoBtn]").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

input("insert any  key to stop")
