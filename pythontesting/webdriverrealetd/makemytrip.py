from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

s = Service()

driver = webdriver.Chrome(service=s)

driver.implicitly_wait(10)
driver.get("https://www.makemytrip.com")
# driver.find_element(By.XPATH, "//input[@data-cy='desktopCard_43']").send_keys("7060889488")
# driver.find_element(By.CSS_SELECTOR,".primaryBtn.font24.latoBold.widgetSearchBtn").click()
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# wait= WebDriverWait(driver,8)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".messageSentStatusText")))
driver.find_element(By.CSS_SELECTOR,"label[for='fromCity']").click()
driver.find_element(By.CSS_SELECTOR,".react-autosuggest__input.react-autosuggest__input--open").send_keys("dehradun")
driver.find_element(By.XPATH,"//ul[@class='react-autosuggest__suggestions-list']/li[1]")


print(input("lets take a break"))
