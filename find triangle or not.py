# 9. Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

def equilateral_triangle(AB,BC,CA):

    if AB == BC == CA:
        print("It is Equilateral Triangle")

    elif AB == BC != CA:
        print("It is Isosceles Triangle")
    
    elif AB != BC != CA:
        print("It is Scalene Triangle")

    else:
        print("It isn't a Triangle")


AB = int(input("Enter AB Units Values:"))
BC = int(input("Enter BC Units Values:"))
CA = int(input("Enter CA Units Values:"))

equilateral_triangle(AB,BC,CA)
