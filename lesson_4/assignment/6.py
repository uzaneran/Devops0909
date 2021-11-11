from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chrome.get("https://translate.google.com/")
elem_by_class = chrome.find_element(By.CLASS_NAME, "er8xn")
print("elem_by_class", elem_by_class)
elem_by_tag = chrome.find_element(By.TAG_NAME, "textarea")
print("elem_by_tag", elem_by_tag)
elem_by_xpath = chrome.find_element(By.CSS_SELECTOR, "textarea[jsname='BJE2fc']")
print("elem_by_xpath", elem_by_xpath)
