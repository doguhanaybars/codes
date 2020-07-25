from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "http://google.com.tr"

driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("google.png")

url = "https://www.google.com/search?q=do%C4%9Fuhan+aybars+ay"
driver.get(url)
print(driver.title)
if "Google" in driver.title:
    driver.save_screenshot("google_deneme.png")
time.sleep(2)
driver.back()
time.sleep(2)
driver.close()