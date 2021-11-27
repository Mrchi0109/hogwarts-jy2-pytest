"""
__author__ = 'hogwarts_xixi'
"""
import yaml

"""
__author__ = 'hogwarts_xixi'
"""
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


class TestCalc:
    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,expect", get_data().get("add_normal"), ids=["int_int", "float_float", "int_float"])
    def test_add(self, a, b, expect):
        """"
        1. 第一个数输入 a ：1
        2. 第二个数输入 b ：1
        3. 预期结果为 expect：2
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        result = calc.add(a, b)
        # result 要与预期结果对比
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [["文", 0.3, "TypeError"]])
    def test_add_error(self, a, b, expect):
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
