
# # 6 : reverse a list
# li3 = [1,2,3,4,5,6]

# li3.reverse()
# print(li3)

# assignments
exit_flag = False


subjects = ("python", "DSA", "networks")
students = []

# Input function
def getStudentDetails():
    mutable_student_object = {}
    mutable_student_object["id"] = int(input("Student id : "))
    mutable_student_object["name"] = input("Student name : ")
    if "scores" not in mutable_student_object: 
        mutable_student_object["scores"] = {}
    
    for sub in subjects:
        mutable_student_object["scores"][sub] = int(input(f"{sub} : "))
    students.append(mutable_student_object)

# Input loop   
while True:
    getStudentDetails()
    
    command = input("Done? ")
    if command == "Done" or command == "y" or command == "Y":
        break

results = {
    "PASS" : [],
    "FAIL" : []
}
for std in students:
    print("std : ", std)
    sum = 0
    for sub in std["scores"]:
        sum += std["scores"][sub]
    if sum / 3 >= 50:
        results["PASS"] += std["name"]
    else:
        results["FAIL"] += std["name"]

print(results)