from selenium import webdriver

from selenium.webdriver.chrome.service import Service

service_obj= Service()

driver = webdriver.Chrome(service=service_obj)

================================================


this is the main lines to ue in python scripts in selenium. for browsers we need a seperate drivers.

for chrome- chrome webdriver

for firefox- geko driver

driver = webdriver.firefox(service=service_obj)
