#Program2
#Input
engmarks=int(input("Enter English Marks:"))
hindimarks=int(input("Enter Hindi Marks: "))
scimarks=int(input("Enter Science Marks: "))
mathsmarks=int(input("Enter Maths Marks: "))
ssmarks=int(input("Enter Social Science Marks: "))
#Process
marks=engmarks+hindimarks+scimarks+mathsmarks+ssmarks
totalmarks=250
print("The total marks is: ",marks)
percentage=(marks/250)*100
print("The percentage is: ",percentage)
if percentage>90:
    print("Your grade is A")
elif percentage>80:
    print("Your grade is B")
elif percentage>70:
    print("Your grade is C")
elif percentage>50:
    print("Your grade is D")
else:
    print("Your grade is E")