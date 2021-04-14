import unittest
import requests

class MyTestCase(unittest.TestCase):
    url = 'http://httpbin.org'

    def test_get(self):
        url =self.url+'/get'
        res = requests.get(url)
        assert res.status_code==200
        # 获取响应内容
        print(res.text)
    def test_post(self):
        url = self.url+'/get'
        res = requests.post(url)

    def test_get1(self):
        url = self.url+'/get'+'?name=zhangsan&age=18'
        res = requests.post(url)
        print(res.url)
        # print(res.status_code)
        # 获取响应内容
        print(res.text)

    def test_get2(self):
        url = self.url+'/get'
        param = {'name':'zhangsan','age':'18'}
        res = requests.get(url,param)
        print(res.text)
        print(res.json()["headers"]["Host"])

        # 获取响应内容
        # print(res.text)
if __name__ == '__main__':
    unittest.main()
