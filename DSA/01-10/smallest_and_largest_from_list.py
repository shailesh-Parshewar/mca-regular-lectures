
array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)

# array
sm = array[0]
lg = array[0]

for item in array:
    if item > lg:
        lg = item
    if item < sm:
        sm = item


ssm = array[0]
slg = array[0]
for item in array:
    if item > slg and item < lg:
        slg = item
    if item < ssm and item > sm:
        ssm = item


print("smallest : ", sm)
print("largest : ", lg)
print("second smallest : ", ssm)
print("second largest : ", slg)