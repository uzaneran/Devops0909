from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chrome.get("https://github.com/")
search_input = chrome.find_element(By.CSS_SELECTOR, "input.form-control.input-sm.header-search-input.jump-to-field.js-jump-to-field.js-site-search-focus")
search_input.send_keys("Selenium")
search_input.submit()

