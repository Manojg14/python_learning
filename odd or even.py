# 6) Write a program that will tell whether the number entered by the user is odd or even.

number = int(input("Enter the Number:"))

def odd_or_even(number):

    if (number %2 == 0):
        print("It is Even Number")

    else: 
        print("It is Odd Number")
    
odd_or_even(number)


