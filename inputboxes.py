from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

driver.implicitly_wait(5)
inputboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='text']")
inputboxesLength = len(inputboxes) #find all elements that are input boxes


for x in range(0,inputboxesLength-1):
    print(inputboxes[x].is_enabled())

driver.quit()