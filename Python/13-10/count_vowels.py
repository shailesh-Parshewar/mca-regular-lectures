
with open("project_guide.txt") as f:
    content = f.read()
    vowels = "aeiou"
    count = 0
    for i , ch in enumerate(content):
        if ch in vowels or ch in vowels.upper():
            count +=1

print("vowels count : ", count)