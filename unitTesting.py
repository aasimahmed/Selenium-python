import unittest

class Test(unittest.TestCase): #extendsfromalways
    def test_firstTest(self):
        print("This is my first unit test case")

if __name__ =="__main__":
    unittest.main()