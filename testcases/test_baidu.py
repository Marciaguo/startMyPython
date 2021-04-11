import allure
import pytest


@allure.feature("搜索类")
class TestSearchDemo:
    @allure.story("搜索中文")
    @pytest.mark.parametrize("searchKey", ["android", "连衣裙", "@1￥"])
    def test_search(self, searchKey):
        with allure.step("第一步：打开搜索页面"):
            print("第一步：打开搜索页面")
        with allure.step("第二步：点击搜索框"):
            print("第二步：点击搜索框")
        with allure.step("第三步：输入搜索词"):
            print(f"第三步：输入搜索词{searchKey}")

    @allure.story("搜索英文")
    def test_search1(self):
        print("这是一个搜索方法1:英文")
        raise NameError

    @allure.story("搜索特殊字符")
    def test_search2(self):
        print("这是一个搜索方法2:特殊字符")


@allure.feature("登录类")
class TestLoginDemo:
    @allure.story("login1")
    def test_login1(self):
        allure.attach.file('/Users/guoshanyi/Desktop/屏幕快照\ 2021-04-08\ 下午12.36.58.png',
                      attachment_type=allure.attachment_type.PNG)
        print("login1")

    @allure.story("login2")
    def test_login2(self):
        print("login2")
