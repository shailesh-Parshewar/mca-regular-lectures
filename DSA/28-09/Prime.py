
num = int(input("enter a number : " ))
isPrime = True
for i in range(2,(num//2) + 1):
    if num % i == 0 :
        isPrime = False
        break


if isPrime == False:
    print("Not Prime")
else:
    print("Prime")
