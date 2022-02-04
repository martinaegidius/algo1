#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:43:35 2022

@author: max
"""

nums = list(map(int,input().split()))
seqsum = 0
for i in range(len(nums)):
    seqsum += nums[i]
print(seqsum)