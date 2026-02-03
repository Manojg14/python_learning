# 2. Write a program that will convert celsius value to fahrenheit


def celsius_to_fahrenheit():
    celsius = float(input("Enter your Celsius Value:"))
    fahrenheit = celsius * 1.8 + 32
    print(f"{fahrenheit} °F" )

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter your Fahrenheit Value:"))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{celsius} °C")

while True:

    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Break Code")

    choose_option = int(input("Enter any one option(1 or 2 or 3):"))

    if choose_option == 1:
        celsius_to_fahrenheit()

    elif choose_option == 2:
        fahrenheit_to_celsius()

    elif choose_option == 3:
        break

    else:
        print("Choose Correct Option")