import getpass # To hide password from showing in trminal
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
        while attempts > 0:
            if User != "renault":
                print("username not found")
            elif Password != "1234!@#$":
                print("Invalid Password")
            attempts -= 1
            print("You have", attempts, "attempts remaiing.")
            if attempts > 0:
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
                    print("Login Failed. Please try again")
            else:
                print("ACCOUNT BLOCKED!!!")
                break
user = input("Enter your username: ").lower()
pwd = getpass.getpass("Enter your password: ")
AUTH(user,pwd)

# Dictionary to store usernames and passwords
register = {}

def register_user():
    username = input("Enter your username: ").lower()
    password = getpass.getpass("Enter your password: ")
    register[username] = password
    print("Registration Successful")

def login():
    username = input("Enter your username: ").lower()
    password = getpass.getpass("Enter your password: ") # we use the getpass inbuilt function to hide the password from displaying
    if username in register and register[username]==password:
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
            print("Invalid Username or Password")
            print("You have", attempts, "attempts remaiing.")
            User = getpass.getpass("Enter username again: ").lower()
            Password = getpass.getpass("Enter password again: ")
            if username in register and register[username]==password:
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

# Main program loop
while True:
    print("--- Shopping Cart ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        register_user()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")