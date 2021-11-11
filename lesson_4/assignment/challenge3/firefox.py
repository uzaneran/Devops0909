from selenium import webdriver
from selenium.webdriver.firefox.options import Options


firefox_options = Options()
firefox_options.add_argument("--disable-extensions")
geckodriver = webdriver.Firefox(executable_path="/Users/student/Downloads/geckodriver", options=firefox_options)
geckodriver.get("http://www.ynet.co.il")
