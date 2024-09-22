# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:46:13 2024

@author: Student
"""

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if 1<= thang <= 12:
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        ngay = 31
        print("tháng này có 31 ngày")
    elif thang==2:
        if (nam % 4 == 0 and nam %100 != 0) or nam % 400 == 0:
            ngay = 29
            print("Năm nhuận")
        else:
            ngay = 28
            print("Không phải là năm nhuận")
    else:
        ngay = 30
    print(f" Tháng {thang} năm {nam} có {ngay} ngày")
    
    
    