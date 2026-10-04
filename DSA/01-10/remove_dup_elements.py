
array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)

uniques = []

for item in array:
    if item not in uniques:
        uniques.append(item)

print("unique elements are : ", uniques)