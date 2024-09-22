# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:48:46 2024

@author: Student
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
if a + b > c and a + c > b and b + c > a:
    if a==b==c:
        print("Đây là tam giác đều.")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2 :
        print("Đây là tam giác vuông.")
    elif a==b or b==c or c==a:
        print("Đây là tam giác cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Đây không phải là 3 cạnh của tam giác.")
    