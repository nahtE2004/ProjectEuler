# -*- coding: utf-8 -*-
"""
Ethan Mort

Smallest positive number which is evenly divisible by all the numbers from 1 to 20

"""

def factorpair(num): #finds one factor pair of num
    factors = []
    i = 2
    while len(factors) == 0 and i <= num:
        if num % i == 0:
            factors.append(i)
            factors.append(num//i)
        i += 1
    if 1 in factors:
        factors.remove(1)
    return factors

def primefactors(num):
    wip = [[num]] #list containing each generation in breaking down factors
    i=0 #creates a numerical value for each generation
    while wip[i] != wip[i-1] or i == 0: #compares current generation to previous to check if have changed
        ifactors = [] #holds factors of this generation
        for j in wip[i]: #iterates through each value in generation, breaks down into factor pair and appends to ifactors
            jfactors = factorpair(j)
            for k in jfactors:
                ifactors.append(k)
        wip.append(ifactors) #appends new generation onto the end of wip
        i += 1
    return wip[-1]

number = int(input("Enter a number: "))

factorlist = []

for i in range(1,number+1):
    factorlist.append(primefactors(i))
print(factorlist)

factortotals = {}
for i in factorlist:
    print(i)
    print(factortotals)
    for factor in i:
        frequency = i.count(factor)
        if factor not in factortotals.keys():
            factortotals.update({factor:frequency})
        elif factortotals[factor] < frequency:
            factortotals.update({factor:frequency})

answer = 1
for factor in factortotals.keys():
    answer *= (factor ** factortotals[factor])

print("The smallest number evenly divisible by all inegers for 1 to",number,"is",answer)