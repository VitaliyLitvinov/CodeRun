from decimal import *
from math import sqrt
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
dis = b ** 2 - 4*a*c
if dis==0:
    print(1)
    x = -b/2*a
    print(Decimal(x).quantize(Decimal("1.000000")))
elif dis > 0:
    x1 = (-b + sqrt(dis)) / (2*a)
    x2 = (-b - sqrt(dis)) / (2*a)
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    print(2)
    print(Decimal(min_x).quantize(Decimal("1.000000")), end=' ')
    print(Decimal(max_x).quantize(Decimal("1.000000")))
else:
    print(0)