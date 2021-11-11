from selenium import webdriver
from selenium.webdriver.edge.options import Options


edge_options = Options()
edge_options.add_argument("--disable-extensions")
edgedriver = webdriver.Edge(executable_path="/Users/student/Downloads/edgedriver_mac64/msedgedriver", options=edge_options)
edgedriver.get("http://www.ynet.co.il")
