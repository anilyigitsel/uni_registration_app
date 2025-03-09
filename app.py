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

vote_choice = None  

def student_rep_elections():
    global vote_choice  

    first_candidate = "A"
    second_candidate = "B"
    third_candidate = "C"
    forth_candidate = "D"

    print("------------------------------------------")
    print(f"Welcome to Student Representative Elections")
    print("------------------------------------------")

    print("Candidates:")
    print(first_candidate)
    print(second_candidate)
    print(third_candidate)
    print(forth_candidate)
    print()
    vote = input("Would you like to vote? (y/n): ").strip().lower()
    print()

    if vote == "y":
        if vote_choice is not None:  
            print("You have already voted.")
        else:
            vote_choice = input("Which candidate would you like to vote for?:\n").strip().upper()

            if vote_choice in {first_candidate, second_candidate, third_candidate, forth_candidate}:
                print("Your vote has been saved successfully.")
            else:
                print("Select a valid choice!")
                vote_choice = None  
                student_rep_elections()  

    elif vote == "n":
        print("Exiting the election system.")
        isRunning
    else:
        print("Invalid input! Please enter 'y' or 'n'.")
        student_rep_elections()  

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