# 5 : get unique elements from a list
li1 = [12,12,43,2,433,43,34,17,2]
uniques =  []
for i in li1:
    if i not in uniques:
        uniques.append(i)

print(uniques)
