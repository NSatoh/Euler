'''
Created on 2011/09/23

@author: School
'''


import math

sum = 2 
cnt = 1
N = 3 # 2 is even-prime. Other prime numbers are all odd-prime
while N < 2000000:
    tmp = N
    bound = int(math.floor(math.sqrt(tmp)))+1
    for prime in range(3,bound,2):
        while tmp % prime == 0:
            tmp = tmp / prime
    if tmp == N:
        sum = sum + N
        cnt = cnt + 1
        print [cnt,N]
    N = N + 2 

print sum