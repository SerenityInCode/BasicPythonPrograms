from DR_FanQuiz import dr_fanquiz
from EvenorOdd import even_or_odd
from Exchanging_values import exchange_value
from Factorial import factorial
from Firsttennaturalnumbers import first_ten_naturalnos
from foobar import foobar
from Grading import grading
from Leapyear import leap_year
from MaxBet2no import max_bet_twonos
from MaxBet3no import max_bet_threenos
from Multiplicationtable import mul_table
from Numbersfromlist import nums_from_list
from Numbersinreverseorder import nums_in_reverseorder
from Oddpositionindex import odd_positions_index
from Patterns import patterns
from PerimeterandArea import perimeter_area
from Reverseorderlist import reverse_order_list
from Sumofnnumbers import sum_of_n_nos
from Voting import voting
from Whileloop import srs
from Divisibleby5and11 import div_5_nd_11

def main():

    #DR Fan Quiz Contest
    print("WELCOME TO DR FAN QUIZ CONTEST",end="")
    print(""" \033[94m
            ****.****
           ***********
           ***********
             *******    
               ***
                *
    """)
    participants=[]
    score=0
    print("+++++++++++++++++++")
    print("Enter your details:")
    print("+++++++++++++++++++")
    for i in range(1):
        name=input("Enter name:")
        age=int(input("Enter age:"))
        participants.append([name,age])
        playing=input("Do you want to participate in the contest?\n ")
        if playing=='yes':
            print("=============================================")
            print("Answer the questions below to win the contest")
            print("=============================================")
            print("The Quiz Begins!")
            print("=============================================")
            print("Q.1 What is Darshan Raval's age?")
        correctanswer=30
        answer=int(input("Enter answer: "))
        if answer==correctanswer:
            print("Hurray! You got 1 point :) \n")
            score=score+1
        else:
            print("Oops answer is incorrect :( \n")  

        print("Q.2 What is Darshan Raval's fans known as?")
        correctanswer="Blue Family"
        answer=input("Enter answer: ")
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n") 
        
        print("Q.3 What is Darshan Raval's favourite colour?")
        correctanswer="Blue"
        answer=input("Enter answer: ")
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n") 

        print("Q.4 Name his favourite food?") 
        correctanswer="Doodh Khichdi"
        answer=input("Enter answer: ")
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n")  
    
        print("Q.5 Name the show where he made his first television appearance ?")
        correctanswer="India's Raw Star"
        answer=input("Enter answer: ")
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n")  

        print("Q.6 Name the song that was loved by everyone from his originals?")
        correctanswer="Pehli Mohabbat"
        answer=input("Enter answer: ")
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n")  
        
        print("Q.7 When was his first album released?")
        correctanswer=2020
        answer=int(input("Enter answer: "))
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n")  
        
        print("Q.8 In which year did he made his debut with one of his original?")
        correctanswer=2017
        answer=int(input("Enter answer: "))
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n")  
        
        print("Q.9 Which song from the album did he dedicated to his mother?")
        correctanswer="Maa"
        answer=input("Enter answer: ")
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n")

        print("Q.10 How many albums did he release till date?")
        correctanswer=2
        answer=int(input("Enter answer: "))
        if answer==correctanswer:
         print("Hurray! You got 1 point :) \n")
         score=score+1
        else:
         print("Oops answer is incorrect :( \n") 

        print(f"Your total score is: {score} \n ")
        if score<=5:
         print("You are a new fan")
        elif score>5 and score<10:
         print("You are an average fan")
        else:
         print("You are a Darshaner") 

    else:
        print("Bye bye!")
    

    #Program 5
    #Check whether the number is even or odd
    #Input
    number=int(input("Enter number: "))
    #Process
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")

    #Program18
    var1,var2="Manisha","Sharma"
    print(var1)
    print(var2)
    exchange=var1,var2=var2,var1
    print(exchange)
 
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

    #Program16
    #Print first 10 natural numbers
    for i in range(1,11):
        print(i) 

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
        
               
   

    
        
