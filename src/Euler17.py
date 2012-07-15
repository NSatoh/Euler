'''
Created on 2011/09/25

@author: NSatoh
'''

adata = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
a = [0] + map(len,adata.split())

bdata = "twenty thirty forty fifty sixty seventy eighty ninety"
b = [0,0] + map(len,bdata.split())

print a
print b
#a = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,8,8]

one_thousand = 3 + 8
hundred_and = 7 + 3


def count(n):
    cnt = 0
    hyaku = 0
    juu = 0
    ichi = n
    if n >= 100:
        hyaku = int(str(n)[0])
        if n - 100*hyaku >= 20:
            juu = int(str(n)[1])
            ichi = int(str(n)[2])
        else :
            ichi = n - 100*hyaku
        cnt = cnt + hundred_and 
    elif n >= 20:
        juu = int(str(n)[0])
        ichi = int(str(n)[1])
    cnt = cnt + a[hyaku] + b[juu] + a[ichi]
    if n % 100 == 0:
        cnt = cnt - 3
    print str(n) + ":" + str(cnt) 
    return cnt

sum = 0
for n in range(1,1000):
    sum = sum + count(n)

sum = sum + one_thousand

print sum