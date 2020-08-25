from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver")

# print(chrome_browser)
# chrome_browser.maximize_window()
chrome_browser.maximize_window()
chrome_browser.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html")

# True ise çalışır false ise hata döndürür
# assert "Selenium Easy Demo" in chrome_browser.title

button_text = chrome_browser.find_element_by_class_name("btn btn-default")
print(button_text.get_attribute("innerHTML"))
