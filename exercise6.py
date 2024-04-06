# Snake water gun game 
# Create a snake water gun game in Python!
# Search Snake water gun game in google 
# if you need help on rules and how to play the game!
# #Code with harry 
# exercise 6
#From python tutorial for absolute Beginner course 
import random
lst=["s","w","g"]
try:
     user_point=0
     computer_point=0
     print("Welcome to our snake,waterand gun game")
     print("You have 10 chance")
     print(
"If you enter any thing except smaller ('g','w','s').Computer got the point."
      )
     number_of_chances=1
     while(number_of_chances<=10):
        a=input("Enter s for snake ,g for gun ,w for water ")
        if random.choice(lst)=="s" and a =="w":
         print("User got the point")
         user_point+=1
        elif random.choice(lst)=="s" and a =="g":
         print("User got the point")
         user_point+=1
        elif random.choice(lst)=="w" and a =="g":
         print("User got the point")
         user_point+=1
        elif random.choice(lst)=="g" and a =="w":
         print("Computer got the point")
         computer_point+=1
        elif random.choice(lst)=="w" and a =="s":
         print("Computer got the point")
         computer_point+=1
        elif random.choice(lst)=="g" and a =="s":
         print("Computer got the point")
         computer_point+=1
        elif random.choice(lst)=="s" and a=="s":
         print("It is a draw")
        elif random.choice(lst)=="g" and a=="g":
         print("It is a draw")
        elif random.choice(lst)=="w" and a=="w":
         print("It is a draw")
        else:
         print("Computer got the point")
         computer_point+=1
        print(10-number_of_chances,"no of chances left") 
        number_of_chances=1+number_of_chances 
        while number_of_chances>10:
         if user_point>computer_point:
          print("You won aganist computer")
          break   
         elif user_point<computer_point:
          print("You lose aganist computer") 
          break
         else:      
          print("Computer and user get same points")
          break          
except Exception as e:
 print(e)