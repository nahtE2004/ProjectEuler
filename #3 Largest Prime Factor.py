# -*- coding: utf-8 -*-
"""
Ethan Mort

Largest prime factor of 600851475143

"""

# def factors(num): #finds all factor pairs of num
#     factors = []
#     for i in range(1,int(num)):
#         if (num % i == 0) and (i not in factors) and (num//i not in factors):
#             factors.append(i)
#             factors.append(num//i)
#     if len(factors) > 2:
#         factors.remove(num)
#     factors.remove(1)
#     return factors

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
    return wip

number = int(input("Enter a number: "))
print("The largest prime factor of " + str(number) + " is " + str(sorted((primefactors(number))[-1])[-1]))

