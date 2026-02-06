# 10. Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

def calculate_profit_loss(cp,sp):

    if cp < sp :
        print("It is Profit")

    else:
        print("It is Loss")


cp = float(input("Enter your Cost Price:"))
sp = float(input("Enter your Selling Price:"))


calculate_profit_loss(cp,sp)

