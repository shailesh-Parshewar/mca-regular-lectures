
rows = int(input("enter number of rows (odd number) : "))

for i in range(rows//2):
    print("  "*int((rows/2) -  i), end="")
    if i == 0 :
        print("  * ")
    else:
        print("  * ", "  "*(i -1), end="")
        print("  "*(i - 1), "* ")
for i in range(rows//2, -1, -1):
    print("  "*int((rows/2) -  i), end="")
    if i == 0 :
        print("  * ")
    else:
        print("  * ", "  "*(i -1), end="")
        print("  "*(i - 1), "* ")