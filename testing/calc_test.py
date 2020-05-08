import allure
import pytest

from calc_need.calc import Calc


@allure.feature("计算器")
class TestCalc:
    @allure.story('加法')
    @pytest.mark.parametrize('a, b, c', [(0, 0, 0), (0, 11, 11), (9, 9, 18), (0.1, 0.34, 0.44)])
    def test_add(self, a, b, c):
        self.calc = Calc()
        result = self.calc.add(a, b)
        assert result == c

    @allure.story('除法')
    @pytest.mark.parametrize('a, b, c', [(0, 1, 0), (4, 4, 1), (9, 4, 2.25), (0, 0, 0), (0.9, 0.3, 3)])
    def test_div(self, a, b, c):
        self.calc = Calc()
        result = self.calc.div(a, b)
        assert result == c

    @allure.story('减法')
    @pytest.mark.parametrize('a, b, c', [(0, 11, -11), (9, 9, 0), (31, 0, 31), (0.4, 0.1, 0.3)])
    def test_sub(self, a, b, c):
        self.calc = Calc()
        result = self.calc.sub(a, b)
        assert result == c

    @allure.story('乘法')
    @pytest.mark.parametrize('a, b, c', [(7, 1, 7), (0, 11, 0), (9, 9, 81), (0.1, 0.5, 0.05)])
    def test_mul(self, a, b, c):
        self.calc = Calc()
        result = self.calc.mul(a, b)
        assert result == c