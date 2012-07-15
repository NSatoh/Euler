#coding:utf-8
'''
Created on 2012/05/06

@author: NSatoh
'''
# a > sqrt(N) から先は、a^2 が N を超えるので、その先にはもう重複がない。それより小さい所で重複しているので、
# 予め小さい方で重複を排除しておけば、あとは全部足せばよい、という方針。
# 例えば、N=10 なら、a = 2,3 だけ、後半の重複を除いたものを数え、 4　～　9 の部分は、すべて 9 通りずつとカウント出来る。
# という方針。まあ、間違ってたけどね！！！

import math

N = 10

a_pow_b = 0 
num_dup = 0

a = 2
while a**2 <= N:
    print "a = " + str(a)
    maxPow = 2
    while a**maxPow <= N:
        maxPow += 1 
    #duplicate = set()
    duplicate = []              # 4^3 = 8^2 などが排除されないので、リストにしたが、それでもダメ。4^6 = 8^4 など。
    for pow in range(2,maxPow): # けど、これは平方数だけ上手くやれば、回避出来そうな気はする。
        k = 2
        while k*pow <= N:
            #duplicate.add(k*pow)
            duplicate.append(k*pow)
            k += 1
    a_pow_b += N-1 - len(duplicate)
    a += 1
    print "maxPow = " + str(maxPow)
    print duplicate
    print len(duplicate)
    num_dup += len(duplicate)

while a <= N:
    a_pow_b += N-1
    a += 1   

print "a_pow_b = " + str(a_pow_b)
print "(N-1)^2 = " + str((N-1)**2) 
print "num_dup = " + str(num_dup) 



