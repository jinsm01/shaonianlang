import allure
import pytest
import yaml
from test_data.data_logic import Yaml_data

@allure.feature("计算器")
class TestCalc:
    yaml_data_add = Yaml_data('../test_data/calc_test_add.yaml')
    yaml_data_sub = Yaml_data('../test_data/calc_test_sub.yaml')
    yaml_data_mul = Yaml_data('../test_data/calc_test_mul.yaml')
    yaml_data_div = Yaml_data('../test_data/calc_test_div.yaml')

    def steps(self):
        with open('../test_data/stepdata.yaml') as f:
            return yaml.safe_load(f)

    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_add.data)
    def calc_add(self, sl_calc, num_one, num_two, expected):
        for step1 in TestCalc.steps(self):
            if step1 == 'calc_add':
                assert expected == sl_calc.add(num_one, num_two)

    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_div.data)
    def calc_div(self, sl_calc, num_one, num_two, expected):
        for step1 in TestCalc.steps(self):
            if step1 == 'calc_div':
                assert expected == sl_calc.div(num_one, num_two)

    @allure.story('减法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_sub.data)
    def calc_sub(self, sl_calc, num_one, num_two, expected):
        assert expected == sl_calc.sub(num_one, num_two)

    @allure.story('乘法')
    @pytest.mark.parametrize('num_one, num_two, expected', yaml_data_mul.data)
    def calc_mul(self, sl_calc, num_one, num_two, expected):
        assert expected == sl_calc.mul(num_one, num_two)
