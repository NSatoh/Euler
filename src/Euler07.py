'''
Created on 2011/09/23

@author: School
'''

import math

N = 1 
cnt = 1 # 2 is even-prime. Other prime numbers are all odd-prime
print [cnt,2]
while cnt < 10001:
    N = N + 2 
    tmp = N
    bound = int(math.floor(math.sqrt(tmp)))+1
    for prime in range(3,bound,2):
        while tmp % prime == 0:
            tmp = tmp / prime
    if tmp == N:
        cnt = cnt + 1
        print [cnt,N]

print N