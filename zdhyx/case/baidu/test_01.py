#coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
    def test01(self):
        '''登录测试用例'''
        print("test_01用例01")
    def test02(self):
        '''登录测试用例'''
        print("test_01用例02")
    def test03(self):
        '''登录测试用例'''
        print("test_01用例03")
if __name__ == "__main__":
    unittest.main
