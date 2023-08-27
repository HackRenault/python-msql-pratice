import random
import datetime

"""Create a number guessing ga,e where the computer generates a random number between 1 and 10. The user should be primpted to guess the number. Provide feedback on each guess(HIGHER OR LOWER) and keep track of the nmber of attempts until the user guess the correct number."""
print("Welcome to Renault Guessing Game")
attempts = 0
number = random.randint(1,100)
while True:
    guess = int(input("Enter your number: "))
    if guess < number:
        print("Guess Higher")
        attempts += 1
    elif guess > number:
        print("Guess Lower")
        attempts += 1
    elif guess == number:
        print("~~~You guessed correct~~~")
        attempts += 1
        break
    
print("you guessed", attempts, "times")
print()
"""- Write a program that prints all the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz"."""
print("This program prints all the numbers from 1 to 100. For multiples of 3, it displays 'Fizz' instead of the number, and for multiples of 5, it displays 'Buzz'. For numbers that are multiples of both 3 and 5, it displays 'FizzBuzz'")
# Using the for loop
for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
print()
"""- Write a program that calculates the factorial of a given number using a loop."""
print("THIS SCRIPT CALCULATES THE FACTORIAL FOR ANY NUMBER")
digit = int(input("Enter a number: "))
factorial = 1
# Using the if/else:
if digit < 0:
    print("Factorial is not defined for negative numbers.")
elif digit == 0:
    print("Factorial of 0 is 1")
else:
    # Use a for loop to multiply the numbers from 1 to the given number and calculate the factorial
    for i in range(1, digit + 1):
        factorial *= i
    print(f"The factorial for {digit} is {factorial}")
print()    

"""Write a program that checks whether a given number is even or odd and prints the result"""
print("This Program checks whether a given number is even or odd")
while True:
    user_number = int(input("Enter your number: "))
    # use the if/else loop
    if user_number % 2 == 0:
        print(f"{user_number} is an EVEN Number")
    else:
        print(f"{user_number} is an ODD Number")
    break
print()

"""Write a program that determines if a given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400"""
print("This program prints the Leap Years from 1990 till date")
current_year = datetime.datetime.now().year

