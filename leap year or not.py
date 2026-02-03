# 7) Write a program that will tell whether the given year is a leap year or not.

while True:
    year = int(input("Enter your year:"))

    def leap_year_or_not(year):
        if (year %4 == 0) and ((year %400 == 0) or (year %100 != 0)):
            print("It is Leap Year")
        
        else:
            print("It is not an Leap Year")

    leap_year_or_not(year)