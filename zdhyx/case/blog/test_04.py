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
        print("test_04用例01")
    def test02(self):
        print("test_04用例02")
    def test03(self):
        print("test_04用例03")
if __name__ == "__main__":
    unittest.main
