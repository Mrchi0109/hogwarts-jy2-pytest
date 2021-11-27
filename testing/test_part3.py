"""
__author__ = 'hogwarts_xixi'
"""
import logging

import allure

"""
定义执行顺序，顺序为
    安装 插件 ：pip install pytest-ordering
    最终顺序为：add 用例 （P1_1>P1_2>P0）> div 用例 >  add 用例（P2）
生成测试报告
    安装allure,（先安装java1.8）
    安装插件： pip install allure-pytest
    为测试类和方法添加分类
    测试用例中添加日志，测试步骤，及图片
"""

"""
__author__ = 'hogwarts_xixi'
"""
import yaml

# 测试类
# 命名规则：文件以test_开头，类以Test开头，方法以test_开头
import pytest
from pythonsource.calculator import Calculator


# get_data()提供测试数据
def get_data():
    # return [[1,1,2],[-0.01, 0.02,0.01],[10, 0.02,10.02]]
    # 数据文件 里的测试数据读取出来，
    with open("./datas/data.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
    return result


# 为用例添加大的类别
@allure.feature("计算器")
class TestCalc:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect", get_data().get("add_normal"), ids=["int_int", "float_float", "int_float"])
    @pytest.mark.run(order=3)
    @allure.story("相加功能")
    def test_add_PO(self, a, b, expect):
        """"
        1. 第一个数输入 a ：1
        2. 第二个数输入 b ：1
        3. 预期结果为 expect：2
        """
        with allure.step("步骤1：实例化一个calc对象"):
            # 定义一个对象calc
            logging.info("实例化一个calc对象")
            calc = Calculator()
        with allure.step("步骤2：完成相加操作"):
            # result 为实际结果
            logging.info("完成相加操作")
            result = calc.add(a, b)
        with allure.step("步骤3：实现断言"):
            logging.info("实现断言")
            # result 要与预期结果对比
            assert result == expect

        allure.attach.file("/Users/juanxu/Downloads/logo帽子.jpg", "截图",
                           allure.attachment_type.JPG, ".jpg")

    @pytest.mark.run(order=1)
    @allure.story("相加功能")
    def test_add_P1_1(self):
        print("测试相加P11用例")

    @pytest.mark.run(order=-1)
    @allure.story("相加功能")
    def test_add_P2(self):
        print("测试相加P2用例")

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", [["文", 0.3, "TypeError"]])
    @allure.story("相加功能")
    def test_add_error_P1_2(self, a, b, expect):
        """
        1. 第一个数输入：文
        2. 第二个数输入：9.3
        3. 预期结果：TypeError
        :return:
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        with pytest.raises(eval(expect)) as e:
            result = calc.add(a, b)
        assert e.typename == expect

    @pytest.mark.run(order=4)
    @allure.story("相除功能")
    def test_div(self):
        print("测试相除用例")
