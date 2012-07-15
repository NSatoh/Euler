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

for num in range(3,max_val): #工夫の欠片もねえ。なさすぎて遅い。なんとかならんか。
    l = num_to_list(num)
    s = sum([factorial[i] for i in l])
    if num_to_list(s) == l:
        ans += num
        answer_list += [num]

print answer_list
print ans


