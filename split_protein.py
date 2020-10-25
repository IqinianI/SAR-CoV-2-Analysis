import sys
'''
prot_list=[]
f=open(sys.argv[1],'r')
#line=f.readlines()

for i in range(len(line)+1):
    if line[i].find('>')!=-1:
        index=line[i].find('gene=')
        prot_list.append(line[i])
        
    else:
        if line[i+1][0]!='>':
            prot_list.append(line[i])
            
        else:
            print(prot_list)
            
            prot_list=[]
    
'''
fr=open(sys.argv[1],'r')
fw=open('out.fasta', 'w')
seq={}

for line in fr:
    if line.startswith('>'):    #判断字符串是否以‘>开始’
        name=str(line)  #以空格为分隔符，并取序列为0的项。
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')
fr.close()

for i in seq.keys():
    fw.write(i)
    #fw.write('\n')
    fw.write(seq[i])
    fw.write('\n')
fw.close()


        
 