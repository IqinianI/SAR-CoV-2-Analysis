from Bio import SeqIO
import re
import sys

f=open(sys.argv[1],'r')
less=open(sys.argv[2],'w')
more=open(sys.argv[3],'w')
count=open(sys.argv[4],'w')

seq_record=SeqIO.parse(f,'fasta')

threshold=1000
string='N'
# f_less=open('nucleotide/count_less.fasta','a')
# f_more=open('nucleotide/count_more.fasta','a')
# f_count=open('nucleotide/count_n.csv','w')
f_less=less
f_more=more
f_count=count
for record in seq_record:
    count_start=0
    count_end=0
    seq=str(record.seq)
    start_index=seq.find(string)
    end_index=seq.rfind(string)
    count_n=seq.count(string)
    
    
    if start_index==0:
        i=0
        while seq[i]==string:
            count_start+=1
            i+=1
            if seq[i]!=string:
                break
        
        if end_index==len(seq)-1:
            i=len(seq)-1
            while seq[i]==string:
                count_end+=1
                i-=1
                if seq[i]!=string:
                    break
            
            count_n=count_n-count_end-count_start
            
            
        else:
            count_n=count_n-count_start

        f_count.write(record.id+','+str(count_n)+'\n')
        if count_n>threshold:
            f_more.write('>'+record.id+'\n')
            f_more.write(str(record.seq))
        else:
            f_less.write('>'+record.id+'\n')
            f_less.write(str(record.seq)+'\n')

    else:
        if end_index==len(seq)-1:
            i=len(seq)-1
            while seq[i]==string:
                count_end+=1
                i-=1
                if seq[i]!=string:
                    break
            count_n=count_n-count_end
        f_count.write(record.id+','+str(count_n)+'\n')
        if count_n>threshold:
            f_more.write('>'+record.id+'\n')
            f_more.write(str(record.seq+'n'))
        else:
            f_less.write('>'+record.id+'\n')
            f_less.write(str(record.seq+'\n'))
     


                
        
            
