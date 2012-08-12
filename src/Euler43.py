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
# 数字を数で扱うと面倒そう。桁で区切ってリストに突っ込んだ方がいいかも

def hasDistinctDigits(list):
    for i in xrange(len(list)):
        if list[i] in list[i+1:]:
            return False
    return True

#print hasDistinctDigits(123)
#print hasDistinctDigits(123345)

admissible = []

for i in xrange(2,100/17+1):
    s = str(17*i)
    l = [0,int(s[0]),int(s[1])]
    if hasDistinctDigits(l):
        admissible += [l]

for i in xrange(100/17+1,1000/17):
    s = str(17*i)
    l = [int(s[0]),int(s[1]),int(s[2])]
    if hasDistinctDigits(l):
        admissible += [l]
          
#print admissible
#print len(admissible) # 候補少ないな。これくらいなら、約数毎に判定法とか使わないで、まとめて処理していいか。

def nextDigit(list): # すべての桁が異なる、という条件で、次の桁に使える数のリストを返す
    next = range(10)
    for i in list:
        next.remove(i)
    return next

divisors = [13,11,7,5,3,2]

for d in divisors:
    new_admissible = []
    for l in admissible:
        next = nextDigit(l)
        for digit in next:
            if (100*digit + 10*l[0] + l[1]) % d == 0:
                new_admissible += [[digit]+l]
    print new_admissible
    print len(new_admissible)
    admissible = list(new_admissible)
    
sumDigit = [0]*10
for l in admissible:
    pandigital = nextDigit(l) + l # あと1桁残っているはずなので
    sumDigit = map((lambda x,y: x+y),sumDigit,pandigital)
    print sumDigit

sum = 0    
for i in xrange(10):
    sum += 10**(9-i) * sumDigit[i]

print sum
