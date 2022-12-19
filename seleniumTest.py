# bir kütüphaneden dosya import etmek
# kalıp => from {kütüphane-ismi} import {nesne-ismi}
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# HTML Locators

driver = webdriver.Chrome()
driver.get("https://www.google.com/")  # chromeda bu linki aç
# sitenin açılmasını bekle!
sleep(2) # defensive programming
input = driver.find_element(By.NAME,"q") # inputu bul
input.send_keys("Deneme")
sleep(3)
searchBtn = driver.find_element(By.NAME,"btnK")
searchBtn.click()