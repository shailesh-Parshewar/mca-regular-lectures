
rows = int(input("enter an odd rows number : "))

for i in range(rows):
    if i == rows // 2:
        print(" * "*rows)
    else:
        print("   "*int(rows/2), end="")
        print(" * ")
