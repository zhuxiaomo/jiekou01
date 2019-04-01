# coding:utf-8
import requests
import unittest

class TestQQ(unittest.TestCase):
    u''''测试QQ功能'''


    def test_qq(self):
        u'''测试qq号码，appkey是正确的'''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        # 参数
        par = {
            "key": "8dbee1fcd8627fb6699bce7b986adc45",
            "qq": "283340479"
        }
        # post请求
        r2 = requests.post(url, params=par)
        print(r2.text)  # 获取的返回结果
        result = r2.json()["reason"]
        print(result)
        # 断言
        self.assertTrue("success11"==result)
        self.assertTrue("success" in r2.text)
        self.assertIn("success", r2.text)
        self.assertEqual("success", result, msg="失败的时候打印这里")

    def test_qq_appkey_error(self):
        u'''测试qq号码，appkey是错误的'''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        # 参数
        par = {
            "key": "111111111111111111111",
            "qq": "283340479"
        }
        # post请求
        r2 = requests.post(url, params=par)
        print(r2.text)  # 获取的返回结果
        result = r2.json()["reason"]
        print(result)
        self.assertEqual("KEY ERROR!", result)

if __name__ == "__main__":
    unittest.main()








