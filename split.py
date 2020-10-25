import os
#序列分割
import sys

limit=2000
file_count=1000
list_seq=[]
path='nucleotide/seq'

with open('nucleotide/count_less.fasta') as f:
#with open('testdata/test_split.fasta') as f:
    for line in f:
        list_seq.append(line)
        if len(list_seq)<limit:
            continue
        file_name=path+'/'+str(file_count)+'.fasta'
        with open(file_name,'w') as file:
            for seq in list_seq[:-1]:
                file.write(seq)
            file.write(list_seq[-1].strip())
            list_seq=[]
            file_count+=1000
if list_seq:
    file_name=path+'/'+str(file_count)+'.fasta'
    with open(file_name,'w') as file:
        for seq in list_seq:
            file.write(seq)
print('done') 
'''
#wuhan1源文件蛋白质文件分割
limit=2
#file_count=1000
list_seq=[]

with open('out.fasta') as f:
#with open('testdata/test_split.fasta') as f:
    for line in f:
        list_seq.append(line)
        if len(list_seq)<limit:
            continue
        index=list_seq[0].find('gene=')
        end=list_seq[0].find(']')
        file_name=str(list_seq[0][index+5:end])+'.fasta'
        if os.path.exists(file_name):
            file_name=file_name+'(1)'
            with open(file_name,'w') as file:
                for seq in list_seq[:-1]:
                    file.write(seq)
                file.write(list_seq[-1].strip())
                list_seq=[]
        else:
            with open(file_name,'w') as file:
                for seq in list_seq[:-1]:
                    file.write(seq)
                file.write(list_seq[-1].strip())
                list_seq=[]
            #file_count+=1000
if list_seq:
    if os.path.exists(file_name):
        file_name=file_name+'(1)'
    else:
        index=list_seq[0].find('gene=')
        end=list_seq[0].find(']')
        file_name=str(list_seq[0][index+5:end])+'.fasta'
        with open(file_name,'w') as file:
            for seq in list_seq:
                file.write(seq)
print('done') 
'''