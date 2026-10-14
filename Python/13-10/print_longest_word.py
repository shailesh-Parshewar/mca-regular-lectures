
str = input("enter a sentence : ")

words = str.split()
max = ""

for word in words:
    if len(max) < len(word):
        max = word

print("longest word in your string is : ", max)