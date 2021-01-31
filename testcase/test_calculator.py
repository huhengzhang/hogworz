import pytest
import sys

sys.path.append('..')

from calculator.calculator import Calculator

from testcase.getYaml import getYmal

data = getYmal()

addData = data['add']
idsAdd = data['idsAdd']

divData = data['div']
idsDiv = data['idsDiv']


class TestCalculator(object):
    def setup(self):
        print('开始计算')
        self.cal = Calculator()

    def teardown(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b,result', addData,ids=idsAdd)
    @pytest.mark.add
    def test_add(self, a, b, result):
        actual = self.cal.add(a, b)
        assert result == actual

    @pytest.mark.parametrize('a,b,result', divData, ids=idsDiv)
    @pytest.mark.div
    def test_div(self, a, b, result):
        actual = self.cal.div(a, b)
        assert result == actual


