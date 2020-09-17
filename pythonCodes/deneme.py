from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.maximize_window()
chrome_browser.get(
    "https://sabis.sakarya.edu.tr/tr/Login?return=http%3a%2f%2fsabis.sakarya.edu.tr%2f")
# sleep(10)

chrome_browser.find_element_by_id(
    "UserName").send_keys("g131210091")
chrome_browser.find_element_by_id(
    "Password").send_keys("ŞİFRE")
chrome_browser.find_element_by_id("btnLogin").click()
chrome_browser.find_element_by_link_text("ÖĞRENCİ BİLGİ SİSTEMİ").click()
chrome_browser.find_element_by_id("Username").send_keys("")
chrome_browser.find_element_by_id("Password").send_keys("")
chrome_browser.find_element_by_name(
    "button").click()
chrome_browser.find_element_by_partial_link_text("Diğer İşlemler").click()
chrome_browser.find_element_by_partial_link_text("Seçilen Dersler").click()

sleep(8)
chrome_browser.find_element_by_partial_link_text("Transkript").click()

body = chrome_browser.find_element_by_css_selector('body')
body.send_keys(Keys.END)
sleep(8)
# open new blank tab
chrome_browser.execute_script("window.open();")

# switch to the new window which is second in window_handles array
chrome_browser.switch_to_window(chrome_browser.window_handles[1])
chrome_browser.get("https://duckduckgo.com")