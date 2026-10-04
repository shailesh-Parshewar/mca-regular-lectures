
# 8 : print pyramid pattern
rows2 = int(input("Enter number of rows : "))

for i in range(1,rows2+1):
    print("  "*((rows2 + 1) - i), end="")
    print(" *  "*i)


# 9 : pyramid with alternating pattern
rows2 = int(input("Enter number of rows : "))

for i in range(1,rows2+1):
    print("  "*((rows2 + 1) - i), end="")
    print(" *  "*i) if i % 2 == 1 else print(" @  "*i)
