#Program6
#Check whether a number is divisible by 5 and 11 or not
#Input
number=int(input("Enter number: "))
#Process
if number%5==0 and number%11==0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")