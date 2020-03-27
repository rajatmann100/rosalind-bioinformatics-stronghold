# read file
file = open("./data/rosalind_rna.txt", "r")
input_str = file.read()
print(input_str)

rna_str = ''
for x in input_str:
    if(x != "\n"):
        if(x == "T"):
            rna_str += "U"
        else:
            rna_str += x

print(rna_str)
