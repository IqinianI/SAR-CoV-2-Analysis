import sys
#去空行
'''
f=open(sys.argv[1],'r')
w=open(sys.argv[2],'w')

for line in f.readlines():
    line=line.strip()  
    w.write(line)
'''
#取子串
'''
g=open(sys.argv[1],'r')
for line in g.readlines():
    if line[0]!='>':
        
        seq=line
        RBD=seq[329:582]
        S2=seq[661:1269]
        print(RBD)
        print(S2)
'''

#
g=open(sys.argv[1],'r')
w=open(sys.argv[2],'w')
for line in g.readlines():
    if line[0]=='>':
        line=line.split('|')[0]
        w.write(line+'\n')
    else:
        w.write(line)
        