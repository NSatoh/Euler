#coding:utf-8
'''
Created on 2012/07/15

@author: NSatoh
'''

def Euclid(a,b):
    if b == 0:
        return a
    else:
        return Euclid(b,a%b)

# ab/ac = b/c  <=>  ab*c = ac*b 
#              <=>  a*10*c + b*c = a*10*b + c*b
#              <=>  b = c  このタイプはない。（全部trivial） 

# ba/ca = b/c  <=>  ba*c = ca*b 
#              <=>  b*10*c + a*c = c*10*b + a*b
#              <=>  b = c これもtrivial 

# ba/ac = b/c  <=>  ba*c = ac*b 
#              <=>  b*10*c + a*c = a*10*b + c*b
#              <=>  9*b*c = a*(10*b - c) 

# 考えるのは、これの b < c の場合と、分母分子が逆の場合

abc_list = [] # 要らないが、出力用
bc_list = []
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if b <> c:       # 工夫の欠片もねえ
                if 9*b*c == a*(10*b - c):
                    bc_list += [[b,c]]
                    abc_list += [[a,b,c]]
print abc_list
bunbo = 1
bunsi = 1
for bc in bc_list:
        bunbo *= max(bc)
        bunsi *= min(bc)

g = Euclid(bunbo,bunsi)
print bunbo/g


