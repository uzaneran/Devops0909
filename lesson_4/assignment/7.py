from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chrome.get("https://www.facebook.com/")
email_input = chrome.find_element(By.ID, "email")
password_input = chrome.find_element(By.ID, "pass")
submit_button = chrome.find_element(By.CSS_SELECTOR, "button[name='login']")
email_input.send_keys("foo@test.com")
password_input.send_keys("bar")
submit_button.click()
