from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromePath = "C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromePath)

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

print(driver.title) # get title
print(driver.current_url) #get currenturl
print(driver.page_source) # prints pagesource

driver.find_element_by_xpath("//*[@class='btn btn-info']").click()

time.sleep(5)
print(driver.current_url) #prints focused driver window handle

#driver.close() only closes focused browser
#driver.quit() closes all browsers assoc with object



driver.quit()

