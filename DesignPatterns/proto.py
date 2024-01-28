import copy
from typing import Any
from icecream import ic


class SubjectivePrototype:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __call__(self, other) -> Any:
        ic("called boiii")

    def __copy__(self):
        a, b = copy.copy(self.a), copy.copy(self.b)
        ic(a, b)
        new_obj = self.__class__(a, b)
        ic(new_obj)
        ic(new_obj.__dict__)
        new_obj.__dict__.update(self.__dict__)
        ic(new_obj.__dict__)
        return new_obj

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        a, b = copy.deepcopy(self.a, memo=memo), copy.deepcopy(self.b, memo=memo)
        ic(a, b)
        new_obj = self.__class__(a, b)
        ic(new_obj)
        ic(new_obj.__dict__)
        new_obj.__dict__ = copy.deepcopy(self.__dict__, memo=memo)
        ic(new_obj.__dict__)
        return new_obj


obj = SubjectivePrototype(12, 44)
newO = copy.copy(obj)
newO.a = 23
print(type(newO))
ic(newO.a, obj.a)
dc = copy.deepcopy(obj)
ic(dc.a)