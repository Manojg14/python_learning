# 3. User will input (2numbers).Write a program to swap the numbers

a = int(input("Enter a value:"))
b = int(input("Enter b value:"))

def swap_numbers(a,b):
    temp = a
    a = b
    b = temp

    print (f"A values {a}")
    print(f"B values {b}")

swap_numbers(a,b)