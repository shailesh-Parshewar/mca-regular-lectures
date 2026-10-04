# 8 : print pyramid pattern
rows2 = int(input("Enter number of rows : "))

for i in range(1,rows2+1):
    print("  "*((rows2 + 1) - i), end="")
    print(" *  "*i)
