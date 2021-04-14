import requests


class TestRequest:
    def test_demo(self):
        params = {'q':'python','cat':'1001'}
        r = requests.get('https://www.douban.com/search',params)
        print(r.url)
        # print(r.json())
