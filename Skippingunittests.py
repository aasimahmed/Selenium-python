import unittest

#Add unittest.Skiptest to unit test decorator
#Add unittest.skip("message") to provide a loggable message with reason
#add unittest.skipif(condition, "message") - skip conditionally the test

class AppTesting(unittest.TestCase):
    @unittest.skip("Reason I am skipping this because its not needed")
    def test_search(self):
        print("search_test")
    @unittest.SkipTest
    def advanced_search(self):
        print("Advanced_test")
    @unittest.skipIf(1==1, "if 1 is equal to 1 skip it")
    def complex_search(self):
        print("AdvancedSearch")

if __name__ == '__main__':
        unittest.main()