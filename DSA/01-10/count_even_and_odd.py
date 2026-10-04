
array = []
n = int(input("enter size of array : "))

for i in range(n):
    element = int(input(f"enter element no. {i+1} : "))
    array.append(element)

counter  = {
    "even" : 0,
    "odd" : 0
}

for item in array:
    if item % 2 == 0:
        counter["even"] += 1
    else:
        counter["odd"] += 1
print("counter : ", counter)
