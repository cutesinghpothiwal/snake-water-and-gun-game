# snake water gun game
import random

 
lis= ['s', 'w' , 'g']
ran= random.choice(lis)
attempt= 1
c_point= 0
your_point=0
attempts_left=11

print ("welcome to snake water and gun\n" )
print ("rules are simple snake drinks water\n"
       "gun falls in water \n"
       "gun kills sanke \n" )
name= input(" please enter your name:\n" )


while(attempt<=10):
 inp= input("choose between s for snake w for water and g for gun: ")
 inp=inp.lower()
 if inp==ran:
    print("its a tie")
    c_point=+ c_point
    your_point =+ your_point
    print("both get one point  \n")
    
 elif inp=='s' and ran=='w':
     
     your_point = your_point +1
     print(f"you choose {inp} and computer choose {ran}") 
     print("you win the round ")
     print("you get 1 point \n")
     
 elif inp=='s' and ran=='g':
     
     c_point = c_point +1
     print(f"you choose {inp} and computer choose {ran}")
     print("you lose the round ")
     print (" computer gets 1 point \n")
     
 elif inp=='w' and ran=='s':
     
     c_point = c_point +1
     print(f"you choose {inp} and computer choose {ran}")
     print("you lose the round ")
     print (" computer gets 1 point \n")
     
 elif inp=='w' and ran =='g':
     
     your_point = your_point +1
     print(f"you choose {inp} and computer choose {ran}") 
     print("you win the round ")
     print("you get 1 point \n")
     
 elif inp=='g' and ran == 's':
     
     your_point = your_point +1
     print(f"you choose {inp} and computer choose {ran}") 
     print("you win the round ")
     print("you get 1 point \n")
 
    
 elif inp=='g' and ran == 'w':
     
     
     c_point = c_point +1
     print(f"you choose {inp} and computer choose {ran}")
     print("you lose the round ")
     print (" computer gets 1 point \n")
     
 else:

        print("Invalid Input")



 

 attempt = attempt +1
 
 print(f"Number of gueses left = {attempts_left - attempt}")

 if(attempt>10):

         print("Game Over!")
 


print(f"your score is {your_point} and computer's score is {c_point} \n")

if your_point>c_point:
    print(f"congrats {name} have won the game ")
    
elif your_point<c_point:
    print(f"sorry {name} lose better luck next time \n")

else :
    print ("its a tie\n")    

     
     