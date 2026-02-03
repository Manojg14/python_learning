# 1 ) User will input (3ages).Find the oldest one 

n = int(input("enter the count:"))

values = []
for i in range (0,n):
    age = int(input(f"Enter your age {i+1}:"))
    values.append(age)

oldest_age = max(values)
print(oldest_age)
