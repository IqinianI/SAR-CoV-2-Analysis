import sys
from Bio import SeqIO

f=open(sys.argv[1],'r')
g=open(sys.argv[2],'w')

#方法一：用SeqIO，速度快

seq_record=SeqIO.parse(f,'fasta')

count=0
for record in seq_record:
    count+=1
    if count<=1000:
        g.write('>'+record.id+'\n')
        g.write(str(record.seq)+'\n')
  

#方法二：直接按行读写，速度慢
'''
count=0
line=f.readlines()

for i in range(len(line)):
    
    if line[i][0]=='>' and count<3:
        count+=1
        print(line[i],end='')
        print(line[i+1],end='')
'''

            
    
