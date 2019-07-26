import unittest

#setup - before each test method
#teardown - after each test method
#setupclass - once before methods started
#teardownclass - after methods finished
#setupmodule
#tearDownModule

def setUpModule():
    print("Before module initiates the class")

class Test1(unittest.TestCase):

    def setUpClass(cls):
        print("Opening application/setting up class")
    @classmethod
    def setUp(self):
        print("This is the setup method")

    def test_search(self):
        print("This is a search text")

    def test_advancedsearch(self):
        print("Advanced search")

    def tearDown(self):
        print("This is a teardown method")

    def tearDownClass(cls):
        print("Close application/tearing down class")


def tearDownModule():
    print("Tearing don module")
if __name__ == "__main__":
    unittest.main()
