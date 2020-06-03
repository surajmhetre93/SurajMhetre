"""
1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “c” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
"""
user_input = eval(input("Enter  any value:"))
if user_input % 3 == 0 and user_input % 5 == 0:
    print("Consultadd Python Training")
elif user_input % 3 == 0:
    print("Consultadd")
elif user_input % 5 == 0:
    print("c")

"""
2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
At the end if the answer of any operation is Negative print a statement saying “zsa”
NOTE: At a time user can perform one action at a time.
"""

user_input1 = eval(input("""Enter your choice(Option #):
1. Addition
2. Subtraction
3. Division
4. Multiplication
5. Average
"""))
if user_input1 in [1, 2, 3, 4, 5]:
    first = eval(input("Enter first number:"))
    second = eval(input("Enter second number:"))
    if user_input1 == 1:
        print("Addition:", first + second)
    elif user_input1 == 2:
        print("Subtraction:", first - second)
    elif user_input1 == 3:
        print("Division:", first / second)
    elif user_input1 == 2:
        print("Multiplication:", first * second)
    else:
        first1 = eval(input("Enter the third number:"))
        second1 = eval(input("Enter fourth number:"))
        print("Average:", sum([first, second, first1, second1]) / 4)
else:
    print("ZSA")

"""
Program for the given flowchart
"""
a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("avg = ", avg)
if avg > a and avg > b and avg > c:
    print("Average is higher than a, b, c")
else:
    if avg > a and avg > b:
        print("Average is higher than a, b, c")
    elif avg > a and avg > c:
        print("Average is higher than a, c")
    elif avg > b and avg > c:
        print("Average is higher than b, c")
    elif avg > a:
        print("Average is higher than a only.")
    elif avg > b:
        print("Average is higher than b only.")
    elif avg > c:
        print("Average is higher than c only.")

"""
4. 	Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”
"""
while True:
    try:
        user_input = int(input("Enter an integer number:"))
        if user_input < 0:
            print("It's over")
            break
        else:
            print("Good Going! Enter negative number to exit else continue.")
    except ValueError:
        pass

"""
5.   Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
"""
lst = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)
print("numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200")
print(lst)

"""
6. What is the output of the following code examples?
x=123 
for i in x:
   	print(i)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print(“error”)
    
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
"""

x = 123
for i in x:
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

"""
7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
       Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement
"""
for i in range(0, 7):
    if i != 3 or i != 6:
        print(i)

"""
8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
"""
user_input = input("Enter a string: ")
digit_count = 0
letter_count = 0
for ch in user_input:
    if ch.isnumeric():
        digit_count += 1
    elif ch.isaplha():
        letter_count += 1
print("""
Letters: %d
Digits: %d
""" % (digit_count, letter_count))

"""
9. Read the two parts of the question below: 
    Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
    Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. 
    The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
"""
guess = 57
while True:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        user_input, answer = input("Do you want to guess again? (Enter number & Yes to continue. Enter No to stop")
        if user_input != guess and answer.lower() == 'yes':
            continue
        elif user_input == guess:
            break
        elif answer.lower == 'no':
            break

"""
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		counter=1
		While counter <= 5:
			print(“Type in the”, counter, “number”
			counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). 
If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
"""
import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        guess = random.randint(1, 100)
    else:
        print("Try again!")
    counter += 1
print("Game over!")

"""
11. In the previous question, insert “break” after the “Good guess!” print statement. 
“break” will terminate the while loop so that users do not have to continue guessing after they found the number. 
If the user does not guess the number at all, print “Sorry but that was not very successful”.
"""
import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        break
    else:
        print("Try again!")
    counter += 1
print("Sorry but that was not very successful!")
