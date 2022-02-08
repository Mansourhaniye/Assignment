from collections import UserList
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class MagicList(UserList):
    def __init__(self, cls_type=None):
        super().__init__()
        self._cls_type = cls_type

    def __getitem__(self, _ind):
        _size = len(self.data)
        if _ind == -1 or _size == _ind:
            self.data.append(self._cls_type())
        return super().__getitem__(_ind)

    def __setitem__(self, _ind, _item):
        _size = len(self.data)
        if _ind == -1 or _size == _ind:
            self.data.append(_item)
        else:
            super().__setitem__(_ind, _item)






def main():
    a = MagicList()
    a[0] = 5
    print(a)

    b = MagicList(cls_type=Person)
    b[0].age = 5
    print(b)


if __name__ == '__main__':
    main()




