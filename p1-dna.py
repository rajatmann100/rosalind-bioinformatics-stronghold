# read file
file = open("./data/rosalind_dna.txt", "r")
input_str = file.read()
print(input_str)
dna_count = {
    "A": 0, "C": 0, "G": 0, "T": 0
}
for x in input_str:
    if(x != "\n"):
        dna_count[x] = dna_count[x]+1
count_str = str(dna_count["A"])+" "+str(dna_count["C"]) + \
    " "+str(dna_count["G"])+" "+str(dna_count["T"])
print(count_str)
