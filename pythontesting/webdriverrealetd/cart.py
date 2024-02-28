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
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
total = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert total == sum
#driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span[class='promoInfo']")))
alert = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
assert "Code applied" in alert

# Assignment 2: The value is in decimal hence converted value to float
totalAfterDis = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)
#print(totalAfterDis)
dis_Perc= driver.find_element(By.XPATH,"//span[@class='discountPerc']").text
#print(dis_Perc)
x=int(dis_Perc[:-1])
#print(x)
dis_value = (total*x)/100
amount_After_discount= total - dis_value
assert totalAfterDis == amount_After_discount
print(amount_After_discount)



input("insert any  key to stop")

