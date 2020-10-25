
from Bio import SeqIO,SeqFeature
import sys
ref_f=open(sys.argv[1],'r')
ref_g=open(sys.argv[2],'a')
#record=SeqIO.read(ref_f,'genbank')
record=SeqIO.parse(ref_f,'genbank')
#print(record.features[4])
list_keys=['gene','locus_tag','product','protein_id']


rec=next(record)

port_seq=rec.features[3].qualifiers['translation'][0]
i=0


for f in rec.features[4:19]:
    
    list_values=[]
    #list_values=[f.qualifiers[x][0] for x in list_keys]
    for x in list_keys:
        if x=='product':
            
            if f.qualifiers[x][0][0]!='n':
                
                list_values.append(f.qualifiers['note'][0][0:5])
            else:
                list_values.append(f.qualifiers[x][0][0:5])
        else:
            list_values.append(f.qualifiers[x][0])
    list_values.append(int(f.location.start))
    list_values.append(int(f.location.end))
    #print(list_values)
    ref_g.write('>lcl|NC_045512.2_prot_'+list_values[3]+' [product='+list_values[2]+'] '+'[location='+str(list_values[4]+1)+'..'+str(list_values[5])+']'+'\n')
    #print(list_values[4]-265)
    i=i+1
    if i==11:
        i+=1
    else:
        stri=str('sequences/Protein/NSP/sequence-'+str(i)+'.fasta')    
    g=open(stri,'r')
    for ref in g.readlines():

        if ref[0]!='>' and ref!='':
            ref_g.write(ref)
    #ref_g.write('\n')
        
##手动加入S蛋白RBD和S2
'''
##读取并写入文件
#ref_prot=open(sys.argv[2],'r')
list_test=''
ref_port=open('mutations/ref_port.txt','r')
for ref in ref_port.readlines():
    if ref[0]=='>':
        print(ref.strip())
        list_test=''
        #print(list_test)
        #print(len(list_test))
        #list_test=''

    else:
        list_test+=ref.strip()
        print(list_test)

'''
    


    
    
