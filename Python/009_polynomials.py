'''
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
'''

import numpy

p = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(p, x))