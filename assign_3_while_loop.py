"""          Write code for the following (while loop) questions.    """


'''     1) Print Numbers from 1 to 10:      '''
# n = 1
# while (n<=10):
#     print(n)
#     n = n + 1



'''     2) Sum of First N Natural Numbers:
Ask the user for a number 'N', and then sum up all 
natural numbers up to N using a while loop.'''


# N = int(input("Enter a Natural Number: "))
# sum = 0
# counter = 1
# while counter <= N:
#     sum += counter
#     counter += 1
# print("Te sum of first ", N, "natural numbers is: ", sum)




'''     3) Countdown Timer:
Write a program that counts down from 10 to 1 and then prints "Liftoff!".   '''

# n = 10
# while n >= 1:
#     print(n)
#     n -= 1
# print("Liftoff!")



'''     4) Guess the Number:
Implement a number guessing game. The program should pick a fixed number, 
and the user has to guess it. The loop should continue until the user guesses the correct number.'''

# fix_num = 50
# while True:
#     guess = int(input("Guess the number: "))

#     if guess > fix_num:
#         print("Guess is high. Try Again")
#     elif guess < fix_num:
#         print("Guess is low.Try Again")
#     else:
#         print()
#         print("You guess the Right Number")
#         break



'''     5) Calculate the Average:
Write a program that continuously asks users to enter a number until they enter "0". 
At the end, print the average of all entered numbers.'''

# sum = 0
# count = 0
# while True: 
#     num = int(input("Enter a number (or 0 to finish): "))

#     if num == 0:
#         break

#     sum += num
#     count += 1

# if count == 0:
#     print("no number entered")
# else:
#     avg = sum / count
#     print("The average of enter numbers is:", avg)





'''     6) Password Retry System:
Create a program that asks for a password with a maximum of three attempts. 
If the correct password, "Python123", is entered, print "Access granted", 
otherwise print "Access denied" after three incorrect attempts.'''

# correct_passwrd = "python123"
# attempts = 3

# while attempts > 0:
#     password = input("Enter the password: ")

#     if password == correct_passwrd:
#         print("Access granted")
#         break
#     else:
#         attempts -= 1
#         print("Incorrect password. You have", attempts,"attempts left")

# if attempts == 0:
#     print("Access Denied")




'''     7) Print All Even Numbers up to N:
Ask the user to input a number 'N', then use a while loop to print all even numbers from 1 to N.'''

# N = int(input("Enter a number: "))
# counter = 2

# while counter <= N:
#     print(counter)
#     counter += 2




'''     8) Multiplication Table:
Ask for a number from the user and print its multiplication table up to 10 using a while loop.'''

# num = int(input("Enter a number: "))
# mul = 1

# while mul <= 10:
#     result = mul * num
#     print(f"{num} x {mul} = {result}")
#     mul += 1




'''     9) Find the Largest Number:
Prompt the user to enter numbers one by one, 
and continue accepting numbers until the user enters "0". Print the largest number entered.'''

# largest_number = None
# while True:
#     number = int(input("Enter a number (or 0 to finish): "))
    
#     if number == 0:
#         break

#     if largest_number is None or number > largest_number:
#         largest_number = number

# if largest_number is None:
#     print("No numbers were entered.")
# else:
#     print(f"The largest number entered is: {largest_number}")



'''     10) Factorial of a Number:
Ask the user for a non-negative integer and 
calculate the factorial of that number using a while loop.'''

# number = int(input("Enter a non-negative integer: "))
# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial = 1
#     original_number = number

#     while number > 1:
#         factorial *= number
#         number -= 1

#     print(f"The factorial of {original_number} is: {factorial}")



