#coding:utf-8
'''
Created on 2012/08/01

@author: NSatoh
'''

# とりあえず、1から9までの和は45なので、9桁は9の倍数だから素数はあり得ない。
# 一度チェックしてみよう。

# a = 0
# triangleNums = []
#
# for i in range(1,10):
#     a += i
#     triangleNums += [a]
#
# print triangleNums
#
# >> [1, 3, 6, 10, 15, 21, 28, 36, 45]
#
# ということで、8桁・6桁・5桁・3桁・2桁もアウト。
# もうこれ、答え7桁に絞って良いのでは？まあ7桁になければ4桁か。
# 7桁くらいなら、Euler35で作ったEratosthenesを使っても、まあ許容な計算時間だろうか。
# でもまあ、やっぱり7桁の順列で末尾が 2,4,5,6以外のもの、で上から調べる方が速いかな。
# 7桁の順列だが、末尾に制限があるので、6!*3 = 2160 個、大したことねえべ。
# 末尾に制約があるので、末尾から先にまわして、最後にソートかな。

def permutationBottomDecimal(L,a):
    if a == 0:
        return [0]
    else:
        return [top*10 + btm for i,btm in enumerate(L)
                             for top in permutationBottomDecimal(L[:i]+L[i+1:],a-1)]

admissible_btm = [1,3,7]

kouho = []
for bottom in admissible_btm:
    l = range(1,8)
    l.remove(bottom)
    top_list = permutationBottomDecimal(l,6)
    kouho += [10*top_list[i] + bottom for i in xrange(len(top_list))]

kouho.sort()

def isPrime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True

for p in kouho:
    if isPrime(p):
        ans = p
        # break 逆だった。今小さい順に並べてしまったから、とりあえず削除。ソートを逆順にしたいな。

print ans
