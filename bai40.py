# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:28:28 2024

@author: Student
"""

s=0
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập n: "))
    
for i in range(1, n+1):
    s += 1/ (2*i)
print(round(s, 2))
