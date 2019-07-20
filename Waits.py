from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromePath = "C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromePath)


driver.get("http://newtours.demoaut.com")

driver.implicitly_wait(10) # maximum wait for 10 seconds

assert "Welcome: Mercury Tours" in driver.title

usernameEle = driver.find_element_by_name("userName")
passwordEle = driver.find_element_by_name("password")
loginButton = driver.find_element_by_name("login")

usernameEle.send_keys("mercury")
passwordEle.send_keys("mercury")
loginButton.click()

driver.quit()
