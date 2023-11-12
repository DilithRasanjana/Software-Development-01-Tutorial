number_1=int(input("Enter the number:"))
number_2=int(input("Enter the number you want to divide by number1:"))
try: 
   value= number_1/number_2
   print(value)
except ZeroDivisionError:
   print("Cannot divide by zero")
