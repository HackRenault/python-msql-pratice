import math
import random
# string=["Ben", 1, 0.5, "Paula", 8, "CLARA"]
# ring= ["Cat", 6]
# string.extend(ring)
# print(string)
# string.append(ring)
# print(string)
# string.insert(1,ring)
# print(string)
# string.remove(ring)
# print(string)
# string.pop(5)
# print(string)
# string.reverse()
# print(string)
# strin=[1,3,4,6,2,1,7,8,3,9]
# strin.sort()
# print(strin)
# strin.sort(reverse=True)
# print(strin)
# print(sorted(strin))
# print(sum(strin))
# print(min(strin))
# print(max(strin))

#DICTIONARIES
# dict={1:80,2:90}
# dict2={5:"Alx", 6:"Peter"}
# print(dict, dict2)
# print(dict[1])
# dict[3] = 45
# dict[4] = 74
# print(dict)
# print(sum(dict))
# print(4 not in dict)
# print(len(dict))
# print(dict.keys())
# print(dict.values())
# print(sum(dict.values()))
# x=dict.get(3)
# print(x)
# dict.update(dict2)
# print(dict)
# del dict[6]
# print(dict)
# del dict2
# print(dict2)
""" Retrieve the dictionary values and convert them to a list
register_list = list(Student_Register.values())

# Print the list vertically
for item in register_list:
    print(item)"""


# EVEN ={2:"TWO", 4:"FOUR", 6:"SIX", 8:"EIGHT"}
# #Display the keys.
# print(EVEN.keys())
# #Display the values.
# print(EVEN.values())
# #Display the whole dictionary.
# print(EVEN)
# #Display length of dictionary.
# print(len(EVEN))
# #Check if "3" is present in the dictionary.
# print(3 in EVEN)
# #retrieve the value for the key value 2.
# print(EVEN.get(2))

# """Write a code for a calculator where the user iputs 2 numbers and inputs
# the operation for which the program should execute & print appropriate message
# Operations: +,-,*,/
# """
# #1 Provide a msg if the user inputs the second number as 0 if division is used
# #2 Provide a msg if the user does not input a number

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# op = input("Enter the operation (+, -, x, /): ")

# if op == "+":
#     sum = num1 + num2
#     print(sum)
# elif op == "-":
#     sub = num2 - num1
#     print(sub)
# elif op == "x":
#     product = num1 * num2
#     print(product)
# elif op == "/":
#     if num2 == 0:
#         print("Division not possible by 0")
#     else:
#         div = num1 / num2
#         print(div)
# else:
#     print("Incorrect Input")


"""Questions for this assignment
Write a code in where the user inputs 3 numbers and the program prints
the number which is greater than the other & display appropriate 
message. (Copy-paste from IDE)"""

# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# n3 = int(input("Enter the third number: "))

# if n1 > n2 and n3:
#     print(f"{n1} is greater than all the numbers entered")
# elif n1 < n2 and n2 > n3:
#     print(f"{n2} is greater than all the numbers entered")
# else:
#     print(f"{n3} is greater than all the numbers entered")

"LOOPS"
"For Loop"
x = "HELLO"
# to traverse to a list
# for i in x:
#     print(i)
"Range"
# for i in range(1,10+5,3):
#     print(i)
"While Loop"
# x=4
# while x < 10:
#     print("OK", x)
#     x+=1

"""Convert your calculator program to a menu-driven program 
using the appropriate loop (research)."""
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def calculator():
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print("Result:", result)
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            print("Result:", result)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# calculator()

"example 2"

# print("Welcome to My Calculator")
# print()
# print("Menu:")
# print("Operations: +, -, x, /, exit")
# print()
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# op = input("Enter the operation (+, -, x, /, exit): ")

