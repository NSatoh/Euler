#coding:utf-8
'''
Created on 2012/07/21

@author: NSatoh
'''



NSmath_name_list = []

#---------------------------------------------------------------------------------

# ユークリッド互除法による、最大公約数
def Euclid(a,b):
    if b == 0:
        return a
    else:
        return Euclid(b,a%b)

NSmath_name_list += ["Euclid(a,b) --> num gcd(a,b)"]


# 拡張ユークリッド互除法： a,b --> x,y; ax + by = g(=gcd(a,b))  
def extendedEuclid(a,b,x0,x1,y0,y1):     # [x0,x1]=[1,0], [y0,y1]=[0,1] からスタートを想定
    if b == 0:                           # b == 0 なら、 ax_0 + by0 = g (<=> a*1 + 0*0 = a) 
        return [x0,y0]                   # なので、[x0,y0] を返す。
    else:                                # それ以外なら、[a,b] = [b,a%b], [x0,x1] = [x1,x0 - q*x]
        q = a/b                          # などとして、繰り返す（q = a/b :商 int型ならこれで平気だと思うが。a//bなら確実？)
        return extendedEuclid(b,a%b,x1,x0-q*x1,y1,y0-q*y1) 

def exEuclid(a,b):
    return extendedEuclid(a,b,1,0,0,1)

NSmath_name_list += ["exEuclid(a,b) --> list [x,y,g] ; g = gcd(a,b), ax + by = g \n ###Required nsmath.extendedEuclid"]






#---------------------------------------------------------------------------------

def help():
    print 
    print "----------- NS-math module -----------"
    print
    
    for explanation in NSmath_name_list:
        print explanation

    print    
    print "--------------------------------------"
    print