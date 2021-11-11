from selenium import webdriver
from time import sleep


my_driver = webdriver.Chrome(executable_path="/Users/student/Downloads/chromedriver")
my_driver.get("file:///Users/student/PycharmProjects/tip_calc/index.html")
# find element by ID:
my_driver.find_element_by_id("billamt").send_keys("100")

# full path for XPath:
# my_driver.find_element_by_xpath("s/html/body/div/div[1&2]/form/p[4]/select/option[2]").click()

# realative XPath
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element_by_xpath('//*[@id="musicQual"]/option[6]').click()


my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("calculate").click()
expected = "9.00"
actual = my_driver.find_element_by_id("tip").text
if expected == actual:
    print("All good!")


# sleep(5)
# my_driver.refresh()
# my_driver.back()
