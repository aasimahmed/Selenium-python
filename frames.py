from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

#We have to go to main page to frame
driver.switch_to.frame("packageListFrame") #name of frame
driver.switch_to.default_content()
driver.switch_to_frame("packageFrame") #second frame id