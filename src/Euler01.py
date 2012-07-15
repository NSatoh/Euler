#coding:utf-8
'''
Created on 2011/09/23

@author: School
'''

s = 0
for i in range(1000):
   if i%3 == 0 :
      s = s + i
   elif i%5 == 0:
      s = s + i

print s