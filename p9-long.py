########## BASE FASTA CODE - START ##########
from lib.FastaReader import FASTA
file = open("./data/data.txt", "r")
input_str = file.read()

gene_arr = input_str.split(">")
gene_arr = gene_arr[1:]
########## BASE FASTA CODE - END ##########


def processDNA(c, dna):
    print(c, dna)


for g in gene_arr:
    fs = FASTA(g)
    processDNA(fs.code(), fs.dna())
