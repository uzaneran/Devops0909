from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_browser = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver", options=chrome_options)
chrome_browser.get("https://google.com")


# firefox
firefox_options = Options()
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument('headless')
firefox_driver = webdriver.Firefox(executable_path="/Users/student/Downloads/geckodriver", options=firefox_options)
firefox_driver.get("http://www.ynet.co.il")

# microsoft edge
edge_options = Options()
edge_options.add_argument("--disable-extensions")
edge_browser = webdriver.Edge(executable_path="/Users/student/Downloads/edgedriver_mac64/msedgedriver", options=edge_options)
edge_browser.get("http://www.ynet.co.il")
