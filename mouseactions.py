from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")

usernameField = driver.find_element(By.ID, "txtUsername")
passwordField = driver.find_element(By.ID, "txtPassword")
loginButton = driver.find_element()

usernameField.clear()
usernameField.send_keys("Admin")

passwordField.clear()
passwordField.send_keys("admin123")

actions= ActionChains(driver)
element1 = driver.find_element("")
#Movecursor to an element then click
actions.move_to_element(element1).click().perform() #performs actions built up in action obj

#Doubleclick
actions2 = ActionChains(driver)
actions2.double_click(element1).perform()

#Rightclick
action3 = ActionChains(driver)
action3.context_click(element1).perform()

#DragandDrog
element2 = driver.find_element(By.ID, "examp")
action4 = ActionChains(driver)
action4.drag_and_drop(element1, element2) # source element to target element

driver.quit()
