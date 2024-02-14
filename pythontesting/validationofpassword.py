from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.ID, "userPassword").send_keys("boohoo123#")

driver.find_element(By.ID, "confirmPassword").send_keys("boooo113#")
value1=driver.find_element(By.ID,"userPassword").text
value2=driver.find_element(By.ID, "confirmPassword").text

driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

if value1==value2:
    print("The values of the two input elements are equal:")
else:
    print("The values of the two input elements are not equal.")




input("enter any key to close the browser") #this i added so tha browser cannot stop immediately


input("enter any key to close the browser") #this i added so tha browser cannot stop immediately

