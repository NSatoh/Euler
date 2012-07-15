'''
Created on 2012/01/04

@author: NSatoh
'''

F = [1,1]

i = 2
fib = 1
while fib < 10**(999):
   F = F + [F[i-1]+F[i-2]]
   fib = F[i]
   i = i + 1

print i