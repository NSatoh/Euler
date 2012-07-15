'''
Created on 2011/09/23

@author: School
'''

# sum_of_square(1:n) = n*(n+1)*(2*n + 1) / 6
# sum(1:n) = ( n*(n+1)/2 )^2
# hence: diff = n*(n+1)*(n*(n+1)/4 - (2*n + 1)/6)
#             = n*(n+1)*(3*n^2 - n - 2)/12

n = 100
print n*(n+1)*(3*n**2 - n - 2)/12
