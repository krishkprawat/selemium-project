import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from trio._subprocess_platform import windows

s = Service()

driver = webdriver.Chrome(service=s)

driver.implicitly_wait(10)
driver.get("https://www.makemytrip.com")
driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@data-cy='desktopCard_43']").send_keys("7060889488")
# driver.find_element(By.CSS_SELECTOR,".primaryBtn.font24.latoBold.widgetSearchBtn").click()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# wait= WebDriverWait(driver,8)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".messageSentStatusText")))
driver.find_element(By.CSS_SELECTOR,"label[for='fromCity']").click()
driver.find_element(By.CSS_SELECTOR,".react-autosuggest__input.react-autosuggest__input--open").send_keys("dehradun")
time.sleep(3)
driver.find_element(By.XPATH,"//ul[@class='react-autosuggest__suggestions-list']/li[1]").click()
driver.find_element(By.XPATH,"//div[@data-cy='returnArea']").click()
driver.find_element(By.XPATH,"//div[@aria-label='Wed Mar 13 2024']").click()
validate_Date = driver.find_element(By.XPATH,"//p[@data-cy='returnDay']").text
print(validate_Date)
driver.find_element(By.XPATH,"//a[text()='Search']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='OKAY, GOT IT!']").click()
sometext=driver.find_element(By.XPATH,"//p[@class='fontSize16 blackText appendLR20 appendBottom20 paddingTop20']").text
print(sometext)

assert "Dehradun → Bengaluru Sat, 2 Mar" in sometext
#assert "Wednesday" in  validate_Date
print(input("lets take a break"))
