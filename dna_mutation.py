import sys
import re
f = open(sys.argv[1],"r")
data = f.readlines()
g = open(sys.argv[2],"w")

def str_append(s, n):
    output = ''
    i = 0
    while i < n:
        output += s
        i = i + 1
    return output


for i in range(0,len(data)) :
    if data[i].find("Query=")!=-1 or data[i].find(">")!=-1:
        #g.write(data[i])
        query=data[i].split()[1]
    else:
        while data[i].find("|||||") != -1:
            mutation_result = data[i][14:-1]
            mutation_query = data[i-1]
            mutation_sub = data[i + 1]
            start_sub = int(mutation_sub.split()[1])
            if mutation_result.find(" ") == -1:
                break
            #if mutation_result.find(" ") != -1:
            else:
                mutation_result = mutation_result.find(" ")#mutation loc
                #if mutation_sub.find("-")==-1 and mutation_query.find("-")==-1:
                if mutation_sub.split()[2][mutation_result]!='-' and mutation_query.split()[2][mutation_result]!='-':
                    pos=start_sub+mutation_result
                    ori = mutation_sub.split()[2][mutation_result]
                    cur = mutation_query.split()[2][mutation_result]
                    if cur!='N' and cur!='n' and cur.upper()!=ori.upper():
                        g.write(query+'\t'+str(pos) + "\t"+ ori.upper() + "\t"+cur.upper() + "\n")
                    data[i]=data[i][:14+mutation_result] + '|' + data[i][15+mutation_result:]
                else:
                
                    count=0
                    if mutation_sub.find("-")!=-1:
                        it = re.finditer(r'[-]*', mutation_sub)
                    elif mutation_query.find("-")!=-1:
                        it = re.finditer(r'[-]*', mutation_query)
                    for node in it: 
                        len_node = len(node.group(0))
                        if len_node>=1: 
                            count+=len_node
                            insert=str_append('|',count)
                            data[i]=data[i][:14+mutation_result] +insert+ data[i][14+count+mutation_result:]
                           
                
                    
                    pos = start_sub+mutation_result-1
                    ori=mutation_sub.split()[2][mutation_result-1:mutation_result+count].split('-')[0]
                    cur = mutation_query.split()[2][mutation_result-1:mutation_result+count].split('-')[0]
                    if ori!='' and cur!='':
                        g.write(query+'\t'+str(pos) + "\t"+ ori.upper() + "\t"+cur.upper() + "\n")
                    
                        
#                     if len(ori)==len(cur):
#                         pos=start_sub+mutation_result
#                         try:
#                             g.write(query+'\t'+str(pos)+'\t'+ori[1]+'\t'+cur[1]+'\n')
#                         except:
#                             continue
                    
# #                     if cur.find('-')==-1 and ori.find('-')==-1:
# #                         pos=start_sub+mutation_result
# #                         g.write(query+'\t'+str(pos)+'\t'+ori[1]+'\t'+cur[1]+'\n')

#                     else:
#                         pos = start_sub+mutation_result-1

#                         g.write(query+'\t'+str(pos) + "\t"+ ori + "\t"+cur + "\n")
f.close()
g.close()

#识别insertion和deletion
#全部装换成大写