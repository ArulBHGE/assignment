# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:25:51 2022

@author: 105042833
"""

import math
import operator
lst_1=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("the given list to be squared is:", lst_1)
res = list(map(operator.mul, lst_1, lst_1))
print("squared list is:",res)
