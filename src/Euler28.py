#coding:utf-8
'''
Created on 2012/05/06

@author: NSatoh

N = (2n+1)^2
(N-2n)xxxxxxxxxxxxxxxxxx N
  x                      x 
  x                      x
  x                      x
  x     21        25     x
  x         7   9        x
  x           1          x
  x         5 4 3        x
  x     17 16     13     x
  x                      x
  x                      x
(N-4n)(2n)^2 xxxxxxxx (N-6n)
'''




diag = 1

for n in range(1,501):
    diag = diag + 4*(2*n+1)**2 - 12*n

print diag