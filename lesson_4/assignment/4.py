from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chrome.get("https://translate.google.co.il/?hl=iw&sl=iw&tl=en&op=translate")
textarea = chrome.find_element(By.CSS_SELECTOR, "textarea[jsname='BJE2fc']")
textarea.send_keys("בואי נלך לים")
