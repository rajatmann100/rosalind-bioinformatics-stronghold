# read file
file = open("./data/rosalind_grph.txt", "r")
input_str = file.read()
# print(input_str)
# print(matchSuffPref("AAATAAA", "AAATTTT"))
gene_arr = input_str.split(">")
gene_arr = gene_arr[1:]
# print(gene_arr)


def matchSuffPref(x, y):
    if(x[-3:] == y[:3]):
        return True
    return False


def makeCombinationPairs(arr):
    if(len(arr) == 1):
        return None
    for x in arr[1:]:
        processGene(arr[0], x)
        processGene(x, arr[0])
    return makeCombinationPairs(arr[1:])


def processGene(x, y):
    if(matchSuffPref(x[13:].strip(), y[13:].strip())):
        print(x[:13], y[:13])
    # print(x[13:].strip(), y[13:].strip())
    # print(matchSuffPref(x[13:].strip(), y[13:].strip()))


makeCombinationPairs(gene_arr)
