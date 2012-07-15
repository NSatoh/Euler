'''
Created on 2012/05/06

@author: NSatoh
'''

def digit_pow_sum(n,pow):
    tmp_n = n
    tmp_d = tmp_n % 10
    tmp_sum = tmp_d**pow
    while tmp_n >= 10:
        tmp_n = (tmp_n - tmp_d)/10
        tmp_d = tmp_n % 10 
        tmp_sum += tmp_d**pow
    return tmp_sum

N = 5

upperBound = 1
nine_pow_N = 9**N
k = nine_pow_N

while k >= 10**upperBound:
    k += nine_pow_N
    upperBound += 1

#print upperBound
#print k

kekka = 0
for n in range(10,k):
    if digit_pow_sum(n,N) == n:
        print n
        kekka += n 

print "sum --> " + str(kekka)

