def login():
    int(input("Student Number: "))
    input("Password: ")
    print("Succesfully logged in!")

def academic_records():
    pass

def course_list_preparation():
    pass

def gpa_calculator():
    pass

def student_rep_elections():
    pass

login()

isRunning = True

while isRunning:
    print("Welcome to University Registration!")
    print("------------")
    print("Registration")
    print("------------")
    print("1. Academic Records")
    print("2. Course List Preparation")
    print("3. GPA Calculator")
    print("4. Student Representative Elections")
    print("5. Logout")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice =="1":
        academic_records()
    elif choice == "2":
        course_list_preparation()
    elif choice == "3":
        gpa_calculator()
    elif choice == "4":
        student_rep_elections()
    elif choice == "5":
        login()
    elif choice == "6":
        isRunning = False
    else:
        print("Select a valid choice!")









