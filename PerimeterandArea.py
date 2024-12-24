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

    


