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

#print prime_iooo # n = 0 で b:prime ゆえ、これがbの第一候補
print len(prime_iooo)

def f(a,b,n):
    return n**2 + a*n + b

pair_list = []
for b in prime_iooo:
    for a in range(-1000,1001):
        if is_prime(f(a,b,1)):
              pair_list.append([a,b]) # n = 1 のときに prime となるような a,b たちのペア第一候補

print len(pair_list)

o_ab_list = []
e_ab_list = pair_list

n = 2
kouho = len(e_ab_list)
while kouho > 1:
    if n % 2 == 0:
        tmp_ab_list = e_ab_list
        ab_list = o_ab_list
    else:
        tmp_ab_list = o_ab_list
        ab_list = e_ab_list
    for ab in tmp_ab_list:
        if is_prime(f(ab[0],ab[1],n)):
            #tmp_ab_list.remove(ab) #ここで消してたら、番号ずれた。forでまわしてるリストから削るのはよくない？
            ab_list.append(ab) # 素数になったペアは新世界へ旅立つ。ノアの箱舟。
    del tmp_ab_list[:] # 素数にならなかったペアたちが散っていく。大洪水。
    kouho = len(ab_list)
    print "kouho [a,b] --> " + str(kouho)
    print "[1,41] in this list ? --> ", [1,41] in ab_list # エラーチェッカー。39までTrueならまあ大丈夫やろ。
    print "n is " + str(n)
    n += 1

print ab_list
print ab_list[0][0]*ab_list[0][1]

