
import random
randomnumber=print(random.randint(1,30));

for i in range(5):
    userInput=int(input('your input:'));
    if userInput==randomnumber:
        print("you won you are a good guesser");

    elif userInput>randomnumber:
        print("your guess is greater");
    elif userInput<randomnumber:
        print("your guess is low");    
        



