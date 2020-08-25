from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

browser = Chrome("./chromedriver")
browser.maximize_window()
browser.get("https://duckduckgo.com")


Search_bar = browser.find_element_by_id("search_button_homepage")
Duck_input = browser.find_element_by_name("q")
Duck_input.send_keys("dune")
# Search_bar.click()
# search bar ı tanımlamak yerine şu da yazılabilir.
Duck_input.submit()
