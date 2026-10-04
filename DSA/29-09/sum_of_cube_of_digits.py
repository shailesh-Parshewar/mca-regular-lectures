n = int(input("enter a number : "))

sum = 0
# This A.P. formula cleverly calculates sum of cube of all number from 1 to n
sum = ((n*(n+1))//2)**2

# for i in range(1, n+1):
#     sum += i**3
print("sum of cube of digits : ", sum)