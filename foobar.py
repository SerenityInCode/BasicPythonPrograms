#Program18
#Input
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("foo"+"bar")  
    if i%3==0:
        print("foo")
    elif i%5==0:
        print("bar")    
    else:
        print(i)         

  