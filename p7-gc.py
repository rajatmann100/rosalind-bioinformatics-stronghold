# read file
file = open("./data/rosalind_gc.txt", "r")
input_str = file.read()
# print(input_str)

gene_arr = input_str.split(">")
gene_arr = gene_arr[1:]
# print(gene_arr)


def calcGC(gene):
    t = 0
    gc = 0
    for x in gene:
        if(x != "\n"):
            t += 1
            if(x == "C" or x == "G"):
                gc += 1
    # print(t, gc)
    return (gc/t)*100


longest_gene = ''
max_perc = 0
for g in gene_arr:
    p = calcGC(g[13:].strip())
    if(p > max_perc):
        max_perc = p
        longest_gene = g[:13]
    # print(g[13:].strip())

print(longest_gene)
print(max_perc)
