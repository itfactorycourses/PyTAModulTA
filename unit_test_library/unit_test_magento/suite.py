import unittest

import HtmlTestRunner

from test_login import Test_Login
from test_search import Test_Search

class TestSuite(unittest.TestCase):

    def test_suite(self):
        # test_list este un obiect instantiat din clasa TestSuite()
        test_list = unittest.TestSuite()
        test_list.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test_Search),
                            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Login)
                            ])

        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title="Test execution report",
                                               report_name="Test results")
        # daca vom rula suita cu mai multe clase de test, ni se va genera un singur raport
        # pentru toate, nu un raport per clasa, pentru ca am specificat combine_reports=True
        runner.run(test_list)
