# read file
file = open("./data/rosalind_hamm.txt", "r")
input_file = file.read()
print(input_file.split("\n"))

input_arr = input_file.split("\n")
count = 0
for i in range(len(input_arr[0])):
    # print(i, input_arr[0][i], input_arr[1][i])
    if(input_arr[0][i] == input_arr[1][i]):
        count += 1

print(len(input_arr[0])-count)
