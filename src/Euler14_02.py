'''
Created on 2011/09/25

@author: NSatoh
'''

data = {'1':1}

#print length(data) 
tmpa = 0
for n in range(1000000):
    tmp = n
    length = 1
    while tmp>1:
        if tmp % 2 == 0:
            tmp = tmp/2
        else:
            tmp = 3*tmp + 1
        key = '%d' % tmp
        if data.has_key(key) == True:
            length = length + data[key]
            tmp = 1
        else: 
            length = length + 1
    data['%d' % n] = length 
    tmpa = max(tmpa,length)
    if tmpa == length:
        ans = [n,tmpa]
    print n
    
print ans

#"""    