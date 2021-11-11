from selenium import webdriver


chrome = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chrome.get("https://google.com")
print("cookies", chrome.get_cookies())
chrome.delete_all_cookies()
print("cookies", chrome.get_cookies())
