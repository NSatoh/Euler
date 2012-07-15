'''
Created on 2011/09/25

@author: NSatoh
'''

date = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def uruu(month):
    uruudoshi = 0
    if month % 4 == 0:
        uruudoshi = 1
    if month % 100 == 0:
        uruudoshi = 0
    if month % 400 == 0:
        uruudoshi = 1
    return uruudoshi
monday = 0
sunday = 6

youbi = 365 % 7 # 1900,1,1 = monday
cnt = 0

for month in range(1901,2001):
    for i in range(1,13):
        if youbi == sunday:
            cnt = cnt + 1
        youbi = youbi + date[i]
        if i == 2:
            youbi = youbi + uruu(month)
        youbi = youbi % 7
        
print cnt
