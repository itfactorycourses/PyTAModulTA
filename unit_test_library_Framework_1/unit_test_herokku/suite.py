import unittest
import HtmlTestRunner
from test_alerts import Test_Alerts

class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_list = unittest.TestSuite()
        test_list.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test_Alerts)])

        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True,
                                               report_title="Test execution report",
                                               report_name="Test results")
        runner.run(test_list)
