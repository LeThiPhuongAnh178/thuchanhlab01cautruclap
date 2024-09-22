# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:32:29 2024

@author: phuong 
"""

quangduong= float (input("nhập số km đã đi:"))
motkmdau= 15000
kmhaidennam= 13500
km_thu_sau= 11000
if quangduong<=1:
    sotien= motkmdau
    print("số tiền đi được là:", sotien)
elif  1 < quangduong <= 5:
    sotien= motkmdau + ((quangduong-1)*kmhaidennam) 
    print("số tiền đi được là:", sotien)
elif quangduong >=6:
    sotien= motkmdau + (4* kmhaidennam) + ((quangduong)*km_thu_sau)
    print("số tiền đi được là:", sotien)
elif quangduong >120:
    sotien= sotien*0.9
    print("sô tiền đi được là:", sotien)