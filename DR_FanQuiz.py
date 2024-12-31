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
 


 
  
