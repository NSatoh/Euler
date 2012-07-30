#coding:utf-8
'''
Created on 2012/07/30

@author: NSatoh
'''

# 1,000,000 まで Eratosthenes しようとすると意外と大変？そうでもないか。
# 素数のリストを用意しなくても、数字のリストである程度何とかなるか。
# 2桁以上では、巡回させるのだからそもそも偶数と5は出現不可
# 桁和が3の倍数もはじくことができるが、まあそれはいいか。
# 一応、Eratosthenes してみようか。

def Eratosthenes(n):
    TF_list = [True] * n
    for i in xrange(2, int(n**0.5) + 1):
        if TF_list[i]: 
            for j in xrange(2*i, len(TF_list), i): # i 自身は True のままに、i の倍数たちを全員 False に。
                TF_list[j] = False
    return [str(p) for p in xrange(0,n) if TF_list[p] and p > 1]

#print len(Eratosthenes(1000000)) # 意外と時間掛からなかった。以前 Euler27 で作ったやつは、% 使ってたから異常に遅かったのかも。

prime_list = Eratosthenes(10**6)
num_strlist = ["1","3","7","9"]

def repeatedPermutationStr(L,a): # L: 文字列のリスト --> a 個の文字を選んで並べた重複順列の文字列
    if a == 0:
        return [""]
    else:
        return [top + btm for top in L
                          for btm in repeatedPermutationStr(L,a-1)]

def cyclic(s):
    length = len(s)
    ss = s + s
    return [ss[i:i+length] for i in range(length)]

ans = [2,3,5,7]
for digit in range(2,7):
    for i,lead in enumerate(num_strlist):
        kouho_tmp = repeatedPermutationStr(num_strlist[i:],digit-1)
        kouho = [lead + str for str in kouho_tmp] # 巡回的に入れ替えるので、先頭は最小数にしてしまってよい。
        print kouho
        for s in kouho:
            cycles = cyclic(s)
            if all(p in prime_list for p in cycles):
                ans += [int(p) for p in cycles]
   
print ans
print len(ans) # うわあ。劇的に遅い上に、重複があるよ。もとシンプルに変えよう。

