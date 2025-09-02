# TODO: 사용자 모듈 import


# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.


from funcs import pan, ave, max, min

def test_pan():
    assert pan(2) == "evennum"
    assert pan(3) == "oddnum"

def test_ave():
    assert ave([1, 2, 3]) == 2
    assert ave([10, 20]) == 15

def test_max():
    assert max([1, 2, 3]) == 3
    assert max([-5, -1, -10]) == -1

def test_min():
    assert min([1, 2, 3]) == 1
    assert min([-5, -1, -10]) == -10
