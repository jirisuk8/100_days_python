from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Development\\\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.maximize_window()
driver.get("http://secure-retreat-92358.herokuapp.com")
driver.find_element(By.NAME, "fName").send_keys("Angela")
driver.find_element(By.NAME, "lName").send_keys("Yu")
driver.find_element(By.NAME, "email").send_keys("angela@justtesting.com")
driver.find_element(By.CSS_SELECTOR, "body > form > button").click()