# while True:
#     if op == "+":
#         sum = num1 + num2
#         print(sum)
#     elif op == "-":
#         sub = num2 - num1
#         print(sub)
#     elif op == "x":
#         product = num1 * num2
#         print(product)
#     elif op == "/":
#         if num2 == 0:
#             print("Division not possible by 0")
#         else:
#             div = num1 / num2
#             print(div)
#     elif op == "exit":
#         print("exiting...")
#         break
#     else:
#         print("Incorrect Input")


"""Write the multiplication table of 5 upto 10 using the (for loop)."""
# number = 5
# for i in range (1,11):
#     result = number * i
#     print(number, "x", i, "=", result)

# for i in range(6+1):
#     print("Voltage Okay.", i)
#     if i == 4:
#         break
# print("fused")

"""Loop Continue Statement"""
# for x in range(0,6+1):
#     if x==3:
#         continue
#     print(x)

"""Nexted Loop"""
# num = int(input("Enter Number Here: "))
# for x in range(1, num + 1):
#     for y in range (1, x + 1):
#         print(y, end=", ")
#     print(x)

# rows = int(input("Enter the number of rows: "))
# increment = int(input("Enter the increment value: "))

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j * increment, end=" ")
#     print(i)
   
"""Pratice Sessions"""
#1.  Write a program to find the sum of individual digits 
# of a number input by the user.
# usin = input("Enter the number: ")
# suma = 0 #since we want to find the sum of the numbers we create a new variable
# for i in usin:
#     suma = suma + int(i)
# print(suma)

# s= input("Enter word here: ")
# for t in s:
#     print(t)

"2.  Write a program to find the grade of a student according to the table given below"
"if > 80% = A, 70-80% = B, 60-70% = C, Below 60% = D"

# student_grade = int(input("Enter your Percentage WITHOUT the '%' here: "))
# if student_grade >= 80:
#     print("Congratulations! you've got A")
# elif student_grade >= 70 and student_grade <80:
#     print("You've got B")
# elif student_grade >= 60 and student_grade <70:
#     print("You've got C")
# elif student_grade <= 59:
#     print("You've got D")
# else:
#     print("Invalid Entry")

"3. Write a program that takes a string as input and prints the number of character in the string"

# string = input("What is your favourite word? ")
# print(len(string))
# count = 0
# for i in string:
#     count += 1
#     print(i, end=" " )
# print(count)

"4. Online Shopping Cart"
"Requirements"
"a) Add item to cart, b) View cart, c)Calculate total cost, D) Apply discount, e) Check out and exit"

# print("Welcome to Azeez Shopping Cart")
# print()
# print("Menu: \n1. Add Item \n2. Remove Item \n3. View Cart \n4. Calculate Cost \n5. Apply Discount \n6. Checkout & Exit")
# items={}
# while True:
#     choice = input("Enter your choice (1-6): ")

#     if choice == "1":
#         item = input("Enter the name of item: ")
#         cost = float(input("Enter Cost of item: "))
#         items[item] = cost
#     elif choice == "2":
#         key = input("Enter Item to REMOVE from cart: ").lower()
#         if key in items:
#             del items[key]
#             print("Item Removed Successfully...")
#         else:
#             print(f"{key} not found in the cart")        
#     elif choice == "3":
#         print("Your Cart is: \n", items)
#     elif choice == "4":
#         value = items.values()
#         totalcost = 0
#         for i in value:
#             totalcost +=i 
#             print(i)
#         print("Total cost is: BHD",totalcost)
#     elif choice == "5":
#         voucher = input("Enter DISCOUNT VOUCHER: ").upper()
#         if voucher == "RENAULT":
#             discount_cost = totalcost - (20/100)*totalcost
#             print(totalcost)
#             print(voucher, "discount voucher added")
#             print("New Price:", discount_cost)
#         else:
#             print("Invalid Code.")
#     elif choice == "6":
#         print("Thank you for shopping with us..")
#         break
#     else:
#         print("Invalid Input!")
#         continue

"FUNCTIONS"
def multipliy():
    n1 = 5
    n2 = int(input("number2: "))
    p = n1*n2
    print(p)
    return p
# multipliy()

