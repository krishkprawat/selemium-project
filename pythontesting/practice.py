import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@id='checkBoxOption1']").click()
#select dropdown
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example"))
dropdown.select_by_value("option1")

#table sum of values integer
values= driver.find_elements(By.XPATH,"")
sum=0
for value in values:
    newvalue=value.find_element(By.CSS_SELECTOR,"/td[4]")
    sum=sum+newvalue
    print(sum)
input("enter any keyword to stop the screen")