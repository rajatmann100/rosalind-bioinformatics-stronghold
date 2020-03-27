# read file
file = open("./data/rosalind_revc.txt", "r")
input_str = file.read()
print(input_str)

reverse_str = input_str[::-1]


def getComplement(bp):
    switcher = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return switcher.get(bp, "nothing")


COMP_STR = ''
for x in reverse_str:
    if(x != "\n"):
        COMP_STR += getComplement(x)

print(COMP_STR)
