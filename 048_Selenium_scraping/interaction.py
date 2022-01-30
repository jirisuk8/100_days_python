from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Development\\\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text.replace(",", ""))

# article_count.click()
all_partals = driver.find_element(By.LINK_TEXT, "All portals")
# all_partals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


# driver.quit()
