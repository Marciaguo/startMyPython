import pytest


# def setup_module():
#     print("模块级别的setup")
# def teardown_module():
#     print("模块级别的teardown")
# #类外边的定义是函数
# def func(i):
#     return i+2
# def test_answer():
#     assert func(3)==5
@pytest.fixture()
def login():
    print("登录")
    return "tom"

class TestDemo:
    # def setup_method(self):
    #     print("函数级别setup")
    # def teardown_method(self):
    #     print("函数级别teardown")
    # def setup_class(self):
    #     print("setup 类级别 初始化")
    # def teardown_class(self):
    #     print("teardown 类级别 资源销毁")
    def test_a(self,login):
        print(f"aa,用户名{login}")
    def test_b(self,login):
        print(f"bb,用户名{login}")
        # raise NameError
class TestDemo2:
    # def setup_method(self):
    #     print("函数级别setup")
    # def teardown_method(self):
    #     print("函数级别teardown")
    # def setup_class(self):
    #     print("setup 类级别 初始化")
    # def teardown_class(self):
    #     print("teardown 类级别 资源销毁")
    def test_a(self,login):
        print(f"aa,用户名{login}")