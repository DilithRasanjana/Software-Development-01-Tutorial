#Create Variable
mark=0

#Get User Inputs
mark=int(input("Enter the marks:"))

#Process
if mark<0 or mark>100:
    print("Invalid Mark")
if mark>=70:
    print('Exceptional result!')
elif mark >= 40:
    print('Satisfactory result!')
else:
    print('You have failed')
