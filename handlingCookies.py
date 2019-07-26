from selenium import webdriver
import time

AmazonLink = "https://www.amazon.co.uk"
driver = webdriver.Chrome(executable_path="C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe")

driver.get(AmazonLink)

cookies = driver.get_cookies() #gets all the cookies from webpage and prints them out

for cookie in cookies:
    print(cookie)

cookie2 = {'name': 'MyCookie', 'value': '1234567890'}

driver.add_cookie(cookie2) #here we can add the cookie to the browser

cookies = driver.get_cookies()
print(len(cookies))

driver.delete_cookie('MyCookie') #pass in name of cookie to delete

time.sleep(3)
cookies=driver.get_cookies()
print(len(cookies))

driver.delete_all_cookies()
time.sleep(2)
print(len(driver.get_cookies()))
driver.quit()