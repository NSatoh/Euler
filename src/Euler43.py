#coding:utf-8
'''
Created on 2012/08/11

@author: NSatoh
'''

# d2 d3 d4 : 2で割り切れる => d4: 2の倍数
# d3 d4 d5 : 3で割り切れる => d3 + d4 + d5: 3の倍数
# d4 d5 d6 : 5で割り切れる => d6: 0, 5
# d5 d6 d7 : 7で割り切れる => d5 d6 - 2*d7: 7の倍数
# d6 d7 d8 : 11で割り切れる => d6 - d7 + d8: 11の倍数
# d7 d8 d9 : 13で割り切れる 
# d8 d9 d10: 17で割り切れる => d8 d9 - 5*d10: 17の倍数
#
# 使わなそうな条件も多いが、とりあえずこんなところか。
# 17の倍数でまずd8 d9 d10 を絞るのが速そう？

def hasDistinctDigits(num):
    s = str(num)
    for i in xrange(len(s)):
        if s[i] in s[i+1:]:
            return False
    return True

#print hasDistinctDigits(123)
#print hasDistinctDigits(123345)

admissible = []
for i in xrange(2,1000/7):
    if hasDistinctDigits(7*i):
        admissible += [7*i]

admissible.remove(70) # 1つだけ明らかに例外なので除外。あとは大丈夫
            
#print admissible
#print len(admissible)

def nextDigit(admissible_num): # すべての桁が異なる、という条件で、次の桁に使える数のリストを返す
    s = str(admissible_num)
    next = range(10)
    for i in s:
        next.remove(int(i))
    return next







