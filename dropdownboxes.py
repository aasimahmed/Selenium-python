from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

driver.implicitly_wait(5)
drp = driver. find_element_by_id("RESULT_RadioButton-9")



element = Select(drp)

element.select_by_index(2) #Select by indes of dropdown
element.select_by_value("Radio-0") #Select by value of the html value='sasaS'
element.select_by_visible_text("Morning") #Text inside of option

alloptionsdropdown = element.options

print(len(alloptionsdropdown))

for option in alloptionsdropdown:
    print(option.text)