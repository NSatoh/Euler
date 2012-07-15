#coding:utf-8
'''
Created on 2011/09/23

@author: School
'''

f = [1,2]
tmp = 2
i = 1
sum = 0
while tmp <= 4000000:
    i = (i+1) % 2
    sum = sum + tmp * ( (tmp+1) % 2 )
    #print "tmp = " + str(tmp) + "; sum = " + str(sum)
    tmp = f[0] + f[1]
    f[i] = tmp
    
print sum
    