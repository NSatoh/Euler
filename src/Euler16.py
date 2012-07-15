'''
Created on 2011/09/25

@author: NSatoh
'''

data = str(2**1000)

sum = 0
for i in range(len(data)):
    sum = sum + int(data[i])

print sum
