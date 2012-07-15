#coding:utf-8
'''
Created on 2012/07/15

@author: NSatoh
'''

import math

def perm(L,a): # L:List の数字から、同じ数字を使わずにa桁の数を作り出してリストを作る
    if a == 0:
        return [0]
    else:
        return [top*(10**(a-1)) + btm for i,top in enumerate(L)
                                      for btm in perm(L[:i]+L[i+1:],a-1)]

#print perm([1,2,3,4,5,6,7,8],2)


def is_FromOneToNine(a,b):
    a_b_ab = str(a)+str(b)+str(a*b)
    if len(a_b_ab) <> 9:
        return False
    else:
        for i in range(1,10):
            if a_b_ab.find(str(i)) == -1:
                return False
        return True
            
ans = 0
prod_list = []

# 1桁    ×  4桁      =  4桁
#  a  ×   b   =  ab 
for a in range(1,10):
    b_list = range(1,10)
    b_list.remove(a)
    for b in perm(b_list,4):
        if is_FromOneToNine(a,b):
            if a*b in prod_list:
                continue
            else:
                ans += a*b
                prod_list += [a*b] 

# 2桁    ×  3桁      =  4桁
#  a  ×   b   =  ab 
for a in perm(range(1,10),2):
    b_list = range(1,10)
    #b_list.remove(a % 10)
    #b_list.remove(int(math.floor(a/10)))
    for i in str(a):    # 文字列に in が使えるというKimからの天才的助言
        b_list.remove(int(i))
    for b in perm(b_list,3):
        if is_FromOneToNine(a,b):
            if a*b in prod_list:
                continue
            else:
                ans += a*b
                prod_list += [a*b] 

print prod_list
print ans
    

    
    
    