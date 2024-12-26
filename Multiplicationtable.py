#Program10
#Print multiplication table of a given number
n=int(input("Enter table number: "))
for i in range(1,11):
    table=n*i
    print(f"{n}X{i}=",table)
    