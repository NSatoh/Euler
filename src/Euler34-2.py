#coding:utf-8
'''
Created on 2012/07/15

@author: NSatoh
'''

def num_to_list(num):
    L = []
    while num > 0:
        m = num % 10
        L = [m] + L
        num = (num - m)/10
    
    return L

a = 1
factorial = [1]
for i in range(1,10):
    a *= i
    factorial += [a]

print factorial
# print a
max_val = a * 7    
ans = 0
answer_list = []

#for num in range(3,max_val): #工夫の欠片もねえ。なさすぎて遅い。なんとかならんか。
#    l = num_to_list(num)
#    s = sum([factorial[i] for i in l])
#    if num_to_list(s) == l:
#        ans += num
#        answer_list += [num]


# 上の方法は、
#    数字 --> リスト --> 階乗和 --> 元の数字？ --yes--> 加える
# という流れ。数字を片っ端から調べているが、桁を並べ替えただけの数は階乗和も同じになるので、何回も調べるのは無駄。
# （7桁の異なる数だと、7!回も調べている。超無駄。）
# なので、やり方を変えよう。数字からリストを作るのでなく、最初からリストを生成。重複組合せ的に、ソートされた状態のリストを作る。で、
#    リスト --> 階乗和 --> ソート --> 元のリスト？ --yes-->階乗和を加える
# てな方針で。従って、桁数ごとにまわす。

def repeatedCombList(L,a): 
    if a == 0:
        return [[]]
    else:
        return [[top] + btm for i,top in enumerate(L)
                                      for btm in repeatedCombList(L[i:],a-1)]
        
for digit in range(2,8):
    numList = repeatedCombList(range(10),digit)
    for l in numList:
        s = sum([factorial[i] for i in l])
        sorted = num_to_list(s)
        sorted.sort()
        if sorted == l:
           ans += s
           answer_list += [s]


print answer_list
print ans


