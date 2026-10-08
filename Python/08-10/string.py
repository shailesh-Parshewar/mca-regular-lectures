# String methods: strip, lower, upper, capitalize, replace, split, partition, count, find, startsWith, endsWith

text = "this Text is for Test!   "

# strip strips trailing spaces on both ends of a string
print("strip : ", text.strip())

# upper converts everything into upper case
print("upper : ", text.upper())

# lower converts everything into lower case
print("lower : ", text.lower())

# capitalize capitalizes first letter of entire string
# doesn't work if trailing spaces prefix the string
print("capitalize : ", text.capitalize())

# replace replaces part of a string with another string
print("replace : ", text.replace("this", "these"))

# split splits a string into a list based on a separator
# it separates based on space if no separator is provided
print("split : ", text.split())

# partition partitions a string into three parts, that is, before a separator, separator, after a separator
# it always divides a string into three parts only unlike split
print("partition : ", text.partition("is"))

# count counts occurances of a substring inside some string
print("count : ", text.count("t"))

# find returns the index of first occurence of a substring inside a string
print("find : ", text.find("for"))

# startswith checks if a string starts with a substring
print("startsWith : ", text.startswith("for"))

# endswith checks if a string ends with a substring
print("endsWith : ", text.endswith("for"))

