import random
exit_flag = False
while not exit_flag:
    true_num = random.randint(0, 10)
    num = int(input("enter number : "))
    if true_num == num:
        print("You guessed right!")
        break
    else: 
        print("try again")



name = "shailesh"
vowels = ["a","e","i","o","u"]

for v in vowels:
    name = name.replace(v, "z")
print(name)



# create a list of numbers and strings
# accept the values from user
# separate the list from the maximum number
# display the list in sorted order (descending)

li: list[str|int] = []
for i in range(5):
    str = input("enter an element : ")
    if str.isdigit():
        li.append(int(str))
    else:
        li.append(str)


alphalist = []
numlist = []
for item in li:
    if isinstance(item, int):
        numlist.append(item)
    else:
        alphalist.append(item)

alphalist = sorted(alphalist)
numlist = sorted(numlist)

print("sorted list : ", alphalist, ", ", numlist)


