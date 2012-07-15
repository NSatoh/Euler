'''
Created on 2012/01/04

@author: NSatoh
'''

def len_junkan(n):
    Q = 1
    i = 1
    loopflag = 0
    print "1/"+str(n)+" --> ",
    while loopflag == 0:
        if 10*Q % n == 0:
            print "not cyclic"
            return 0
            loopflag = 1
        if 10*Q % n == 1:
            print i
            return i
            loopflag = 1
        else:
            Q = 10 * Q % n
            i = i + 1

a = 0
for n in range(1,1001):
    if n % 2 == 0:
        b = 0
    elif n % 5 == 0:
        b = 0
    else:
        b = len_junkan(n)
        if a < b:
            a = b
            M = n

print "\n\n Max --> " + str(M) + ": length = " + str(a)
