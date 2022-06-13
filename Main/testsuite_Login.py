import unittest
from Test.loginTest import LoginTestInChrome

# get all tests from SearchText and HomePageTest class
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTestInChrome)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([login_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)