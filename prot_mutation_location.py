##蛋白水平突变

import sys

f = open(sys.argv[1],"r")
##read blast alignment result eg: *.blast.log
data = f.readlines()
g = open(sys.argv[2],"w")
for i in range(0,len(data)) :
    #if data[i].find("Query=")!=-1 or data[i].find(">")!=-1:
    if data[i].find('Query=')!=-1:
        #g.write("\n"+data[i])
        #print("\n"+data[i].split()[1])
        query=data[i].split()[1]
    else:
        if data[i].find("Query") != -1:
            mutation_query=data[i]
            mutation_result=data[i+1][14:-1]
            mutation_sub=data[i+2]
            start_sub = int(mutation_sub.split()[1])
            pos = start_sub
            for i in range(len(mutation_result)):
                if mutation_result[i]==" " and mutation_query[i+14]!='X':
                    pos+=i
                    ori = mutation_sub.split()[2][i]
                    cur = mutation_query.split()[2][i]
                    g.write(query+','+str(pos)+','+ori+','+cur+'\n')
'''
    else:
        if data[i].find("Query") != -1:
            mutation_query=data[i]
            mutation_result=data[i+1][14:-1]
            mutation_sub=data[i+2]
            start_sub = int(mutation_sub.split()[1])
            pos = start_sub
            for i in range(len(mutation_result)):                    
                if mutation_result[i]==" " or mutation_result[i]=="+":
                    pos+=i
                    ori = mutation_sub.split()[2][i]
                    cur = mutation_query.split()[2][i]
                    if mutation_result[i]==" ":
                        
                        print(str(pos)+','+ori+'-->'+cur+','+' ')
                    if mutation_result[i]=="+":
                        print(str(pos)+','+ori+'-->'+cur+','+'+')
'''
