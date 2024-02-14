from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj= Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")

driver.maximize_window() #to maximize the window
driver.get("https://rahulshettyacademy.com/consulting")
driver.minimize_window()
driver.back() # to go back to previuos url

driver.refresh() #refresh the current page in browser
driver.forward() #forward the url
print(driver.title)
print(driver.current_url)
driver.close()

