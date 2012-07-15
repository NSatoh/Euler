'''
Created on 2011/12/24

@author: NSatoh
'''
import math
kajou = []

for num in range(12,28123):
    N = num
    factor_sum = 1
    i = N % 2
    e = 1
    while i == 0:
        N = N / 2
        e = e + 1
        i = N % 2
    factor_sum = factor_sum * (2**e - 1)/(2 - 1)        
    bound = int(math.floor( math.sqrt(N) ))+1
    for p in range(3,bound,2):
        i = N % p
        e = 1
        while i == 0:
            N = N / p
            e = e + 1
            i = N % p
        factor_sum = factor_sum * (p**e - 1)/(p - 1)
    if N > 1:
        factor_sum = factor_sum *(N+1)
    if 2*num < factor_sum:
        kajou = kajou + [num]

print kajou
number_of_kajou = len(kajou)
print "the number of Kajou_suu --> ",
print number_of_kajou
ng = set([])
for i in range(number_of_kajou):
    for j in range(i,number_of_kajou):
        if kajou[i] + kajou[j] < 28123:
            ng.add(kajou[i]+kajou[j])

sum = 28122*28123/2 
for n in ng:
    sum = sum - n

print "Answer --> ",
print sum