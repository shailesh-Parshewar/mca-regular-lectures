
array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)

for i in range((len(array) - 1), -1, -1):
    print(array[i], end=" ")
