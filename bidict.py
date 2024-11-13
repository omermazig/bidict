from collections import defaultdict
from typing import Any


class TwoWayDictNaive(dict):
    def get_keys_for_value(self, value):
        return {key for key, val in self.items() if val == value}


class TwoWayDictReverse(dict):
    """ Note that mutable values will cause an error if used with this class. """

    def __init__(self):
        super().__init__()
        self.values_to_keys = defaultdict(set)

    def __setitem__(self, key: Any, value: Any):
        if key in self:
            self.get_keys_for_value(self[key]).remove(key)
        self.values_to_keys[value].add(key)
        super().__setitem__(key, value)

    def pop(self, __key):
        if __key in self:
            self.get_keys_for_value(self[__key]).remove(__key)
        super().pop(__key)

    def get_keys_for_value(self, value: Any) -> set:
        return self.values_to_keys[value]
