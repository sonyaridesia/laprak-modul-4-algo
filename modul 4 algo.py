#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:50:41 2022

@author: sonyaridesia
"""

import calendar
print("Program dapat menentukan jumlah hari di salah satu bulan")
ulang = "y"
while ulang == "y" or ulang == "n": 
    year = int(input("Masukan Tahun yang anda inginkan: ")) 
    month = int(input("Masukan Bulan yang anda inginkan: "))
    print("Ada", (calendar.monthrange(year, month)[1]), "Hari di bulan ke",month)
    ulang = input("ketik'y' jika ingin lanjut, ketik 'n' jika stop ")
    if ulang == "n":
        print("Terimakasih sudah Menggunakan program ini")
        print("Sonya Ridesia 064002200007")
        break