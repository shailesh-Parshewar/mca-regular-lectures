array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)

zeroes = []
non_zeroes = []
for item in array:
    if item == 0:
        zeroes.append(0)
    else:
        non_zeroes.append(item)


non_zeroes.extend(zeroes)
print(non_zeroes)