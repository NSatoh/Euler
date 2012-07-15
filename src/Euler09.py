'''
Created on 2011/09/23

@author: School
'''
import math
for a in range(1,333):
    bbound = int( math.floor( (1000 - a)/2 ) )+1
    for b in range(a+1,bbound):
        c = 1000 - a - b
        if c*c == a*a + b*b:
            print [a,b,c]
            print a*b*c
