from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("")
element = driver.find_element(By.ID("element1"))

#Scroll by pixel amount
driver.execute_script("window.scrollBy(0,500)","")
driver.execute_script("arguements[0].scrollIntoView();", element) # keep scrolling til element in view

#Scroll entire length of document
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")