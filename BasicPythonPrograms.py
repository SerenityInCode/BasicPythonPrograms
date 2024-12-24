# Program1
# Input
age=int(input("Enter age: "))
#Process
if age>18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")    

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

# Program3
# Find max between 2 numbers
# Input
a=int(input("Enter a: "))
b=int(input("Enter b: " ))
#Process
if a>b:
    print("The max number is: ",a)
else:
    print("The max number is: ",b)

# Program4
# Find max between 3 no.s
# Input
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

# Program 5
# Check whether the number is even or odd
# Input
number=int(input("Enter number: "))
#Process
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")

# Program6
# Check whether a number is divisible by 5 and 11 or not
# Input
number=int(input("Enter number: "))
#Process
if number%5==0 and number%11==0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")
   
#Program7
#Whether the year is leap year or not
year=int(input("Enter a year: "))
#Process
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year is a leap year")
        else:
            print("The year is a common year") 
    else:
        print("The year is a leap year")     
else:
    print("The year is a common year")    

#Program8
#Select shape and print the perimeter and area
shape=(int(input("Choose the option for selecting shape: ")))
if shape==1:
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    perimeter1=2*(l+b)
    area1=l*b
    print("Perimeter of rectangle is: ",perimeter1)
    print("Area of rectangle is: ",area1)
if shape==2:
    side1=(int(input("Enter side: "))) 
    perimeter2=4*side1
    area2=side1*side1
    print("Perimeter of square is: ",perimeter2)
    print("Area of rectangle is: ",area2)
if shape==3:
    radius=(int(input("Enter radius:")))    
    perimeter3=2*3.14*radius
    area3=3.14*radius*radius
    print("Perimeter of circle is: ",perimeter3)
    print("Area of circle is: ",area3)
if shape==4:
    side2=(int(input("Enter side of a rhombus: ")))
    d1=(int(input("Enter diagonal1: ")))
    d2=(int(input("Enter diagonal2: ")))
    perimeter4=4*side2
    area4=(d1*d2)/2
    print("Perimeter of rhombus is: ",perimeter4)
    print("Area of rhombus is: ",area4)
if shape==5:
    b=(int(input("Enter base: ")))
    h=(int(input("Enter height: ")))
    thirdside=(int(input("Enter third side: ")))
    perimeter5=b+h+thirdside
    area5=1/2*b*h
    print("Perimeter of triangle is: ",perimeter5)
    print("Area of triangle is: ",area5)


