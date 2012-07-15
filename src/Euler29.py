#coding:utf-8
'''
Created on 2012/05/06

@author: NSatoh
'''

import math

N = 10
a_pow_b = set() 

for a in range(2,N+1):
    for b in range(2,N+1):
        #a_pow_b.add(math.log(a,b))
        if a**b in a_pow_b:
            print "(a,b) = (%d,%d)" % (a, b)
        a_pow_b.add(a**b)

 
print len(a_pow_b)





