#coding:utf-8
'''
Created on 2012/05/06

@author: NSatoh
'''

Lp = [200, 100, 50, 20, 10, 5, 2, 1]

def pay_Lp(money,n):
    kekka = 0
    if n == 7:
        return 1
    i = 0
    while Lp[n]*i <= money :
        kekka += pay_Lp(money-Lp[n]*i,n+1)
        i += 1
    return kekka

print pay_Lp(200,0)
