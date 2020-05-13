import pytest
from calc_need.calc import Calc


@pytest.fixture(scope='module')
def sl_calc():
    calc = Calc()
    return calc


def pytest_configure(config):
    marker_list = ["add", "sub", 'div', 'mul']
    for markers in marker_list:
        config.addinivalue_line("markers", markers)


# 自动添加标签
def pytest_collection_modifyitems(items: list):
    print(items)
    print(type(items))
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)

    # items.reverse()
