import sys
f=open(sys.argv[1],'r')
g=open(sys.argv[2],'w')


g.write('#CHROM'+'\t'+'POS'+'\t'+'ID'+'\t'+'REF'+'\t'+'ALT'+'\t'+'QUAL'+'\t'+'FILTER'+'\t'+'INFO'+'\n')
#print('#CHROM'+'\t'+'POS'+'\t'+'ID'+'\t'+'REF'+'\t'+'ALT'+'\t'+'QUAL'+'\t'+'FILTER'+'\t'+'INFO'+'\n')

for line in f.readlines():
    line=line.strip()
    #print(line)
    #line_list=line.split(',')
    
    line_list=line.split('\t')
    g.write('NC_045512.2'+'\t'+line_list[1]+'\t'+'.'+'\t'+line_list[2]+'\t'+line_list[3]+'\t'+'10'+'\t'+'PASS'+'\t'+'SID='+line_list[0]+'\n')
    #if line_list[2]!=line_list[3]:
    #print('NC_045512.2'+'\t'+line_list[1]+'\t'+'.'+'\t'+line_list[2]+'\t'+line_list[3]+'\t'+'10'+'\t'+'PASS'+'\t'+'SID='+line_list[0])


       
   
    