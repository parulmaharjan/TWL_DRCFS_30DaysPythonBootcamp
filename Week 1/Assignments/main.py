#Rock,Paper&Scissors game
import random
choice=['Rock','Paper','Scissors']
YouWin,Computerwin=0,0
print('*****Get ready to play Rock,Paper& Scissors*****') #starting game
while True:
     #using for loop to play game 5 times
     for round in range(1,6):
          #remaining round
          print('you have',6-round,'round remaing')
          #starting round
          print('Round', round ,'is starting')
          #taking choices input from user  
          userChoice = int(input('Enter your Choice 1:Rock 2:Paper 3:Scissors:  '))
          #using if-else statements to check the condition
          if userChoice==1:
               print('you choose Rock')
               YourChoice="Rock"
          elif userChoice==2:
               print('your choose Paper')
               YourChoice="Rock"
          elif userChoice==3:
               print('you choose Scissors')  
               YourChoice="Rock"
          else: 
               print('Invalid Choice please resart the game and input correct choice')
               exit()
          computerChoice =random.choice(choice) 
          print('Computer choose:',computerChoice)
          if YourChoice==computerChoice:    
               YouWin+=1
               Computerwin+=1
               print("This Round is Draw:")
          elif (YourChoice=="Paper" and computerChoice=="Rock") or (YourChoice=="Rock" and computerChoice=="Scissors") or(YourChoice=="Scissors" and computerChoice=="Paper"):
               YouWin+=1
               print("You win this Round")
          else:
               Computerwin+=1
               print("Computer win this Round")
          #CHOOSING WINNER
     if YouWin>Computerwin:
          print("Score are:Your score:",YouWin,",Computer score:",Computerwin)
          print('*****Congrats you won this game*****')
          

     elif Computerwin>YouWin:
          print("Score are:Your score:",YouWin,",Computer score:",Computerwin)
          print('*****Computer won this game sorry try again***** ')  
          
        
     elif YouWin==Computerwin:
          print("Score are:Your score:",YouWin,",Computer score:",Computerwin)
          print('*****Match draw*****')
     else:
          break
     replay=input("Want to Play again?(Yes/Exit)")
     if replay=='yes' or replay=='Yes' or replay=='YES':
          continue             
     else:
          break


  #guessing game
import random
randomnumber=random.randint(1,30)
print('welcome to guessing game!!! Guess the number in 5 tries')
for i in range(1,6):
    print("you have total", 6-i, "tries remaining out of 5")
    userInput=int(input(' Enter your input between 1 and 30:'));
    if userInput==randomnumber:
        print("*****correct guess,you won***** ");
    elif userInput>randomnumber:
        print("*****your guess is greater*****");
    elif userInput<randomnumber:
        print("*****your guess is low*****");  
print("actual number to be guessed:",randomnumber)      
if i == 5:
    print("***** Try again!!!You're a bad guesser*****")

