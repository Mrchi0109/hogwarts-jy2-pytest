"""
__author__ = 'hogwarts_xixi'
"""

# 测试类
# 命名规则：文件以test_开头，类以Test开头，方法以test_开头
import pytest

from pythonsource.calculator import Calculator


class TestCalc:
    def setup(self):
        # 每条用例执行之前需要执行setup
        print("开始计算")

    def teardown(self):
        # 每条用例执行之后需要执行teardown -- 方法级别
        print("结束计算")

    def teardown_class(self):
        # 这个类的所有用例执行之后执行teardown_class --- 类级别
        # 类级别：整个类只执行一次
        print("结束测试")

    @pytest.mark.add
    def test_add(self):
        """"
        1. 第一个数输入：1
        2. 第二个数输入：1
        3. 预期结果为：2
        """

        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        result = calc.add(1, 1)
        # result 要与预期结果对比
        assert result == 2

    @pytest.mark.add
    def test_add1(self):
        """
        1. 第一个数输入：-0.01
        2. 第二个数输入：0.02
        3. 预期结果为：0.01
        :return:
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        result = calc.add(-0.01, 0.02)
        # result 要与预期结果对比
        assert result == 0.01

    @pytest.mark.add
    def test_add2(self):
        """
        1. 第一个数输入：10
        2. 第二个数输入：0.02
        3. 预期结果为：10.02
        :return:
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        result = calc.add(10, 0.02)
        # result 要与预期结果对比
        assert result == 10.02

    def test_add_error(self):
        """
        1. 第一个数输入：文
        2. 第二个数输入：9.3
        3. 预期结果：TypeError
        :return:
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        with pytest.raises(TypeError) as e:
            result = calc.add("文", 0.3)
        assert e.typename == "TypeError"

    @pytest.mark.div
    def test_div(self):
        pass
