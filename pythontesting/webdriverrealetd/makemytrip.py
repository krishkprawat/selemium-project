from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service()

driver=webdriver.Chrome(service=s)

driver.get("https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-01/03/2024_BLR-DEL-02/03/2024&tripType=R&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng")
results=driver.find_elements(By.XPATH,"//ul[@class='fareTypeOptions']/li[2]").click()
# for result in results:
#     result.find_elements(By.XPATH,"li[2]").click()


print(input("lets take a break"))
