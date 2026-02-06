# Write a program to find the euclidean distance between two and Three coordinates.

import math


def dimension_2d(x1,x2,y1,y2):

    formula = (x2 - x1) ** 2+ (y2 - y1) ** 2
    dimension2d= math.sqrt(formula)

    print(f"2 Dimension {dimension2d}")

def dimension_3d(x1,x2,y1,y2,z1,z2):

    formula = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    dimension3d = math.sqrt(formula)

    print(f"3 Dimension {dimension3d}")


dimension = input("Enter Dimension Measured 2D or 3D:").strip().lower()

if dimension == '2d':

    x1 = int(input("Enter X1 Value:"))
    y1 = int(input("Enter Y1 Value:"))
    x2 = int(input("Enter X2 Value:"))
    y2 = int(input("Enter Y2 Value:"))

    dimension_2d(x1,x2,y1,y2)

elif dimension == '3d':
    
    x1 = int(input("Enter X1 Value:"))
    y1 = int(input("Enter Y1 Value:"))
    z1 = int(input("Enter Z1 Value:"))
    x2 = int(input("Enter X2 Value:"))
    y2 = int(input("Enter Y2 Value:"))
    z2 = int(input("Enter Z2 Value:"))

    dimension_3d(x1,x2,y1,y2,z1,z2)

else:
    print("You Enter Invalid Number")



