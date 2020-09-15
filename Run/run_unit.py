#coding=utf-8
import os
import HTMLTestRunner
import unittest
import time
from Run import run_main


# class Run_Unit(unittest.TestCase):

    # def setUp(self):
    #     print("预置条件")
    #
    # def testcase01(self):
    #     run_main.RunCase().run()
    #
    # def testcase02(self):
    #     pass
    #
    # def testcase03(self):
    #     pass
    #
    # def tearDown(self):
    #     print("后置条件")

def add_case():
    case_path = os.path.join(os.getcwd())
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_run_*.py')
    return discover

if __name__ == '__main__':
    #suite=unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(Run_Unit('testcase01'))
    # print(suite)
    with open(os.path.join(os.path.dirname(os.getcwd()),"report\\{}.html").format(time.strftime("%Y_%m_%H_%M_%S")),'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="接口测试报告", description="this is test")
        runner.run(add_case())
    f.close()