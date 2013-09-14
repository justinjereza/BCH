#!/usr/bin/python

# Valid BCH codes: (48, 36), (40, 28), (32, 20)
class Message(object):
    def __init__(self):
        self._data = bytearray()

    def __init__(self, x):
        if isinstance(x, str):
            self._data = bytearray(x)
        elif isinstance(x, bytearray):
            self._data = x
        elif isinstance(x, Message):
            self._data = x._data
        print self._data

    def __getattr__(self, name):
        if name == 'color_code':
            return self._data[0]

    def generate(self, x):
        pass

    @staticmethod
    def _g(x):
        return x**12 + x**10 + x**8 + x**5 + x**4 + x**3 + 1

print Message('abcde').color_code
