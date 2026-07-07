import json
from pathlib import Path

database = "school_data.json"
data = {"students" : [], "teachers" : []}

if Path(database).exists():
    with open(database,'r') as file:
        content = file.read()
        if content:
            data = json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent = 4)


class Student:
    def register(self):
        name = input("\nEnter student's name :-")
        age = input("Enter student's age :-")
        email = input("Enter student's email :-")
        rollno = input("Enter student's roll number :-")

        if not ("@" in email and "." in email):
            print("\nInvalid Email")
            return
        
        for i in data['students']:
            if i['rollno'] == rollno:
                print("\nStudent already exists")
                return 

        data['students'].append({
            "name" : name,
            "age" : age,
            "email" : email,
            "rollno" : rollno,
            "grades" : {}
        })

        save()
        print(f"\nStudent {name} registered")

    def grade(self):
        rollno = input("\nEnter student's roll number :- ")

        for i in data['students']:
            if i['rollno'] == rollno:
                subject = input("Subject :- ")
                marks = float(input("Marks :- "))
                i['grades'][subject] = marks
                save()
                print("\nGrades added successfully")
                return
        print("\nStudent not found")

    def details(self):
        rollno = input("\nEnter student's roll number :- ")
        
        for i in data['students']:
            if i['rollno'] == rollno:
                print(f"\n   Name : {i['name']}")
                print(f"   Age : {i['age']}")
                print(f"   Roll number : {i['rollno']}")
                print(f"   Grades : {i['grades']}")
                print(f"   Email ID : {i['email']} \n")
                return
        print("Student not found")



class Teacher:
    def register(self):
        name = input("\nEnter teacher's name :-")
        age = input("Enter teacher's age :-")
        email = input("Enter teacher's email :-")
        empid = input("Enter teacher's employee id :-")

        if not ("@" in email and "." in email):
            print("\nInvalid Email")
            return
        
        for i in data['teachers']:
            if i['empid'] == empid:
                print("\nteacher already exists")
                return

        data['teachers'].append({
            "name" : name,
            "age" : age,
            "email" : email,
            "empid" : empid,
        })
        save()
        print(f"\nTeacher {name} registered")

    def details(self):
        empid = input("\nEnter teacher's employee id :- ")
        for i in data['teachers']:
            if i['empid'] == empid:
                print(f"\n   Name : {i['name']}")
                print(f"   Age : {i['age']}")
                print(f"   Employee ID : {i['empid']}")
                print(f"   Email ID : {i['email']} \n")
                return
        print("Teacher not found")
        



stud = Student()
teach = Teacher()


while True:
    print("Press 1 to register a student")
    print("Press 2 to register a teacher")
    print("Press 3 to add a student's grade")
    print("Press 4 to show a student's details")
    print("Press 5 to show a teacher's details")
    print("Press 6 to exit")
    try:
        choice = int(input("\nPlease input your choice :- "))
    except ValueError:
        print("Please enter a number")
        continue 

    if choice == 1:
        stud.register()

    elif choice == 2:
        teach.register()

    elif choice == 3:
        stud.grade()

    elif choice == 4:
        stud.details()

    elif choice == 5:
        teach.details()

    elif choice == 6:
        print("Exit")
        break

    else:
        print("Wrong Choice")

