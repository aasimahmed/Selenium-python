from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com")

#Alerts have two buttons - ok or cancel

alertbox = driver.find_element(By.XPATH, "//*[@onclick='myFunction()']")
alertbox.click()

time.sleep(3)

#driver.switch_to_alert().accept() accept the alert
#driver.switch_to_alert().dismiss() decline the alert