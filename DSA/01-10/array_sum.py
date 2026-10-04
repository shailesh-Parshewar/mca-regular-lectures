
array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)
sum = 0
for item in array:
    sum += item

print("sum is : ", sum)