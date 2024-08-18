"""             Write code for the following (for loop) questions.      """



'''     1) Print Numbers from 1 to 10:
Ask the students to write a Python program using a for loop to print numbers from 1 to 10.'''

# for i in range(1, 11):
#     print(i)



'''     2) Calculate the Sum of First 10 Natural Numbers:
Write a program to sum up the first 10 natural numbers using a for loop'''

# sum = 0
# for i in range(1, 11):
#     sum += i
# print(f"The sum of the first 10 natural numbers is: {sum}")




'''     3) Print the Multiplication Table for a Given Number:
Write a program that asks the user for a number and prints the multiplication table for that number up to 10 using a for loop.'''

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")




'''     4) Print All Even Numbers Between 1 and 20:
Use a for loop to print all even numbers between 1 and 20.'''

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)





'''5) Count the Number of Digits in an Integer:
Write a Python program to count the number of digits in a given integer. Use a for loop with str() conversion.'''

# number = input("Enter an integer: ")
# count = 0
# for char in number:
#     if char.isdigit():
#         count += 1
# print(f"The number of digits is: {count}")




'''6) Reverse a String:
Write a program to reverse a given string using a for loop.'''

# string = input("Enter a string: ")
# rev_string = ""

# for char in string:
#     rev_string = char + rev_string
# print(f"The reversed string is: {rev_string}")



'''7) Calculate Factorial of a Number:
Ask the user for a non-negative integer and calculate the factorial of that number using a for loop.'''

# num = int(input("Enter a non-negative number: "))
# if num < 0:
#     print("Factorial is not for negative numbers.")
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is: {factorial}")





'''8) Find the Sum of All Numbers in a List:
Write a program that sums all the numbers in a given list using a for loop.'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# for x in numbers:
#     sum += x
# print(f"The sum of all numbers in the list is: {sum}")



'''9) Check if a Number is Prime:
Write a program that asks the user to enter a number and then uses a for loop to check if it is a prime number.'''

# num = int(input("Enter a number to check it is prime or not: "))
# if num <= 1:
#     print("The number is not prime")
# else:
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#         if is_prime:
#             print("Te number", num, "is prime")
#         else:
#             print("Te number", num, "is not a prime")





'''10) Print Each Character of a String on a New Line:
Write a program that prints each character of a given string on a new line using a for loop.'''


# string = "This is a String"
# for i in string:
#     print(i)


