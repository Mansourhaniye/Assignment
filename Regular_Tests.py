from MagicList import MagicList
import pytest
from pytest import raises


def test1():
    _list = MagicList()
    _list[0] = 5
    assert _list[0] == 5

def test2():
    _list = MagicList()
    _list[-1] = 5


def test3():
    _list = MagicList()
    for i in range(5):
        assert _list == list(range(i))
        _list[-1] = i


@pytest.mark.parametrize("i", range(2, 6))
def test4(i):
    _list = MagicList()
    with raises(IndexError):
        _list[i] = 5

@pytest.mark.parametrize("i", range(2, 6))
def test5(i: int):
    _list = MagicList()
    with raises(IndexError):
        _list[-i] = 5

if __name__ == '__main__':
    pytest.main()