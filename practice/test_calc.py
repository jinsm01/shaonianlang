import unittest
import sys

sys.path.append('..')

from calc_need.calc import Calc

print(sys.path)

'''
命令行运行时招不到python模块，看路径少了shaonianlang的所以需要手动添加
rint(sys.path)
from calc_need.calc import Calc
'''


class TestCacl(unittest.TestCase):

    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        self.assertEqual(3, result)
        print(result)


# unittest.main()
