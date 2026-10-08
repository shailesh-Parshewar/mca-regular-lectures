
arr = [10,20,30,40,50,60]
flag = True
sum = 0
for i in arr:
    sum += i if flag else 0
    flag = False if flag else True

print(sum)


def factorial(n):
    acc = 1
    for i in range(n, 1, -1):
        acc *= i
    print(acc)
    return acc

factorial(10)

