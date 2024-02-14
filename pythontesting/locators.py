from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"email").send_keys("vijay@gmail.com")


driver.find_element(By.ID,"exampleInputPassword1").send_keys("secretpassword")
driver.find_element(By.ID,"exampleCheck1").click()
dropdown_element=driver.find_element(By.ID,"exampleFormControlSelect1")
dropdown=Select(dropdown_element)
dropdown.select_by_visible_text("Male") # this is by providing the value
#dropdown.select_by_index(0) # this is select  by index
driver.find_element(By.CSS_SELECTOR,"input[value=option2]").click() #cssselector locator
#driver.find_element(By.XPATH,"//input[@value=option1]").click() #xpath locator

#last submit button
driver.find_element(By.CSS_SELECTOR,"input[value=Submit]").click()
driver.find_element(By.CSS_SELECTOR,".ng-pristine ").send_keys("kpbhai")

message= driver.find_element(By.CSS_SELECTOR,".alert").text
assert "sucess!." in message #this is assertion to check after sucess the mesage contains success text or not.




input("enter any key to close the browser") #this i added so tha browser cannot stop immediately

