# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:38:25 2024

@author: Student
"""

N = int(input("Nhập số nguyên dương N: "))
tong = 0

while N > 0:
    chu_so = N % 10
    
    tong += chu_so
    
    N //= 10
print("Tổng các chữ số là ", tong)