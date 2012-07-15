'''
Created on 2011/09/25

@author: NSatoh
'''

prod = 1
for n in range(1,101):
    prod = prod * n

print prod


sum = 0
for n in range(len(str(prod))):
    sum = sum + int(str(prod)[n])

print sum