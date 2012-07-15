'''
Created on 2011/09/23

@author: School
'''

import math

N = 600851475143
bound = int(math.floor( math.sqrt(N) ))+1

#print bound

for p in range(3,bound,2):
    i = N % p
    while i == 0:
        prime = p
        N = N / p
        i = N % p
        #print " N = " + str(N)
        #print " i = " + str(i)
if N > 1:
    prime = N
 
print prime