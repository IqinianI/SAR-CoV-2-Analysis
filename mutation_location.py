#!/usr/bin/python
import sys

f = open(sys.argv[1],"r")
##read blast alignment result eg: *.blast.log
data = f.readlines()
g = open(sys.argv[2],"w")
##output the mutation file eg: *.mut

for i in range(0,len(data)) :
    if data[i].find("Query=")!=-1 or data[i].find(">")!=-1:
        #g.write("\n"+data[i])
        query=data[i].split()[1]
#     elif data[i].find("Identities")!=-1:
#         g.write("\n")
    else:
        tag = 3
        while data[i].find("|||||") != -1:
            mutation_query = data[i-1]
            mutation_result = data[i][14:-1]
            mutation_sub = data[i + 1]
            if tag == 3:
                start_sub = int(mutation_sub.split()[1])
                pos = start_sub
            if mutation_result.find(" ") == -1:
                '''
                #process whether there are some insertions or deletions
                
                if mutation_query.find("-") != -1:
                    del_loc = mutation_query.find("-") # deletion starts here
                    start_query = int(mutation_query.split()[1])
                    start_del_on_query = start_query +
                    g.write()
                # if no in-del, do:
                '''
                break
            #if mutation_result.find(" ") != -1:
            else:
                mutation_result = mutation_result.find(" ")#mutation location
                # mutation_sub = data[i + 1]
                if tag == 3:
                    pos += mutation_result
                ori = mutation_sub.split()[2][mutation_result]
                cur = mutation_query.split()[2][mutation_result]
                if ori == '-' and tag ==3:
                    g.write("\n"+query+'\t'+str(pos) + "\t" + "Insertion" + "\t" + cur)
                    tag = 0
                elif ori == '-' and tag == 0:
                    g.write(cur)
                    if data[i][14 + mutation_result+ 1] == '|':
                        tag = 3
                elif cur == '-' and tag == 3:
                    g.write("\n"+query+'\t'+str(pos) + "\t" + ori)
                    tag = 1
                elif cur == '-' and tag == 1:
                    g.write(ori)
                    if data[i][14 + mutation_result+ 1] == '|':
                        g.write("\t" + 'Deletion' + "\n")
                        tag = 3
                elif cur != '-' and ori != '-' and tag == 3 and cur!='N' and cur!='n':
                    g.write("\n"+query+'\t'+ str(pos) + "\t"+ ori + "\t"+cur+"; ")
                    tag = 2
                    if data[i][14 + mutation_result + 1] == '|' :
                        tag = 3
                elif cur != '-' and ori != '-' and tag == 2 and cur!='N' and cur!='n':
                    g.write(ori + "\t" + cur + ";")
                    if data[i][14 + mutation_result + 1] == '|':
                        tag = 3
                data[i] = data[i][:14 + mutation_result] + '|' + data[i][15 + mutation_result:]
        #break
        #data[i] = data[i][:-1]
f.close()
g.close()