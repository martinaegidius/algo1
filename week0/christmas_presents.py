#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:00:58 2022

@author: max
"""

presents = list(map(int,input().split()))

jealous = []
if presents[2] > presents[0] and presents[1] > presents[0]:
    jealous.append('Anna')
if presents[2] < presents[0] or presents[2] < presents[1]: 
    jealous.append('Oscar')
if presents[0] > presents[1]: 
    jealous.append('Laura')

if len(jealous)==0:
    jealous.append('NONE')
    
jealous.sort()

for i in range(len(jealous)):
    print(jealous[i])
    
        