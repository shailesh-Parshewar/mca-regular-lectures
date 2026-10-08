# 4 : count vowels in a text
text = input("enter a sentence : ")
vowels = "aeiou"
count = 0
for i, ch in enumerate(text):
    if ch in vowels or ch in vowels.upper():
        count +=1

print(count)

# 4 : medium difficulty
text = input("enter a sentence : ")
vowels = "aeiou"
count = 0
completeCount = {}
for i, ch in enumerate(text):
    if ch in vowels or ch in vowels.upper():
        count +=1
        if ch in completeCount:
            completeCount[ch] +=1
        else:
            completeCount[ch] = 1

print(count)
print(completeCount)