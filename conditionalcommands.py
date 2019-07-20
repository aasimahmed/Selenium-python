from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromePath = "C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromePath)

driver.get("http://newtours.demoaut.com")

usernameEle = driver.find_element_by_name("userName")
passwordEle = driver.find_element_by_name("password")
loginButton = driver.find_element_by_name("login")


print(usernameEle.is_displayed())
print(usernameEle.is_enabled())

print(passwordEle.is_enabled())
print("Password login is"  + ("displayed" if passwordEle.is_displayed() else "not displayed"))

usernameEle.send_keys("mercury")
passwordEle.send_keys("mercury")

loginButton.click()
time.sleep(10)
if driver.find_element_by_name("findflight").is_displayed():
    print("Login validated")
    roundTripRadioButton = driver.find_elements_by_css_selector("input[value='roundtrip']")[0]
    print("Status of Round trip button is " + "selected" if roundTripRadioButton.is_selected() else "not selected") # print status of radio button that should be selected

    onewayRadioButton = driver.find_elements_by_css_selector("input[value='oneway'")[0]
    print("Status of One way button is " + "not selected" if onewayRadioButton.is_selected() else "selected")

driver.quit()