from selenium import webdriver
import datetime

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

AmazonLink = "http://www.amazon.co.uk"
driver.get(AmazonLink)

time = datetime.datetime.now()
#driver.save_screenshot("C:\\Users\\aahme\\Desktop\\homepage.png") Will save in intended location

#driver.get_screenshot_as_file # supports png does the same


