# -*- coding: utf-8 -*-

def my_abs(x):
    if x>0:
        return x
    else:
        return -x


print(my_abs(-10))

import math
def quadratic(a,b,c):
    t=pow(b,2)-4*a*c
    if t > 0:
        m=(-b+t)/(2*a)
        n=(-b-t)/(2*a)
        return '有两个不同的解',m,n
    elif t == 0:
        m=-(b/(2*a))
        return '有且只有一个解',m
    else:
        return '无解'

a = 1
b = 3
c = -4

print(quadratic(a,b,c))
