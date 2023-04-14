# name = input("Enter your name:")
# print('Hello',  name)

# Write a program to prompt the user for hours and rate per hour using input to
#compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program
#(the pay should be 96.25). You should use input to read a string and float() to
#convert the string to a number. Do not worry about error checking or bad user data.

# hrs = int(input("Enter Hours:"))
# rph = float(input("Enter rate per hour:"))
# gross_pay = hrs * rph
# print('Pay:', gross_pay)


""""
 Write a program to prompt the user for hours and rate per hour using input to
 compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the
 hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50
 per hour to test the program (the pay should be 498.75). You should use input to
 read a string and float() to convert the string to a number. Do not worry about error
 checking the user input - assume the user types numbers properly.
"""
# hrs = input("Enter Hours:")
# rph= input('Enter rate per hour:')
# try:
#     H = float(hrs)
#     R = float(rph)
# except:
#     print('Error, enter actual number:') 
#     quit()  
    
# if H > 40:
#     HR = H*R
#     print(HR)
""""
Write a program to prompt for a score between 0.0 and 1.0. If the score is out
of range, print an error. If the score is between 0.0 and 1.0, print a grade using the
following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For
the test, enter a score of 0.85.
"""

# score = float(input("Enter Score: "))
# if score >= 0.9:
#     print('A')
# elif score >= 0.8:
#     print('B')
# elif score >=0.7:
#     print('C')
# elif score >=0.6:
#     print('D')
# elif score<0.6:
#     print('f')
# else:
#     print('None')

""" 
Write a program to prompt the user for hours and rate per hour using input to
compute gross pay. Pay should be the normal rate for hours up to 40 and time-
and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to
do the computation of pay in a function called computepay() and use the function
to do the computation. The function should return a value. Use 45 hours and a rate
of 10.50 per hour to test the program (the pay should be 498.75). You should use
input to read a string and float() to convert the string to a number. Do not worry
# about error checking the user input unless you want to - you can assume the user
# types numbers properly. Do not name your variable sum or use the sum() function.
# """
# def computepay(H, R):
#     H = float(input("Enter Hours:"))
#     R = float(input('Enter rate per hour:'))
#     if H>40:
#         HR = H*R
#         print('pay', HR)
#         return  HR
        
    
# computepay('H','R',)


# mylist = [1,100,15,17, 105, 9.10]
# #newlist=[i for i in mylist if (i//10)>=1(i//10)<10]
# #print(newlist)
# newlist=[i for i in mylist if i in range(10,100)]
# print(newlist)

# def solve(s):
#         firstname_secondname=input('Enter name:')
#         print(firstname_secondname.title())
# solve('s')
"""
 Write a program that repeatedly prompts a user for integer numbers until the
 user enters 'done'. Once 'done' is entered, print out the largest and smallest of the
 numbers. If the user enters anything other than a valid number catch it with a
 try/except and put out an appropriate message and ignore the number. Enter 7, 2,
 bob, 10, and 4 and match the output below."""
 

# while True:
#     try:
#         num = int(input("Enter a number: "))
#     except: 
#         print('invalid input')
#         print('Maximum is',10 )
#         print('minimum is',2 )
#         quit()
#     if 2<=num<=10:
#         print(num)
#         continue
#     if num =='done':
#         break


# out

# Invalid input
# Maximum is 10
# Minimum is 2


# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     n = int(input())
#     if n % 2 != 0:
#         print ('Weird')
#     elif n > 20:
#         print('Not Weird')
#     elif 6 <= n <= 20:
#         print('Weird')
#     elif 2 <= n <= 5:
#         print('Not Weird')
    
    
    
# list=[]

# while True:

#     try:
#         number = input("Enter a number: ")
#         if number == 'done': 
#             break
#         n = int(number)
#         list.append(n)
#         largest = max(list)
#         smallest = min(list)
        
#     except:
#         print ("Invalid input")
        
# print("Maximum is",largest)
# print("Minimu  is",smallest)

total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

