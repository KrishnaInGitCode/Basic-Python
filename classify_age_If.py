# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 09:06:05 2024

@author: krish
"""
age = int(input("Enter your age:")) 

if age < 13 :
    print ("You are child")
elif 13 < age <= 18 :
    print ("You are teen")
elif 18 < age <= 50 :
    print("You are adult")
else :
    print("You are Senior")