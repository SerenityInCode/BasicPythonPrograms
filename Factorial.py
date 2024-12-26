#Program14
#Print the factorial of a number
#Input
n=int(input("Enter n: "))
factorial=1
#Process
for i in range(1,n+1):
    factorial=factorial*i
    print(factorial)
#Output
print(f"The factorial of number is: {factorial}")