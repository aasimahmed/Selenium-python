from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromePath = "C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromePath)

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
driver.get("http:www.google.co.uk")

driver.back() #BACK
time.sleep(5)
print(driver.title)
    

driver.forward() #FOWRWARD
time.sleep(5)
print(driver.title)

driver.quit()