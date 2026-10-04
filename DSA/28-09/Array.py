# Create Array and find min and max
arr = [12,4,356,0,-12,4,23,67]

min = arr[0]
max = arr[0]

print()
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print("min : ", min)
print("max : ", max)

# Find second min and max
smin = arr[0]
smax = arr[0]
for i in arr:
    if i > smax:
        if (i < max):
            smax = i
    if i < smin:
        if (i > min):
            smin = i

print("second min : ", smin)
print("second max : ", smax)