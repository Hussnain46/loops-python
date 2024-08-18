"""             Write code for the following advance questions using loops. """


'''         1) Print a Pyramid Pattern:
Write a program to print a pyramid pattern with stars (*). The user specifies the number of rows.
    *
   ***
  *****
 *******
*********
'''

# rows = int(input("Enter the number of rows for the pyramid: "))

# for i in range(1, rows + 1):
#     space = rows - i
#     stars = 2 * i - 1
#     print(' ' * space + '*' * stars)




'''     2) Find All Prime Numbers Up to N:
Implement a program that finds all prime numbers up to N.'''

# Num = int(input("Enter a num: "))

# for i in range(2, Num + 1):
#     prime = True
#     for x in range(2, i):
#         if i % x == 0:
#             prime = False
#             break
#     if prime:
#         print(i) 



'''3) Create a Zigzag Sequence:
Write a program to create a zigzag sequence with numbers. 
The sequence should alternate between increasing and decreasing numbers sequentially and use nested loops as shown below:
1
2 1
1 2 3
4 3 2 1
1 2 3 4 5
'''

# rows = int(input("Enter the number of rows for the zigzag sequence: "))

# for i in range(1, rows + 1):
#     if i % 2 == 1:
#         for j in range(1, i + 1):
#             print(j, end=' ')
#     else:
#         for j in range(i, 0, -1):
#             print(j, end=' ')
#     print()




'''4) Fibonacci Sequence with a Twist:
Write a program to generate a Fibonacci sequence up to n elements where every number divisible by 3 is replaced with "Fizz", 
every number divisible by 5 is replaced with "Buzz", and numbers divisible by both are replaced with "FizzBuzz".'''

# n = int(input("Enter the number of Fibonacci elements: "))
# a, b = 0, 1

# for i in range(n):
#     if a % 3 == 0 and a % 5 == 0:
#         print("FizzBuzz", end=' ')
#     elif a % 3 == 0:
#         print("Fizz", end=' ')
#     elif a % 5 == 0:
#         print("Buzz", end=' ')
#     else:
#         print(a, end=' ')
    
#     a, b = b, a + b
# print()


