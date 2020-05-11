import allure
import pytest

from calc_need import calc
from calc_need.calc import Calc


@pytest.fixture()
@allure.step('实例化Calc')
def test_sl_calc(self):
    self.calc = Calc()
