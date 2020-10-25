from Bio import SeqIO
import sys
f=open(sys.argv[1],'r')
g=open(sys.argv[2],'w')
seq_record=SeqIO.parse(f,'fasta')
for record in seq_record:
    seq=str(record.seq.upper())
    count_n=0
    for i in range(len(seq)-1):
    
        if seq[i]=='N':
            count_n=count_n+1
            if count_n==1:
                list_i=i
        

            else:
                if seq[i+1]!='N':
                    if list_i!=0:
                        g.write(record.id+','+str(list_i)+','+str(count_n)+'\n')
                        #print(str(list_i)+':'+str(count_n))

        else:
            count_n=0
        
'''
#包括首尾N的位置和个数
count_n=0
for i in range(len(stri)-1):
    
    if stri[i]=='N':
        count_n=count_n+1
        if count_n==1:
            list_i=i
        else:
            if i+1==len(stri)-1:
                print(str(list_i)+':'+str(count_n+1))
            else:
                if stri[i+1]!='N':
                    print(str(list_i)+':'+str(count_n))

    else:
        count_n=0
'''