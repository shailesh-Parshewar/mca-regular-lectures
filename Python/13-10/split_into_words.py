
with open("project_guide.txt") as f:
    content = f.read()
words = content.split()

print("number of words : ", len(words))

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("unique words in file : ", unique_words)