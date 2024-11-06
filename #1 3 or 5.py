# -*- coding: utf-8 -*-
"""

Ethan Mort

Sum of all multiple of 3 or 5 below 1000

"""

list =[]
total = 0

for i in range(0,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        list.append(i)

for i in list:
    total += i

print(total)