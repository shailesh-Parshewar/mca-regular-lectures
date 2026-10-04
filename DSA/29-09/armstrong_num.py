# Take an int input
num = int(input("enter a number : "))
#  counting digits
p = len(str(num))
n = num
sum = 0
while num > 0:
    sum += (num % 10)**p
    num //= 10

print("is armstrong number : ", sum == n)