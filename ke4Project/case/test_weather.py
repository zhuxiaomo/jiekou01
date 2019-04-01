# coding:utf-8
import requests
import unittest

class TestWeather(unittest.TestCase):

    def test_weather(self):
        url = "http://v.juhe.cn/weather/index"

        par = {
            "cityname": "上海",  # 城市名或城市ID，如："苏州"，需要utf8 urlencode
            "dtype": "json",     # 返回数据格式：json或xml,默认json
            "format": "1",       # 未来7天预报(future)两种返回格式，1或2，默认1
            # key是我个人申请的，群内学习使用，勿乱发
            "key": "80b4d4e1d870d257d3344fcf2d08f64a"
        }

        r = requests.get(url, params=par)
        print(r.json())
        result = r.json()["reason"]
        print(result)
        self.assertEqual("successed!", result)

    def test_weather_appkey_error(self):
        url = "http://v.juhe.cn/weather/index"

        par = {
            "cityname": "上海",  # 城市名或城市ID，如："苏州"，需要utf8 urlencode
            "dtype": "json",     # 返回数据格式：json或xml,默认json
            "format": "1",       # 未来7天预报(future)两种返回格式，1或2，默认1
            # key是我个人申请的，群内学习使用，勿乱发
            "key": "1111111111111111111"
        }

        r = requests.get(url, params=par)
        print(r.json())
        result = r.json()["reason"]
        print(result)
        self.assertEqual("错误的请求KEY!", result)

    def test_03(self):
        print111
