# -*- coding: utf-8 -*-
"""
Ethan Mort

Largest palindrome made from the product of two three digit numbers

"""

palindromes =[]
for i in range(100,1000):
    for j in range(100,1000):
        num = i * j
        numstr = str(num)
        numlist = []
        for n in numstr:
            numlist.append(n)
        length = len(numlist)
        if length % 2 == 0:
            target = length // 2
        else:
            target = (length - 1) // 2
        score = 0
        for k in range(1,target+1):
                if numlist[k-1] == numlist[-k]:
                    score += 1
        if score == target:
            palindromes.append(num)

spalindromes = sorted(palindromes)
print(spalindromes[-1])
