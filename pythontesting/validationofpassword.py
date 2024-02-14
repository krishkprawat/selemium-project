from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.ID,"userPassword")

input("enter any key to close the browser") #this i added so tha browser cannot stop immediately

