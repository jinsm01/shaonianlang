import pytest
from calc_need.calc import Calc


@pytest.fixture(scope='module')
def sl_calc():
    calc = Calc()
    return calc
