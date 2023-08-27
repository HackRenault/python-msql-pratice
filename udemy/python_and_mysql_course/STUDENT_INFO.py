import getpass

"Develop a program that manges student grades. Create functions to input and store student information, calculate average grades, determine highest and lowest grades "

user_register = {}

def Register():
    print("Create username and password to login")
    username = input("Enter your username: ").lower()
    password = getpass.getpass("Enter your password: ")
    # Store Username and password to user_register dictionary
    user_register[username] = password
    print("User Registered Succesfully")

def Login():
    username = input("Enter your username: ").lower()
    password = getpass.getpass("Enter your password: ")  
    if username in user_register and user_register[username] == password:
        print("login succesful")
        while True:
            print("Welcome to INOVATE CENTRE for LEARNING (I.C.L) Grade Portal")
            print()
            print("1. Enter Student Score")
            print("2. Calculate Class Average")
            print("3. Display Highest Score")
            print("4. Display Lowest Score")
            print("5. Exit Portal")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                # Call the function to register a user
                Student_Class_Info()
            elif choice == "2":
                # Call the function to calculate average
                Average_Class()
            elif choice == "3":
                # Call the function to  display highest score
                Highest_score()
            elif choice == "4":
                # Call the function to  display lowest score
                Lowest_score()
            elif choice == "5":
                print("```Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
                continue
    else:
        attempts = 3
        while True:
            print("Invalid Username or Password")
            print("You have", attempts, "attempts remaiing.")
            User = ("Enter username again: ").lower()
            Password = getpass.getpass("Enter password again: ")
            if username in user_register and user_register[username]==password:
                print("Login Successful!")
            else:
                attempts -=1
                if attempts == 0:
                    print("ACCOUNT BLOCKED!!!")
                    break


Student_Info = {}

def Student_Class_Info():
    name = input("Enter Student Name: ").upper()
    clas = input("Enter Student Class: ").lower()
    score = float(input("Enter Student Score: "))
    
    # Create a dictionary to store the user's information
    user_info = {
        'Name': name,
        'Class': clas,
        'Score': score
    }

    # Add the user's information to the Student_Info dictionary
    Student_Info[name] = user_info

    print("Student registered successfully!")
           
    
def Average_Class():
    # Retrieve the values of "score" from the dictionary
    scores = [student['Score'] for student in Student_Info.values()]
    score = 0
    for i in scores:
        score += i
    #  To find the average we divide the score by the length of scores
    Average = score/len(scores)
    print(Average)


def Highest_score():
    # Initialize variable for tracking the lowest score and its corresponding student name
    highest_score = float('-inf') # to ensure that any score encoutered id higher than the initial value
    highest_score_name = ''
    # iterate over dictionary to find the highest score
    for student in Student_Info.values():
        score = student['Score']
        name = student['Name']
    # find the highest score
        if score > highest_score:
            highest_score = score
            highest_score_name = name         
    print(highest_score_name, "has the Highest Score with", highest_score, "points")
    
def Lowest_score():
    scores = [student['Score']for student in Student_Info.values()]
    # find the highest score
    lowest_score = min(scores)
    print("lowest Score:", lowest_score)

#Main Program Here
while True:
    print("--- Welcome to INOVATE CENTRE for LEARNING (I.C.L) ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        Register()
    elif choice == "2":
        Login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.") 



# Retrieve the dictionary values and convert them to a list
register_list = list(Student_Info.values())

# Print the list vertically
for item in Student_Info.values():
    names = item['Name']
    grade = item['Score']
    classe = item['Class']
    print (names, grade, classe)

