'''
Created on 2011/09/23

@author: School
'''

# a * b = lcm(a,b) * gcd(a,b)

def euclid(a,b):
    if b > 0:
       return euclid(b,a % b)
    else :
       return a

a = 1
for i in range(1,20):
    a = a * i / euclid(a,i)
    # print a
    
print a
    