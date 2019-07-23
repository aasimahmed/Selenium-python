from selenium import webdriver
from selenium.webdriver.common.by import By

#Intialise options for firefox

firefoxProfile = webdriver.FirefoxProfile()

# Firefox profile has acceptable preferences to add to it.
firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf") #MIME types - does not ask for preference updates
firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
firefoxProfile.set_preference("browser.download.dir", "C:\\Downloadedfiles")
firefoxProfile.set_preference("browser.download.folderList",2)
firefoxProfile.set_preference("pdfjs.disabled", True)


driver = webdriver.Firefox(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\geckodriver.exe", firefox_profile=firefoxProfile)


driver.get("http://demo.automationtesting.in/FileDownload.html")

pdfTextBox = driver.find_element(By.ID, "pdfbox")
pdfTextBox.send_keys("Testing")

generatePdfButton = driver.find_element(By.ID, "createPdf").click()
#Below button should now be visible
downloadPdfButton = driver.find_element(By.ID, "pdf-link-to-download").click()

driver.quit()
