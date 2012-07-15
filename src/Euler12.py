#coding:utf-8
'''
Created on 2011/09/23

@author: School
'''
# NumberOfDivisors = prod_{e is power of prime}(e + 1)
# なので、三角数を素因数分解して、その各素因子のベキ+1 を乗じ続ければイイ

import math

tri = 0
i = 0
num = 1
while num < 500:
    num = 1
    i = i + 1
    tri = tri + i    
    pow = 1
    tmp = tri
    while tmp % 2 == 0:
        pow = pow + 1
        tmp = tmp / 2
    num = num * pow
    bound = int(math.floor(math.sqrt(tmp)))+1
    for prime in range(3,bound,2):
        pow = 1
        while tmp % prime == 0:
            pow = pow + 1
            tmp = tmp / prime
        num = num * pow
    if tmp > 1:
        num = num * 2
    print [i,tri,num]

print tri