#Program4
#Find max between 3 no.s
#Input
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
#Process
if a>b and a>c:
    print("The max number is: ",a)
elif b>a and b>c:
    print("The max number is: ",b)       
else:
    print("The max number is: ",c)       