from decimal import *
from cmath import sqrt

max_len = 100
max_precision = 50


def root(s, precision=32):
    try:
        return _root_(s, precision)
    except Exception:
        return 5, None


def _root_(s, precision):
    if type(s) == str and len(s) > max_len:
        return 3, None

    try:
        precision = int(precision)
    except ValueError:
        return 2, None

    if precision < 1 or precision > max_precision:
        return 4, None

    getcontext().prec = precision

    try:
        x = Decimal(s)
    except InvalidOperation:
        return 1, None

    getcontext().prec = precision

    if x == Decimal(0):
        ans = f'{Decimal(0):.{precision}f}'
    elif x > 0:
        ans = f'+- {sqrt(x).real:.{precision}f}'
    else:
        ans = f'+- {sqrt(x).imag:.{precision}f}i'
    return 0, ans

if __name__ == '__main__' :
    root(1, precision='0')

