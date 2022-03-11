# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:21:23 2022

@author: 105042833
"""

import math
import operator
x=input("list to be multiplied (no space or camma):")
y=list(x)
z=list(map(int, x))
print("given list to be multiplied",z)
a=input("constant to be multiplied:")
#print(a)
b=list(map(int, a))
c=list(b)*len((z))
print(c)
res = list(map(operator.mul, z, c))
print("the list after multiplication:"+str(res))


