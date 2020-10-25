import sys
import re
import argparse

parse = argparse.ArgumentParser(
    description="This script used for picking up the acceptable transcript and formating output.")

parse.add_argument('-c', '--cDNA', action='store_true', help="Count the transcript's cDNA length")
parse.add_argument('-C', '--CDS', action='store_true', help="Count the transcript's CDS length.[default]")
parse.add_argument('-f', '--first', action='store_true', help="Pick up the first ANN annotation.")
parse.add_argument('-o', '--out',  help="output_file.")
parse.add_argument('-i', '--inp',  help="input_file.")

args = parse.parse_args()
def ConvertAA():
    three = "Gly Ala Val Leu Ile Phe Trp Tyr Asp Asn Glu Lys Gln Met Ser Thr Cys Pro His Arg Ter"
    one = "G A V L I F W Y D N E K Q M S T C P H R Ter"
    three_3 = three.split(" ")
    one_1 = one.split(" ")
    AAHash = dict(zip(three_3, one_1))
    return AAHash

def convert(filein):
    AAHash = ConvertAA()
    AllItems = 0
    fileout = args.out
    with open(fileout, 'w') as fo:
        fo.write(
            "#CHROM	POS	ID	REF	ALT	Gene	cDNA_Change	Protein_Change	HGVS.p	prot_pos	prot_ref	prot_alt	cDNA_Position	mut_type	SID" + "\n")
        with open(filein) as fi:
            for line in fi:
                if not re.match("[#\"]", line):
                    AllItems += 1
                    tmp = line.strip().split("\t")
                    info = tmp[7].split(";")
                    #SID
                    for var in info:
                        if re.match("SID=", var):
                            sid = var.split("=")[1]
                    #找ANN
                    try:
                        transcripts = [item for item in tmp[7].split(";") if re.match("ANN", item)][0].split("=")[1].split(
                        ",")
                    except:
                        
                        continue
                    #选择第一个ANN注释

                    OutVirs = transcripts[0].split("|")
                    Gene = OutVirs[3]
                    mut_type=OutVirs[1]
                    cDNA_Position = OutVirs[11].split("/")[0]
                    cDNA_Position = "-" if cDNA_Position == "" else cDNA_Position
                    # convert amino acid
                    if len(OutVirs[10]) != 0:
                        AAchange = re.sub("[A-Z][a-z]{2}",lambda x:AAHash[x.group()],OutVirs[10])
#                         try:
#                             list1=[]
#                             it=re.finditer(r'[A-Z]|\d+',AAchange)
#                             for match in it:
#                                 list1.append(match.group())
#                             prot_ref=list1[0]
#                             prot_pos=list1[1]
#                             prot_alt=list1[2]
#                         except:
#                             continue

                    else:
                        AAchange = "-"
#                         prot_ref=''
#                         prot_pos=''
#                         prot_alt=''
                    AAchange_full = "-" if OutVirs[10] == "" else OutVirs[10]
                    #把蛋白突变分开
                    try:
                        list1=[]
                        it=re.finditer(r'[A-Z]|\d+',AAchange)
                        for match in it:
                            list1.append(match.group())
                        prot_ref=list1[0]
                        prot_pos=list1[1]
                        prot_alt=list1[2]
                    except:
                        continue

                    
                    OutVir = "\t".join(
                        [Gene, OutVirs[9],AAchange,AAchange_full,prot_pos,prot_ref,prot_alt,cDNA_Position,mut_type,sid])
                    Outmp = "\t".join(tmp[0:5])
                    fo.write("\t".join([Outmp, OutVir]) + "\n")
                    
if __name__ == "__main__":
    convert(args.inp)