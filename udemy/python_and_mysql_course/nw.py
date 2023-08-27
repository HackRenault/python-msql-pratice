inputs = {}  # Create an empty dictionary to store the inputs

for i in range(3):
    user_input = input("Enter key-value pair (key:value): ")
    key, value = user_input.split(":")
    inputs[key] = value

print("Dictionary:", inputs)

Student_Register = {}

def Student_Register_User():
    name = input("Enter your Name: ").upper()
    clas = input("Enter your Class: ")
    score = float(input("Enter Student Score: "))

    # Create a dictionary to store the user's information
    user_info = {
        'Name': name,
        'Class': clas,
        'Score': score
    }

    # Add the user's information to the Student_Register dictionary
    Student_Register[name] = user_info

    print("User registered successfully!")
    
def Average_Class():
    # Retrieve the values of "score" from the dictionary
    scores = [student['Score'] for student in Student_Register.values()]
    score = 0
    for i in scores:
        score += i
    #  To find the average we divide the score by the length of scores
    Average = score/len(scores)
    print(Average)


def Highest_score():
    # Initialize variable for tracking the lowest score and its corresponding student name
    highest_score = float('-inf') # to ensure that any score encoutered is higher than the initial value
    highest_score_name = ''
    # iterate over dictionary to find the highest score
    for student in Student_Register.values():
        score = student['Score']
        name = student['Name']
    # find the highest score
        if score > highest_score:
            highest_score = score
            highest_score_name = name         
    print(highest_score_name, "has the Highest Score with", highest_score, "points")
    
def Lowest_score():
    scores = [student['Score']for student in Student_Register.values()]
    # find the lowest score
    lowest_score = min(scores)
    print("lowest Score:", lowest_score)

#Main Program Here
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
        Student_Register_User()
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



# # Retrieve the dictionary values and convert them to a list
# register_list = list(Student_Register.values())

# # Print the list vertically
# for item in register_list:
#     print(item)

