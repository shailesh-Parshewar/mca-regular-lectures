# List methods: append, insert, remove

li = ["red", "berry", "mango"]

# append appends an element at the end of the list
li.append("banana")
li.append("kiwi")

print("append ")


# insert
li.insert(2, "burger")
li.insert(1,"tomato")
print()




# create a list of ten numbers
# print the sum of last four elements of the list
# find out the difference between min and max of the list
# insert an element in the list at 6th position, this number must be one-third of number stored at 4th position 
nums = [0,67,-12,5,23,87, 11, 9]

sum_of_last_four = sum(nums[-4:])
print("sum of last four : ", sum_of_last_four)

diff = sorted(nums)[-1] - sorted(nums)[0]
print("difference between min and max : ", diff)

nums.insert(5, nums[3]/3)
print("nums after inserting at 6th : ", nums)

strs = "dsfkjhwewrshv"

sorted_str = sorted(strs)
print("sorted string : ", sorted_str)
