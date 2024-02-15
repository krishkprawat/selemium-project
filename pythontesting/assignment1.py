from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

mygrab=driver.find_element(By.CSS_SELECTOR,".red").text
emails = ' '.join(word for word in mygrab.split() if '@' in word and '.' in word)
print(emails)

#switch to main tab again
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(emails)
driver.find_element(By.ID,"password").send_keys("hahahaha")
driver.find_element(By.PARTIAL_LINK_TEXT,"terms and conditions").click()
driver.find_element(By.ID, "signInBtn").click()

wait= WebDriverWait(driver,10)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
alertmessage=driver.find_element(By.CSS_SELECTOR,".alert-danger").text
#print(alertmessage)
input("insert any  key to stop")
