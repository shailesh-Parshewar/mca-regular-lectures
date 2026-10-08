# 3 : print reverse of a string
str = input("enter a string : ")
rev = ""
for i in range(len(str) - 1, -1, -1):
    rev += str[i]

print(rev)
print(type(rev))