from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("shorya@gmail.com")


driver.find_element(By.ID,"exampleInputPassword1").send_keys("secretpassword")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown_element=driver.find_element(By.ID,"exampleFormControlSelect1")
dropdown=Select(dropdown_element)
dropdown.select_by_visible_text("Male") # this is by providing the value
#dropdown.select_by_index(0) # this is select  by index
input("enter any key to close the browser")

