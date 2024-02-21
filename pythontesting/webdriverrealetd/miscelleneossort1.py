import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# chrome_options= webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserlist= driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
allveg=driver.find_elements(By.XPATH,"//tr/td[1]")
originalveg=[]
for veg in allveg:
    originalveg.append(veg.text)

newlist=originalveg.copy()
originalveg.sort()
assert originalveg == newlist

input("enter a key to stop brwoser")


