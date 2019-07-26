import unittest
from selenium import webdriver

#assert equal - compares given two parameter
#assertNotEqual
#AssertTrue
#AssertFalse
#Assert is not none
#Assertnone
#assertIn
#assertNotIn - Useful when asserting if values are in a dictionary/list or not

#Assert greater, greaterequal, assertless, assert less/equal

driverpath = "C:\\Users\\aahme\\Desktop\\webdriver_executables\\chromedriver.exe"
googleLink = "http://www.google.co.uk"

class Assertions(unittest.TestCase):
    def testname(self):
        driver = webdriver.Chrome(executable_path=driverpath)
        driver.get(googleLink)
        self.assertEqual("Google", driver.title)
        driver.quit()
    def testname2(self):
        driver = webdriver.Chrome(executable_path=driverpath)
        driver.get(googleLink)
        self.assertNotEqual(1, 2, "They should not be true")
        driver.quit()


if __name__ == "__main__":
    unittest.main()
