#coding:utf-8
'''
Created on 2012/07/31

@author: NSatoh
'''

# ピタゴラス数の話のよう。
# a^2 + b^2 = c^2 ; 原始
#   <=> a = m^2 - n^2, b = 2mn, c = m^2 + n^2 ; 
#       m > n, m と n との偶奇は異なる  
# ということで、 パラメータを m, n, k として {ka, kb, kc}を作れば尽くされる。
# [0,　0,　0,　0,　...,　0]なリストを作って、和をとるごとにそのindexの数を1つ増やせば良いかな。
# p = ka + kb + kc = 2km(m+n)なので、
# m を先にまわして、2m(m + n) <= 1000  i.e. n <= 500/m - m
# 従って、500/m - m > 0  iff. 500 > m^2 
# の範囲で調べれば良い。



number_p = [0]*1001

for m in xrange(1,int(500**0.5)+1):
    for n in xrange(1,500/m - m + 1):
        if (m + n) % 2 == 1 and m > n:
            for k in xrange( 1, int( 500/(m*(m+n))+1 ) ):
                number_p[2*k*m*(m+n)] += 1
                print k*(m**2-n**2), k*(2*m*n), k*(m**2+n**2)
            
print number_p
print number_p.index(max(number_p))

# ネットで調べたら、list x の最大値の index を取得したかったら、
# max(xrange(len(x)), key=lambda i: x[i]) とか
# max(enumerate(x), key=lambda x: x[1])[0] とか
# でも良いらしい。こっちの方が良さそうなことが書いてあったが、よく分からんので、
# メモに残しておこう。

## シンプルにやるなら、こうか？
#simple_p = [0]*1001
#for p in xrange(3,1000):
#   for c in xrange(1,p/3+1):
#       for b in xrange(c,(p-c)/2+1):
#           a = p - c - b 
#           if a^2 + b^2 == c:
#               simple_p[p] += 1
## ダメだった。遅い上に、間違ってた。どこが間違っているのかは、今度考えよう。
print simple_p
print simple_p.index(max(simple_p))

