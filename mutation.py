#突变统计代码
import sys
import re

f=open(sys.argv[1],'r')
g=open(sys.argv[2],'w')

list=[]
for data in f.readlines():
    data=data.strip()
    if data.find('Query')!=-1:
        if data[0]=='Q':
            strain=data.split()[1]
        else:
            strain=data.split()[3]
        #print(strain)
    else:
        if not len(data):
            continue
        #以空格为分，只分两份
        list=data.split("\t",1)
           
        #print(data.split()[0]+','+data.split()[1])
        #print(str(data.split()[0])+','+data.split()[1])
        print(strain+','+list[0]+','+list[1])
       