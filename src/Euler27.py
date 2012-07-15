#coding:utf-8
'''
Created on 2012/03/11

@author: NSatoh
'''

import math

def is_prime(n):
    if n < 2:
        return False
    m = int(math.floor(math.sqrt(n)))
    for p in range(2,m+1):
        if n % p == 0:
            return False
    return True

prime_iooo = range(2,1000)

for d in range(2,31):    # Eratosthenes
    for p in prime_iooo:
        if p > d:
            if p % d == 0:
                prime_iooo.remove(p)
       
print prime_iooo    

#tmp_a_list = range(-1000,1001)
#a_list = []
#
## 1 + a + b is prime
## 4 + 2a + b is prime
## 9 + 3a + b is prime
#for b in prime_iooo:
#    for a in tmp_a_list:
#       if is_prime(1 + a + b) and is_prime(4 + 2*a + b) and is_prime(9 + 3*a + b):
#           if is_prime(16 + 4*a + b) and is_prime(25 + 5*a + b): 
#               tmp_a_list.remove(a)
#               a_list.append(a)
#
#print a_list
#print len(a_list)*len(prime_iooo)

def f(a,b,n):
    return n**2 + a*n + b

o_a_list = range(-1000,1001)
e_a_list = []
o_b_list = prime_iooo
e_b_list = []

kouho = len(o_a_list)
n = 1
while kouho > 1:
    if n % 2 == 0:
        tmp_a_list = e_a_list
        a_list = o_a_list
        tmp_b_list = e_b_list
        b_list = o_b_list
    else:
        tmp_a_list = o_a_list
        a_list = e_a_list
        tmp_b_list = o_b_list
        b_list = e_b_list
    for b in tmp_b_list:
        for a in tmp_a_list:
            if is_prime(f(a,b,n)):
                tmp_a_list.remove(a) # aは、1つでも相手が見つかったらもう調べる必要がない。消す。
                a_list.append(a)
                if not b in b_list:
                    b_list.append(b) # bはまだ消さない。他のaの相棒になるかもしれない。今知りたいのは相手がいないbだけ。
    del tmp_a_list[:] 
    del tmp_b_list[:] # ここで消す。これで相手が一人もいないbだけが散っていく。
    print "a in " + str(a_list)
    print "b in " + str(b_list)
    kouho = len(a_list)
    print "kouho a -->" + str(kouho)
    print "n is " + str(n)
    n += 1

for a in [-17,-7]:
    for b in [113,479]:
        print "(a,b) = (%d, %d)" % (a ,b)
        for n in range(67):
            print n,f(a,b,n), is_prime(f(a,b,n))

print "The answer is (a,b) = (%d,%d)" % (-17, 113)
ab = -17*113
print "a times b = %d" % ab


