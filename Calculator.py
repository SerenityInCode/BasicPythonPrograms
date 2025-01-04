print("########################")
print("CALCULATOR")
print("########################")

# 1. add
# 2. sub
# 3. div
# 4. mul
# 5. modulus
# 6. percentage
# 7. exit
choice=0
while choice<7:
   print("########################")
   print("Choice 1: Add the numbers")
   print("Choice 2: Subtract the numbers")
   print("Choice 3: Multiply the numbers")
   print("Choice 4: Divide the numbers")
   print("Choice 5: Return remainder of division ")
   print("Choice 6: Calculate percentage")
   print("Choice 7: exit")
   print("########################")
   choice=int(input("Enter choice: "))
   if choice==1:
     def add(num1,num2):
        addition=num1+num2
        return addition
     #Input
     num1=int(input("Enter number 1: "))
     num2=int(input("Enter number 2: "))
     #Process
     catch=add(num1,num2)
     #Output
     print("Addition of two numbers is: ",catch)
   elif choice==2:
    def sub(num1,num2):
       subtract=num1-num2
       return subtract
    #Input
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    #Process
    catch=sub(num1,num2)
    #Output
    print("Subtraction of two numbers is: ",catch)
   elif choice==3:
     def mul(num1,num2):
       multiply=num1*num2
       return multiply
     #Input
     num1=int(input("Enter number 1: "))
     num2=int(input("Enter number 2: "))
     #Process
     catch=mul(num1,num2)
     #Output
     print("Product of two numbers is: ",catch)
   elif choice==4:
     def div(num1,num2):
      division=num1/num2
      return division
     #Input
     num1=int(input("Enter number 1: "))
     num2=int(input("Enter number 2: "))
     #Process
     catch=div(num1,num2)
     #Output
     print("Quotient of division of numbers is: ",catch)
   elif choice==5:
     def modulus(num1,num2):
      remainder=num1%num2
      return remainder
     num1=int(input("Enter number 1: "))
     num2=int(input("Enter number 2: "))
     #Process
     catch=modulus(num1,num2)
     #Output
     print("Remainder of division of numbers is:",catch)
   elif choice==6:
     def percentage(num1,num2,num3):
      value=num1
      totalvalue=num1+num2+num3
      percentage=(value/totalvalue)*100
      return percentage
     num1=int(input("Enter number 1: "))
     num2=int(input("Enter number 2: "))
     num3=int(input("Enter number 3: "))
     #Process
     catch=percentage(num1,num2,num3)
     #Output
     print("Perecentage of numbers is: ",catch)
   else:
    print("Exit") 

