

# n = int(input("Enter rows : "))

# num = 0

# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+num), end=" ")
#         num +=1
#     print()

n = int(input("Enter rows: "))

for i in range(n):
    print("  "*(n - i + 1), end=" ")
    for j in range(2*i + 1):
        if i < n - 1:
            if j == 0 or j == 2*i:
                print(chr(65+j), end=" ")   
            else:
                print(" ", end=" ")
        else:
            print(chr(65+j), end=" ")
    print()

