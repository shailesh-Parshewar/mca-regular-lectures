rows = int(input("enter number or rows : "))

for i in range(1, rows+1):
    print("  "*int((rows)- i), end="")
    for j in range(1, i//2):
        print(f" {j}  ", end="")
    
    print()