import random
import time


print('-'*90)
print("welcome to Hangman game...!!!")
print("WIN THE GAME IF YOU CAN")
print('-'*90)
time.sleep(2)
playerName = input("Your name here: ")
print("Best of Luck!", playerName ,"!")
print('-'*90)
time.sleep(2)
print("Before starting...")
print("Note:")
print("1)players will be given limited chance to GUESS the correct word... ")
print("2)enter only one letter at a time.")
print("3)only enter letter in lowercase")
time.sleep(2)
print('-'*90)
print("Let's play Hangman!The game is about to start... goodluck!! ")
print('-'*90)
time.sleep(2)

def main():
    global countingMoves
    global display
    global word
    global alreadyGuessedWords
    global lengthOfWords
    
    with open("TWL_DRCFS_30DaysPythonBootcamp\Week 4\FInal Project\wordsfile.txt", "r") as file:
        allText = file.read()
    words = list(map(str, allText.split()))
    word=random.choice(words)
    lengthOfWords = len(word)
    countingMoves = 0
    display = '_' * lengthOfWords
    alreadyGuessedWords = []
    

def gameLoopToPlayAgain():
   playGame = input("Do You want to play again? y = yes, n = no \n")
   if playGame == "y" or playGame=="Y" or playGame=="yes" or playGame=="Yes" or playGame=="YES":
        print('-'*90)
        print("welcome back",playerName)
        print('-'*90)
        main()
   else:
        print('-'*90)
        print("thanks for playing...",playerName)
        print('-'*90)
def hangmanGame():
    global countingMoves
    global word
    global alreadyGuessedWords
    global play_game
    global display
    limit = 5
    guess = input(" Enter your guess: \n"+ display +":")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print('-'*90)
        print("Invalid Input, Try a letter\n")
        print('-'*90)
        hangmanGame()


    elif guess in word:
        alreadyGuessedWords.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in alreadyGuessedWords:
        print('-'*90)
        print(playerName," you already guessed this letter:",alreadyGuessedWords,"try new letter!!")
        print('-'*90)
    else:
        countingMoves += 1

        if countingMoves == 1:
            
            print("   *-*-*- \n"
                  "  *     | \n"
                  "  *       \n"
                  "  *       \n"
                  "  *       \n"
                  "  *       \n"
                  "  *       \n"
                  "__|__\n")
            print("That's Wrong guess",playerName )
            print('-'*90)

        elif countingMoves == 2:
            
            print("   *-*-*- \n"
                  "  *     | \n"
                  "  *     |\n"
                  "  *      \n"
                  "  *      \n"
                  "  *      \n"
                  "  *      \n"
                  "__|__\n")
            print("That's Wrong guess",playerName )
            print('-'*90)
        elif countingMoves == 3:
           
           print("   *-*-*- \n"
                  "  *     | \n"
                  "  *     |\n"
                  "  *     |\n"
                  "  *      \n"
                  "  *      \n"
                  "  *      \n"
                  "__|__\n")
           print("That's Wrong guess",playerName )
           print('-'*90) 
        elif countingMoves == 4:
            
            print("   *-*-*- \n"
                  "  *     | \n"
                  "  *     |\n"
                  "  *     | \n"
                  "  *     O \n"
                  "  *      \n"
                  "  *      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - countingMoves) + " last guess remaining\n")
            print('-'*90)
        elif countingMoves == 5:
           
            print("   *-*-*- \n"
                  "  *     | \n"
                  "  *     |\n"
                  "  *     | \n"
                  "  *     O \n"
                  "  *    /|\ \n"
                  "  *    / \ \n"
                  "__|__\n")
            print("That's Wrong guess",playerName,"you are hanged!!!" )
            print('-'*90)
            gameLoopToPlayAgain()

    if word == '_' * lengthOfWords:
        print("Congrats!", playerName, ".You have guessed the word correctly!")
        print('-'*90)
        gameLoopToPlayAgain()

    elif countingMoves != limit:
        hangmanGame()

if __name__=='__main__':
    main()
    hangmanGame()


