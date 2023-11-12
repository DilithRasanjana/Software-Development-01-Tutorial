#Create Variables
num_1 = 0
num_2 = 0
operator = 0

#Get user Inputs
num_1 = int(input("Enter the first integer number:"))
operator = input("Enter the operator:")
num_2 = int(input("Enter the second integer number:"))

#Process
if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    if num_2==0:
        print("Division by zero is not allowed")
    else:
        print(num_1 / num_2)
else:
    print("Invalid Operator")
