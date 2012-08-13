#coding:utf-8
'''
Created on 2012/08/13 

@author: NSatoh
'''

# n が素因数を4つ持つか？
#     yes -> counter += 1
#     no  -> counter = 0
# n += 1
# counter が 4 になったときの n-3 が答え
#
# ってのが素朴に思いつく方法か？

def numberOfPF(n): # Prime Factor の個数。完全に素因数分解する必要はないが・・・
    number = 0
    if n % 2 == 0:
        number += 1
        n = n/2
    while n % 2 == 0: # 2は、他の素数と紛れがないので、割り尽くしておく必要はないが、
        n = n/2       # n が小さくなっている方が、結局探索範囲は狭まる。  
    for p in xrange(3,int(n**0.5)+1,2):
        if n % p == 0:
            number += 1
            n = n/p
        while n % p == 0: # 割り尽くしておかないと、p の倍数を探索したときに
            n = n/p       # 素因数が増えちゃう
    if n > 1:
        number += 1
    return number

counter = 0
n = 2
while counter < 4:
    if numberOfPF(n) == 4:
        counter += 1
        #print n
    else:
        counter = 0
    n += 1

print
print "ans -> ",n-4
         
