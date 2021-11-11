from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver", options=chrome_options)

browser.get("https://google.com")
