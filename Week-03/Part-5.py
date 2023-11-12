#Create Variables
response = 0

#Get User Inputs
response =input("Do you like python(Yes/No) : ").lower()

#Process
if response == 'yes' or response == 'y':
    print("you are on the right course")
elif response == 'no' or response == 'n':
    print("you might change your mind") 
else:
    print("I did not understand")
