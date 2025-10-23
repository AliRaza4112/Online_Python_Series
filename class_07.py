# New Type
# List - Mutable Type 
# In context of other languages: Array

fruits = ["apple", "banana", "Mango"]

# Exalmple of Students

student1 = "Ahmed"
student2 = "Ali"
student3 = "Noor"
student4 = "Muntazir"
student5 = "Faiq"
student6 = "Sarfaraz"

# print(f"Student 1: {student1}")
# Index       0      , 1    ,   2  ,   3   ,   4   ,   5
students = ["Ahmed", "Ali", "Noor", "Muntazir", "Faiq", "Sarfaraz"]
print(students, "Original List")




# Adding new student to the list
students.append("Shayan")
# List After Append ['Ahmed', 'Ali', 'Noor', 'Muntazir', 'Faiq', 'Sarfaraz', 'Shayan']
print(students , "List After Append")
students.extend(["Safeer", "Tanveer"])
print(students , "List After Extend")
# List After Extend ['Ahmed', 'Ali', 'Noor', 'Muntazir', 'Faiq', 'Sarfaraz', 'Shayan','Safeer','Tanveer']
students.insert(2, "Yasir")
print(students , "List After Insert")

# Removing Students from the list
students.remove("Tanveer")
print(students , "List After Removal")

students.pop()
print(students , "List After Pop")  

del students[1]
print(students , "List After Del")

# updating a student name
students[5] = "Zeeshan"
print(students , "List After Update")

# Slicing 
print(students[149:201] , "List After Slicing")
print(students[149:])
print(students[:51] , "List After Slicing from start")


print(students[0:201:3],"List After Slicing with step 2")