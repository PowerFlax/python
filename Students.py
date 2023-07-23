import math
import time
#I might use a class to integrate the concept of permission.
#I might add some permission to init the students only for admins.

Students = []

def init_students():
    name = input("What's the student's name ?")
    age = int(input("What's the age of the student ?"))
    id = int(input("Give the student an id ?"))

    while True:
        if any(student["id"] == id for student in Students):
            print("This id is already used")
            id = int(input("Give the student another id."))
        else:
            break

    grade = input("Give the Student a grade (S/A+/A/B+/B/C)")

    return {"name": name, "age": age, "id": id, "grade": grade}


def best_grade():
    number = 0
    for student in Students:
        if(student["grade"] == "S"):
            number += 1

    return number

number_students = int(input("How many students ?"))


for i in range(number_students):
    print("Student number " + str(i+1))
    student = init_students()
    Students.append(student)

print("there's " + str(best_grade()) +" best grades")

"""""To show the students we have
for student in Students:
    print("Information of the Student number " + str(i+1))
    print("name: " +student["name"])
    print("age: " +str(student["age"]))
    print("id: " +str(student["id"]))
    print("grade: " +(student["grade"]))
    print("---------")
"""""