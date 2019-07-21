from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

linkElements = driver.find_elements(By.TAG_NAME, "a")

print("number of links is " + len(linkElements)) # total links

for link in linkElements:
    print(link.text)


driver.find_element(By.LINK_TEXT,"REGISTER").click() #To find a link by text value and click, Case sensi

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click() #Part of complete link text

driver.quit()