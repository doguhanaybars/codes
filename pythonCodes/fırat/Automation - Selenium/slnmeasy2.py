from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_ = webdriver.Chrome("./chromedriver")
chrome_.maximize_window()
chrome_.delete_all_cookies()
chrome_.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

chrome_.find_element_by_id("isAgeSelected").click()

result = chrome_.find_element_by_id("txtAge")

assert "Success - Check box is checked" in result.text

chrome_.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
