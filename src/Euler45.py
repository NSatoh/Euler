#coding:utf-8
'''
Created on 2012/08/12

@author: NSatoh
'''

# T_n = n(n+1)/2
# P_n = n(3n-1)/2
# H_n = n(2n-1)
#
# まず六角数をまわして、それが五角数か判定、通ったら、三角数か判定、って感じでよい？

# a = T_n  <=>  a  = n(n + 1)/2
#          <=>  2a = n^2 + n
#          <=>   n = (-1 + sqrt(1 + 8a) ) / 2
# したがって、三角数であるためには、1+8a が（奇数の）平方数であることが必要十分
# 奇数は当然なので、結局 1+8a が平方数かどうかだけチェックすればよい

# a = P_n  <=>  a  = n(3n - 1)/2
#          <=>  2a = 3n^2 - n
#          <=>   n = (1 + sqrt(1 + 24a) ) / 6
# したがって、三角数であるためには、1+24a が ≡2(mod 3)なる数の平方であればよい

def isTriangular(a):
    sq = 1 + 8*a
    if sq - int(sq**0.5)**2 == 0:
        return True
    return False

def isPentagonal(a):
    sq = 1 + 24*a
    if sq - int(sq**0.5)**2 == 0:
        if (int(sq**0.5) + 1)% 3 == 0:
            return True
    return False

#for a in [1,3,6,10,15,2,8,9,11]:
#    print isTriangular(a)
#for a in [1, 5, 12, 22, 35, 2,3,6,7]:
#    print isPentagonal(a)

cnt = 0
n = 1
while cnt < 3:
    H = n*(2*n-1)
    if isPentagonal(H):
        if isTriangular(H):
            print H,n
            cnt += 1
    n += 1


