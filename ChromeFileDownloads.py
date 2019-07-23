from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.options import Options

#Before we create the driver we need to configure options for the driver instance

chromeOptions = Options()

chromeOptions.add_experimental_option("prefs" ,{"download.default_directory": "C:\\DownloadedFiles"})
#All browsers have external apis provided which selenium interacts with through driver.
driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe", options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Chrome browser has default download location
#downloadButton = driver.find_element(By.XPATH("//*[@href='https://github.com//sakinala/AutomationTesting/raw/master/samplefile.pdf']"))

#downloadButton.click()

pdfTextBox = driver.find_element(By.ID, "pdfbox")
pdfTextBox.send_keys("Testing")

generatePdfButton = driver.find_element(By.ID, "createPdf").click()
#Below button should now be visible
downloadPdfButton = driver.find_element(By.ID, "pdf-link-to-download").click()