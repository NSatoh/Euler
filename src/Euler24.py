'''
Created on 2011/12/24

@author: NSatoh
''' 

n = 10
M = 1000000
the_perm = ""
factorial = 1
i = 1
fac = [1]
while factorial < M:
    i = i + 1 
    factorial = factorial * i
    fac = fac + [factorial]
    print fac
if i > n:
    print "M is too large, or n is too small"
elif i < n:
    for j in range(n-1,i-1,-1):
        the_perm = the_perm + str(j)+","
    n = i

perm_num = range(n)

print the_perm
print fac

print perm_num
print "n="+str(n)
for dummy in range(len(perm_num)):
    for i in range(1,n+1):
        if fac[n-2]*i >= M:
            the_perm = the_perm + str(perm_num[i-1])+"," 
            del perm_num[i-1] 
            M = M - fac[n-2]*(i-1)
            n = n - 1
            print perm_num
            break
           
print the_perm
            