leap_years = []
for year in range(1990, current_year + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_years.append(year)

print("Leap years from 1990 to", current_year, ":")
print(leap_years)
print()

print("This program determines if a given year is a leap year.")
year = int(input("Enter the year to determine: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"Year {year} is a Leap Year")
else:
    print(f"Year {year} is NOT a Leap Year")
print()

"DATA-TYPES"
"""Write a program that takes a list of numbers as input and finds the maximum and minimum values in the list"""
print("This program TAKES A LIST OF NUMBERS AS INPUT AND FINDS THE MAXIMUM AND MINIMUM VALUES IN THE LIST")

def find_min_max(numbers):
    #check if the input list is empty, or has at least two numbers if empty return None for both the minimum and maximum number indicating no values to evaluate
    if len(numbers) == 0 or len(numbers) < 2:
        return None, None
    #Initialize the min_value and max_value using the first number in the list
    min_value = numbers[0]
    max_value = numbers[0]
    # Use the for loop to iterate over the list and compare it to the initial list
    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
    return min_value, max_value

# Example usage
number_lit = [5, 2, 9, 1, 7, 3, 6]
minimum, maximum = find_min_max(number_lit)

print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
print()

# User Input Loop
number_list = []
while True:
    # Prompt the user to enter a number.
    numbers = input("Enter your number (enter 'done' to finish): ")
    # If the user enters "done" (case-insensitive) the loop terminates
    if numbers.lower()=="done":
        break
    # the enterd number is converted to an interger and appended to the number_list using the append() method
    number_list.append(int(numbers))

minimum, maximum = find_min_max(number_list)
print(number_list)
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")

# User Input Without Loop
# Assuming we want the user to enter bunch of numbers into the list at once without looping, we can simply do it by first creating a list
numeral = []
# Then create an input statement that takes the numbers and sepreate it by a space
input_numerals = input("Enter your numbers ('Seperate Each Number by a SPACE): ")
# Because the numbers are seperated by a space or any delimeter, we use the split() method to remove the delimeter and convert it into integer using the list comprehension
numeral = [int(num) for num in input_numerals.split()]
# We can also us the append() and extend() method just in case
'Using append()'
# for num in input_numerals.split():
#   numeral.append(int(num))
'Using extend()'
# numeral.extend(int(num) for num in input_numerals.split())
# Because our function takes two parameter we now write
minimum, maximum = find_min_max(numeral)

print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
print()

"Create a program that asks the user for a sentence and counts the number of vowels(a,e,i,o,u)"
print("This SCRIPT counts the number of VOWELS in a Sentence")
# Ask the user to input a sentence
sentence = input("Enter a sentence: ")
# Intialiaze a variable to keep count
vowel_count = 0
# Convert the sentence to lower case
sentence = sentence.lower()
# Iterate over each char in sentence
for char in sentence:
    # Check if the character is vowel (a,e,i,o,u)
    if char in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)
print()

"Note to Count each vowel (a,e,i,o,u) indepedently, modify the program to use individual variables"
print("This SCRIPT counts the number of each VOWELS in a Sentence")
sentence1 = input("Enter a sentence: ").lower()
# remove spaces from the sentence (OPTIONAL)
# sentence1 = sentence1.replace(" ", "")
# Intialize variable to keep count of vowels
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
# iterate over each character in Sentence1
for char in sentence1:
    if char == "a":
        count_a += 1
    elif char == "e":
        count_e += 1
    elif char == "i":
        count_i += 1
    elif char == "o":
        count_o += 1
    elif char == "u":
        count_u += 1
print(f"Number of times 'a' appeared in {sentence1} is {count_a}")
print(f"Number of times 'e' appeared in {sentence1} is {count_e}")
print(f"Number of times 'i' appeared in {sentence1} is {count_i}")
print(f"Number of times 'o' appeared in {sentence1} is {count_o}")
print(f"Number of times 'u' appeared in {sentence1} is {count_u}")
print()

"Creating it as a function"
def count_vowels(sentence):
    # Initialize variables for vowel counts
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Iterate over each character in the sentence
    for char in sentence:
        if char == "a":
            count_a += 1
        elif char == "e":
            count_e += 1
        elif char == "i":
            count_i += 1
        elif char == "o":
            count_o += 1
        elif char == "u":
            count_u += 1

    # Return the count of each vowel as a dictionary
    vowel_counts = {
        'a': count_a,
        'e': count_e,
        'i': count_i,
        'o': count_o,
        'u': count_u
    }
    return vowel_counts

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Call the function and get the vowel counts
counts = count_vowels(sentence)

# Display the count of each vowel
print("Count of 'a':", counts['a'])
print("Count of 'e':", counts['e'])
print("Count of 'i':", counts['i'])
print("Count of 'o':", counts['o'])
print("Count of 'u':", counts['u'])
print()

"String Manipulation"
"Write a program that takes a stirng as input and prints it in reverse order"
print("This script prints out the reverse orde of an input string")
# Prompt the user for a sentence
string = input("Enter a word or a sentence: ")
# To do this we utilize the slicing operation [start:end:step] to traverse the list or string sequence in reversal
revised_string = string[::-1]
print(revised_string)

"Create a program that asks the user for a sentence and count the number of words in a sentence"
print("This script counts the number of words in a sentence")
#prompt the user for the sentence
sentences = input("Enter a word or sentence: ")
# Splint the sentence into words
words = sentences.split()
# initiaze a variable and use the len function to count the words and save in the variable
words_count = len(words)
# Print the result
print("Number of words:", words_count)
print()

"Create a program that asks the user for a list of numbes and calculate the sum of all the numbers in the list."
print("This script promptd a user for a list of numbers and calculates the sum of all the numbers in the lits")
# Initialize the variable
list_of_numbers = []
# Prompt the user for the list
no_list = input("Enter your numbers ('Seperate Each Number by a SPACE): ")

