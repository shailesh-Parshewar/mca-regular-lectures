
array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)

num = int(input("element to search : "))
for index, item in enumerate(array):
    if num == item:
        print("found the element at ", index)
        break
    