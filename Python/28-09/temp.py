# counter = {}
# for i in [12,3,12,44,3,44,34,23,55,34]:
#     if i in counter:
#         counter[i] += 1
#     else:
#         counter[i] = 1

# print("counter : ", counter)

def maxDepth(s : str):
    depth_count = 0
    maximum_depth = 0
    for i,ch in enumerate(s):
        if ch == "(":
            depth_count +=1
            if(maximum_depth < depth_count):
                maximum_depth = depth_count
        elif ch == ")":
            depth_count -=1
    return maximum_depth

print(maxDepth("() + (1 + (1 + 3) - 1) * (12 * 3(2 + (2 - 23)))"))