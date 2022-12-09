
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
        
    
  

    
