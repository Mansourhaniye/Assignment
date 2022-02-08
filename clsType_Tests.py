from MagicList import MagicList
import pytest
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1

def test1():
    _list = MagicList(cls_type=Person)
    _list[0].age = 5
    assert _list[0] == Person(age=5)

def test2():
    _list = MagicList(cls_type=Person)
    with pytest.raises(IndexError):
        _list[1].age = 5

if __name__ == '__main__':
    pytest.main()