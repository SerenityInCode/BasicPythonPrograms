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
