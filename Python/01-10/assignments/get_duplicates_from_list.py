
# 5 : get duplicates from list
li2 = [12,32,34,75,12,12,75,87]
occurences = []
duplicates = []
for i in li2:
    if i in occurences:
        duplicates.append(i) if i not in duplicates else None
    else:
        occurences.append(i)
print("DP : ", duplicates)
print("OC : ", occurences)
print("OG : ", li2)
