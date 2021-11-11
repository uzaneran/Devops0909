from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chrome.get("https://www.youtube.com/")
input_element = chrome.find_element(By.CSS_SELECTOR, "input#search")
input_element.send_keys("tornado of souls")
chrome.find_element(By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()
