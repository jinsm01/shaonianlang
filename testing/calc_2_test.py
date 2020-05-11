import allure
import pytest

from test_data.data_logic import Yaml_data


@allure.feature("计算器")
class TestCalc:
    yaml_data_add = Yaml_data('../test_data/calc_test_add.yaml')
    yaml_data_sub = Yaml_data('../test_data/calc_test_sub.yaml')
    yaml_data_mul = Yaml_data('../test_data/calc_test_mul.yaml')
    yaml_data_div = Yaml_data('../test_data/calc_test_div.yaml')

    @allure.story('除法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_div.data)
    def test_div(self, sl_calc, num_one, num_two, expected):
        assert expected == sl_calc.div(num_one, num_two)

    @allure.story('加法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_add.data)
    def test_add(self, sl_calc, num_one, num_two, expected):
        assert expected == sl_calc.add(num_one, num_two)

    @allure.story('减法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_sub.data)
    def test_sub(self, sl_calc, num_one, num_two, expected):
        assert expected == sl_calc.sub(num_one, num_two)

    @allure.story('乘法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_mul.data)
    def test_mul(self, sl_calc, num_one, num_two, expected):
        assert expected == sl_calc.mul(num_one, num_two)
