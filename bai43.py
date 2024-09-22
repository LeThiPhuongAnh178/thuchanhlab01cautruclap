# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:19:51 2024

@author: Student
"""

s=0
n = int(input("Nhập n: "))
while n<= 0:
    n = int(input("Nhập n: "))

for i in range(1, n+1):
    s += i/(i+1)
print(round(s, 2))
