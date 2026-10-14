

with open("project_guide.txt") as f:
    lines = f.readlines() # read lines as list of strings
    line_count = len(lines) 

    print("2nd line : ", lines[1])
    print("4th line : ", lines[3])

    
