#coding:utf-8
'''
Created on 2012/07/31

@author: NSatoh
'''

# 先頭と末尾の桁は、2,3,5,7 に限られる。しかも、末尾が 2, 5 はダメ。
# どういう順番で調べるのが速いか？11個という上限が与えられているので、11個に達した時点で止めてもいいか。
#
# 2(*)3, 2(*)7, 3(*)3, 3(*)7, 5(*)3, 5(*)7, 7(*)3, 7(*)7, 2(**)3, 2(**)7, ... 
# て順番でいいか。
#
# 右切り詰めで、すべての桁には1の位になる時が訪れる。従って、先頭と末尾以外の桁に使える数は 1, 3, 7, 9
#
# とりあえず、左切りつめで全部素数になるものを「左素数」、右を「右素数」とでも呼ぼう。
# 左素数と右素数を判定させればよさそう。これは、あまり多くないから、Eratosthenes より直接調べた方がよい？

def isPrime(n):
    for i in xrange(2,int(n**0.5)+1):
        if n % i == 0: return False
    return True

def isLeftPrime(n):
    s = str(n)
    left_cut = [int(s[i:]) for i in xrange(len(s))]
    if all(isPrime(p) for p in left_cut):
        return True
    else:
        return False

def isRightPrime(n):
    s = str(n)
    left_cut = [int(s[:i+1]) for i in xrange(len(s))]
    if all(isPrime(p) for p in left_cut):
        return True
    else:
        return False

# print isLeftPrime(3797)
# print isRightPrime(3797)
## 意外とイイ感じではなかろうか。遅いかな？

ans = 0
ans_list = []
digit = 2
admissible_top = [2,3,5,7]
admissible_digit = [1,3,7,9]
admissible_middle = [0]
admissible_btm = [3,7]

while len(ans_list) < 11:
    print "----------------------------------- ",digit," ---------------------------------------------"
    if digit > 2:
                admissible_middle = [10*ad_middle + ad_digit for ad_middle in admissible_middle
                                                             for ad_digit in admissible_digit]
    print admissible_middle
    for top in admissible_top:
        for btm in admissible_btm:
            top_btm = top*(10**(digit-1)) + btm
            print top_btm,
            for middle in admissible_middle:
                n = top_btm + 10*middle
                if isLeftPrime(n) and isRightPrime(n):
                    ans += n
                    ans_list += [n]
    digit += 1
    print

print "END...\n"
print ans_list
print ans



