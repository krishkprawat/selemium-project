from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

mygrab=driver.find_element(By.CSS_SELECTOR,".red").text
emails = [word for word in mygrab.split() if '@' in word and '.' in word]
print(emails)




input("insert any  key to stop")
