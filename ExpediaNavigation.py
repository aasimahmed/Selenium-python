from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


expediaURL = "https://www.expedia.com"
driver = webdriver.Chrome("C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")
wait = WebDriverWait(driver, 10)

driver.get(expediaURL)
driver.maximize_window()

driver.implicitly_wait(5)

flightsButton = driver.find_element(By.ID, "tab-flight-tab-hp")
flightsButton.click()

driver.implicitly_wait(5)

flyingFromField = driver.find_element(By.ID, "flight-origin-hp-flight")
flyingToField = driver.find_element(By.ID, "flight-destination-hp-flight")
startDateField = driver.find_element(By.ID, "flight-departing-hp-flight")
endDateField = driver.find_element(By.ID, "flight-returning-hp-flight")

flyingFromField.clear()
flyingFromField.send_keys("Bristol")

flyingToField.clear()
flyingToField.send_keys("NYC")

driver.implicitly_wait(2)

startDateField.click()
startDateField.clear()
startDateField.send_keys("10/10/2020")

driver.implicitly_wait(2)
endDateField.click()

searchSubmitButton = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='btn-primary btn-action gcw-submit']")))
searchSubmitButton.click()

driver.quit()