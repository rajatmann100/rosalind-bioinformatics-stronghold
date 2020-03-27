# read file
file = open("./data/rosalind_subs.txt", "r")
input_str = file.read()

big_gene = input_str.split("\n")[0]
small_gene = input_str.split("\n")[1]

matches = ''

for i in range(len(big_gene)):
    if(small_gene == big_gene[i:i+len(small_gene)]):
        matches += str(i+1)+" "
    # print(i, big_gene, big_gene[i:i+len(small_gene)])

print(matches)
