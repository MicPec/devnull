#!/usr/bin/env python3


class Magic:
    def __init__(self, func):
        self.func = func

    def __ror__(self, value):
        return Magic(lambda x, y=value: self.func(y, x))

    def __or__(self, value):
        return self.func(value)

    def __call__(self, x, y):
        return self.func(x, y)


# Set variables by simple binary operations
_1 = 1
_2, _3, _4 = _1 << _1, _1 << _1 | _1, _1 << _1 << _1
_5, _6 = _4 | _1, _2 << _1 | _2

encoded = [
    _1 << _5 | _1,  # 33
    _1 << _6 | _2 | _1,  # 67
    _1 << _3,  # 8
    _4 | _1 << _1,  # 6
    -(_1 << _1 | _1),  # -3
    _2 << _2,  # 8
    -(_2 << _5 | _1 << _4 | _3 << _1 | _1),  # -87
    _3 << _2,  # 12
    _4 << _2 << _2 | _1 << _1 | _1,  # 67
    -(_1 << _1 | _1),  # -3
    _1 >> _2,  # 0
    -(_1 << _2 | _2 | _1),  # -7
    -(_3 << _3 | _1 << _2 | _1),  # -29
    _1 >> _1,  # 0
]


values = [0]
decoded = []
_get_length_ = lambda x: len(x)
_add_ = Magic(lambda x, y: x + y)
_dec_chr_ = Magic(lambda x, y: chr(x + y))
_append_ = Magic(lambda x, y: x.append(y))


for i in range(_get_length_(encoded)):
    # values.append(encoded[i] + values[i])
    values | _append_ | (encoded[i] - _1 | _add_ | values[i] - -_1)

    # decoded.append(chr(values[i]))
    decoded | _append_ | (values[i] + _1 | _dec_chr_ | -_1)

print("".join(decoded)[::-1])
