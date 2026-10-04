rows = int(input("enter number of rows : "))

for i in range(rows):
    if i == 0 or i == rows - 1:
        print(" * "*(rows))
    else:
        print(" * ", "   "*int(rows - 3), "  * ")
    