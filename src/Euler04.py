'''
Created on 2011/09/23

@author: School
'''
kaibun = "0"
k = "0"

for i in range(100,999):
    for j in range(i,999):
        k = str(i*j)
        if k == k[::-1] :
            if int(k) > int(kaibun):
               kaibun = k
               product = [i,j]

print kaibun + " = " + str(product[0]) + " x " + str(product[1]) 