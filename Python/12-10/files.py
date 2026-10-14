# file operations

# how to open a file
file = open("project_guide.txt")


#  there are modes in which a file is accessed 
#  these are "w", "r", "a", "w+", "r+", "wb", "rb" amd a number of combinations of them

#  when you open a file you have to close it in order for your changes to be saved to disk, otherwise they stay in RAM (aisa kuch bola that ma'am ne)

file.close()

#  using the below syntax you can access a file object, do some operations and be assured that it'll be closed by the time the block ends
with open("project_guide.txt", "") as file:
    content = file.read()
    file.write("hello")

