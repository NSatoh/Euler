'''
Created on 2011/09/25

@author: NSatoh
'''

#def generate(n):
#    len = 1
#    if n == 1:
#        return len
#    if n % 2 == 0:
#        n = n/2
#    else:
#        n = 3*n + 1
#    len = len + generate(n)
#    return len

def generate(n,data):
    len = 1
    while n>1:
        key = '%d' % n
        if data.has_key(key) == True:
            del data[key]
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        len = len + 1
    
    return len
        

#print generate(13)

#"""

data = {}
for i in range(1,1000000):
    key = '%d' % i
    data[key] = i

#print len(data) 

tmpa = 0
while len(data)>0:
    n = int(data.keys()[-1])
    tmpb = generate(n,data)
    tmpa = max(tmpa,tmpb)
    if tmpa == tmpb:
        ans = [n,tmpa]
    #print len(data)

print ans

#"""    