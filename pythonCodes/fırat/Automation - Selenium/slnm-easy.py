from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_browser = webdriver.Chrome("./chromedriver")

# print(chrome_browser)
# chrome_browser.maximize_window()
chrome_browser.maximize_window()
chrome_browser.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html")

show_message_button = chrome_browser.find_element_by_class_name(
    "btn-default")

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("ı am extra cool...")

show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")
print(output_message)

assert "ı am extra cool..." in output_message.text

Value_for_a = chrome_browser.find_element_by_id("sum1")
Value_for_b = chrome_browser.find_element_by_id("sum2")

Value_for_a.clear()
Value_for_b.clear()

Value_for_a.send_keys("10")
Value_for_b.send_keys("15")
assert "Get Total" in chrome_browser.page_source
# Get_Total = chrome_browser.find_element("Get Total")
# Get_Total.click()
Total = chrome_browser.find_element_by_xpath(
    "/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button")
Total.click()

Result = chrome_browser.find_element_by_id("displayvalue")

assert "25" in Result.text

print(Result.text)


chrome_browser.find_element_by_partial_link_text("Input Forms").click()
chrome_browser.find_element_by_partial_link_text("Checkbox Demo").click()

chrome_browser.find_element_by_id("isAgeSelected").click()