# x=math.pow(3,2)
# print(x)
# y = random.random()
# print(y)
# z = random.randint(2,19)
# print(z)

"How can we enhance account security for various types of accounts, such as online accounts, by implementing authentication? Lets use our skill to design a program with a user-defined function called 'AUTH' that takes 'USER' and 'PWD' as parameters. The function should display'Account Blocked' if the attempts exceed 3 times. Upon successful authentication, program should display 'Login Successful!'"

def AUTH(User, Password):
    if User == "renault" and Password == "1234!@#$":
        print("Login Successful!")    
        print("Welcome to Azeez Shopping Cart")
        print()
        print("Menu: \n1. Add Item \n2. Remove Item \n3. View Cart \n4. Calculate Cost \n5. Apply Discount \n6. Checkout & Exit")
        items={}
        totalcost = 0
        while True:
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                item = input("Enter the name of item: ")
                cost = float(input("Enter Cost of item: "))
                items[item] = cost
            elif choice == "2":
                key = input("Enter Item to REMOVE from cart: ").lower()
                if key in items:
                    del items[key]
                    print("Item Removed Successfully...")
                else:
                    print(f"{key} not found in the cart")        
            elif choice == "3":
                print("Your Cart is: \n", items)
            elif choice == "4":
                value = items.values()
                totalcost = 0
                for i in value:
                    totalcost +=i 
                    print(i)
                print("Total cost is: BHD",totalcost)
            elif choice == "5":
                voucher = input("Enter DISCOUNT VOUCHER: ").upper()
                if voucher == "RENAULT":
                    discount_cost = totalcost - (20/100)*totalcost
                    print(totalcost)
                    print(voucher, "discount voucher added")
                    print("New Price:", discount_cost)
                else:
                    print("Invalid Code.")
            elif choice == "6":
                print("Thank you for shopping with us..")
                break
            else:
                print("Invalid Input!")
                continue
    else:
        attempts = 3
        while True:
            if User != "renault":
                print("username not found")
            elif Password != "1234!@#$":
                print("Invalid Password")
            print("You have", attempts, "attempts remaiing.")
            User = input("Enter username again: ").lower()
            Password = input("Enter password again: ")
            if User == "renault" and Password == "1234!@#$":
                print("Login Successful!")
                print("Welcome to Azeez Shopping Cart")
                print()
                print("Menu: \n1. Add Item \n2. Remove Item \n3. View Cart \n4. Calculate Cost \n5. Apply Discount \n6. Checkout & Exit")
                items={}
                totalcost = 0
                while True:
                    choice = input("Enter your choice (1-6): ")

                    if choice == "1":
                        item = input("Enter the name of item: ")
                        cost = float(input("Enter Cost of item: "))
                        items[item] = cost
                    elif choice == "2":
                        key = input("Enter Item to REMOVE from cart: ").lower()
                        if key in items:
                            del items[key]
                            print("Item Removed Successfully...")
                        else:
                            print(f"{key} not found in the cart")        
                    elif choice == "3":
                        print("Your Cart is: \n", items)
                    elif choice == "4":
                        value = items.values()
                        totalcost = 0
                        for i in value:
                            totalcost +=i 
                            print(i)
                        print("Total cost is: BHD",totalcost)
                    elif choice == "5":
                        voucher = input("Enter DISCOUNT VOUCHER: ").upper()
                        if voucher == "RENAULT":
                            discount_cost = totalcost - (20/100)*totalcost
                            print(totalcost)
                            print(voucher, "discount voucher added")
                            print("New Price:", discount_cost)
                        else:
                            print("Invalid Code.")
                    elif choice == "6":
                        print("Thank you for shopping with us..")
                        break
                    else:
                        print("Invalid Input!")
                        continue 
            else:
                attempts -=1
            if attempts == 0:
                print("ACCOUNT BLOCKED!!!")
                break
user = input("Enter your username: ").lower()
pwd = input("Enter your password: ")
AUTH(user,pwd)