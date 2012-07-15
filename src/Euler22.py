#coding:utf-8
'''
Created on 2011/12/24

@author: NSatoh
'''

file = open("names.txt","r")
names = file.read()
names = names.replace('"','')#stripだと, 先頭及び末尾の削除のみ
namelist = names.split(",")
#print namelist
namelist.sort()
print namelist
num = 1
value = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for name in namelist:
    #name_alphabet = list(name)
    #for moji in name_alphabet:
    for moji in name:
         value = value + (alphabet.find(moji) + 1)*num
    num = num + 1

print value

