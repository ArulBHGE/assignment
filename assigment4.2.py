# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:21:23 2022

@author: 105042833
"""

import math
import operator
lst_1=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("the given list to be multiplied is:", lst_1)
list_2=[]
a=int(input("constant to be multiplied:"))
#print(a)
#print(type(a))
for i in range (0,len(lst_1)):
    list_2.append(a)
#print(list_2)
#print(type(list_2))
res = list(map(operator.mul, lst_1, list_2))
print("list after multiplication:", (res))

