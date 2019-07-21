from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_window_handle) #hash for current window

windows = driver.window_handles #get all windows of open browser
for window in windows:
    driver.switch_to_window(window)
    print(driver.title) #print current title of driver