guesses = []
ANSWERS = ["b747", "b757" ,"b767" ,"b777" ,"b787" ,"a320" ,"a330" ,"a340" ,"a350", "a380"]

# FUNCTIONS

# Welcomes User
def intro():
    # Asks for the name
    name = input("What is your username?")

    #Greets the user
    print("Hello {}, welcome to the top 10 quiz.".format(name))
    print("This quiz is about the top 10 planes.")

# Asks user for lives
def getlives():
    while True:
        lives = input("How many chances do you want?")
        try:
            #validation check
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

# Checks if answer already exists in the list. Used for both correct answers and previous guesses
def inList(answer, list):
    if answer in list:
        return True
    else:
        return False

# MAIN CODE

intro()
lives = getlives()
score = 0

#Begin quiz
while lives > 0:
    answer = input("Name the top 10 planes.")
    # Checks if correct or wrong
    if inList(answer, ANSWERS):
        # Checks if already guessed or not
        if inList(answer, guesses):
            print("You've guessed that already")
        else:
            print("Correct")
            score += 1
            guesses.append(answer)
            print("You have guessed {}. Your score is {}. You have {} remaining".format(len(guesses), score))
    else:
        print("Wrong")
        lives -= 1
        print("You have guessed {}. Your score is {}. You have {} remaining".format(len(guesses), score))

# End game
print("Game Over, your final score is {}".format(score))              