# -*- coding: utf-8 -*-
"""

Ethan Mort

Sum of all positive fibonacci number below 4 million

"""

list = []
num1 = 1
num2 = 1
num3 = 0
total = 0
while num3 < 4000000:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 % 2 == 0:
        list.append(num3)
        
for i in list:
    total += i
    
print(total)
    