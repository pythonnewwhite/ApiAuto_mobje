import pytest
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]
@pytest.mark.parametrize('a,b',data_1)
class Test_错误密码:

    def test_C001001(self,a,b):
        print('\n用例C001001',a,b)
        assert a == b

    def test_C001002(self):
        print('\n用例C001002')
        assert 2 == 2

    def test_C001003(self):
        print('\n用例C001003')
        assert 3 == 2

if __name__ == '__main__':
    pytest.main(["-s","Pytest01.py",'--html=./Report/report.html'])