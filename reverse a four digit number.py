# 5) Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

digit = input("enter four digit number:")

print(f"The Reversed Number is {digit[::-1]}")

if digit == digit[::-1]:
    print("It is Reversed but it has same values")
else: 
    print("It is Reversed Correctly")

