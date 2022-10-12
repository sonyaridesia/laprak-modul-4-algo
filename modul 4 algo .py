#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:00:59 2022

@author: sonyaridesia
"""

n = int(input("Masukkan jumlah maksimal : "))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end= '')
    print('\r')