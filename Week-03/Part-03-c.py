#Create Variables
cost=0
tip=0
s_level=0

#Statements
print("diners’ satisfaction level ratings:\n\n 1 = Totally satisfied\n\n 2 = Satisfied\n\n 3 = Dissatisfied\n\n")

#Get user Inputs
cost=int(input("Enter the cost of meal:"))
s_level=int(input("Enter satisfaction level using ratings:"))

#Process

if s_level==1:
    tip=cost*20/100
elif s_level==2:
    tip=cost*15/100
elif s_level==3:
    tip=cost*10/100
else:
    print("Invalid satisfaction level")

#Output

print("Tip is",tip)
