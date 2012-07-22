#coding:utf-8
'''
Created on 2012/07/21

@author: NSatoh
'''



NSmath_name = []
NSmath_variable = []
NSmath_return = []
NSmath_require = []


#---------------------------------------------------------------------------------

# ユークリッド互除法による、最大公約数
def Euclid(a,b):
    if b == 0:
        return a
    else:
        return Euclid(b,a%b)

NSmath_name += ["Euclid(a,b)"]
NSmath_variable += ["int a, b"]
NSmath_return += ["num gcd(a,b)"]
NSmath_require += [0]

# 拡張ユークリッド互除法： a,b --> x,y; ax + by = g(=gcd(a,b))  
def extendedEuclid(a,b,x0,x1,y0,y1):     # [x0,x1]=[1,0], [y0,y1]=[0,1] からスタートを想定
    if b == 0:                           # b == 0 なら、 ax_0 + by0 = g (<=> a*1 + 0*0 = a) 
        return [x0,y0]                   # なので、[x0,y0] を返す。
    else:                                # それ以外なら、[a,b] = [b,a%b], [x0,x1] = [x1,x0 - q*x]
        q = a/b                          # などとして、繰り返す（q = a/b :商 int型ならこれで平気だと思うが。a//bなら確実？)
        return extendedEuclid(b,a%b,x1,x0-q*x1,y1,y0-q*y1) 

def exEuclid(a,b):
    return extendedEuclid(a,b,1,0,0,1)

NSmath_name += ["exEuclid(a,b)"]
NSmath_variable += ["int a, b"]
NSmath_return += ["list [x,y,g ; g = gcd(a,b), ax + by = g]"]
NSmath_require += ["extendedEuclid"]

# L:List の数字から、a個を取り出して並べて、a桁の十進数を作る。そのリストを返す。
def permutateDecimal(L,a): 
    if a == 0:
        return [0]
    else:
        return [top*(10**(a-1)) + btm for i,top in enumerate(L)
                                      for btm in permutateDecimal(L[:i]+L[i+1:],a-1)]

NSmath_name += ["permutateDecimal(L,a)"]
NSmath_variable += ["list L, num a"]
NSmath_return += ["list [num; distinct a decimal digits from L]"]
NSmath_require += [0]

# 「L:List の数字から、a個を取り出して並べたリスト」のリストを返す。
def permutationList(L,a): 
    if a == 0:
        return [[]]
    else:
        return [[top] + btm for i,top in enumerate(L)
                                      for btm in permutationList(L[:i]+L[i+1:],a-1)]

NSmath_name += ["permutateList(L,a)"]
NSmath_variable += ["list L, num a"]
NSmath_return += ["list [ [l[0], l[1], ..., l[a-1]] ; distinct l[i] s from L]"]
NSmath_require += [0]

print NSmath_require

#---------------------------------------------------------------------------------

def help():
    print 
    print "----------- NS-math module -----------"
    print
    
    for i,name in enumerate(NSmath_name):
        print "■ " + name + " ; " + NSmath_variable[i] 
        print "  --> " + NSmath_return[i]
        if NSmath_require[i] != 0:
            print "    ### Required nsmath." + NSmath_require[i]
        print

    print    
    print "--------------------------------------"
    print


