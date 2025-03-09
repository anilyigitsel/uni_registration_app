def login():
    print("-----------------------------------")
    print("Welcome to University Registration!")
    student_id = int(input("Student Number: "))
    input("Password: ")
    print()
    print("Succesfully logged in!")
    print()
    return student_id

courses = []

def academic_records(student_id):
    print("------------")
    print("Academic Records")
    print("------------")
    print(f"Student Number: {student_id}")
    print("--------")
    print("Courses")
    print("--------")
    if courses:  
        for index, course in enumerate(courses, start=1):
            print(f"{index}. {course}")  
    else:
        print("No courses registered yet.") 

def course_list_preparation():
    while True:  
        print("-----------------------")
        print("Course List Preparation")
        print("-----------------------")
        abb = input("Abbreviation: ")
        code = input("Code: ")  
        section = input("Section: ")
        course = f"{abb}{code}.{section}"
        
        courses.append(course)  
        print(f"{course} added successfully!")

        add = input("Do you want to add another course? (y/n): ").lower()
        if add == "n":
            break  

def student_rep_elections():
    pass

isRunning = True

student_id = login()

while isRunning:
    print("------------")
    print("Registration")
    print("------------")
    print("1. Academic Records")
    print("2. Course List Preparation")
    print("3. Student Representative Elections")
    print("4. Logout")
    print("5. Exit ")
    print() 
    choice = input("Enter your choice (1-6): ")

    if choice =="1":
        academic_records(student_id)
    elif choice == "2":
        course_list_preparation()
    elif choice == "3":
        student_rep_elections()
    elif choice == "4":
        student_id = login()
    elif choice == "5":
        isRunning = False
    else:
        print("Select a valid choice!")
        print()