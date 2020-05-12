import allure
import pytest
from calc_need.calc import Calc
from test_data.data_logic import Yaml_data


@allure.feature("计算器")
class TestCalc:
    yaml_data_add = Yaml_data('../test_data/calc_test_add.yaml')
    yaml_data_sub = Yaml_data('../test_data/calc_test_sub.yaml')
    yaml_data_mul = Yaml_data('../test_data/calc_test_mul.yaml')
    yaml_data_div = Yaml_data('../test_data/calc_test_div.yaml')

    @pytest.fixture()
    @allure.step('实例化Calc')
    def test_sl_calc(self):
        self.calc = Calc()

    @allure.story('加法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_add.data)
    def test_add(self, test_sl_calc, num_one, num_two, expected):
        assert expected == self.calc.add(num_one, num_two)

    @pytest.mark.run(order=3)
    @allure.story('除法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_div.data)
    def test_div(self, test_sl_calc, num_one, num_two, expected):
        assert expected == self.calc.div(num_one, num_two)

    @pytest.mark.run(order=1)
    @allure.story('减法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_sub.data)
    def test_sub(self, test_sl_calc, num_one, num_two, expected):
        assert expected == self.calc.sub(num_one, num_two)

    @allure.story('乘法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_mul.data)
    def test_mul(self, test_sl_calc, num_one, num_two, expected):
        assert expected == self.calc.mul(num_one, num_two)
