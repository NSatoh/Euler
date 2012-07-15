'''
Created on 2011/09/25

@author: NSatoh
'''

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def power_reset(power):
     return [0 for i in range(len(power))]

power = power_reset(prime)

def d(n):
    power = power_reset(prime)
    prod = 1
    tmp = n
    for i in range(len(prime)):
        sum = 1
        # print prime[i]
        while tmp % prime[i] == 0:
            tmp = tmp / prime[i]
            power[i] = power[i] + 1
            sum = sum + prime[i]**power[i]
        prod = prod * sum
        # print " prod = %d " % prod
    if tmp > 1:
        prod = prod * (1 + tmp)
    return prod - n
        
ans = 0
yuuai = []
for n in range(2,10000):
    dn = d(n)
    print " n = %d , d(n) = %d " % (n , dn)
    print dn
    if dn <> n:
        if d( dn ) == n:
            ans = ans + n
            yuuai = yuuai + ["%d -- %d" % (n,dn)]
            print yuuai

print ans
print yuuai

    