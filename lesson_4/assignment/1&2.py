from selenium import webdriver

geckodriver = webdriver.Firefox(executable_path="/Users/student/Downloads/geckodriver")
geckodriver.get("http://www.ynet.co.il")

chromedriver = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
chromedriver.get("http://www.walla.co.il")

title = "וואלה! - האתר המוביל בישראל - עדכונים מסביב לשעון"
chromedriver.refresh()
website_name = chromedriver.title
assert title == website_name
