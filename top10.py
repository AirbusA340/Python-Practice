import random

score = 0
MAX_TURNS = 10
ANSWERS = ["nobody, nothing, north, nickles, never, noggin, nicely, nice, niece, niger"]

# FUNCTIONS

def intro():
    name = input("What is your username?")

    print("Welcome to the top 10 quiz.", name)
    print("This quiz is about the top 10 n-words.")

# MAIN CODE

intro()

def getlives():
    while True:
        lives = input("How many chances do you want?")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("Please choose a positive number")
        except:
            print("That wasn't a number")

lives = getlives()

def isCorrect(answer, ANSWERS):
    if answer in ANSWERS:
        return True
    else:
        return False
score = 0
while lives > 0:
    answer = input("Name the top 10 n-words.")

    if isCorrect(answer, ANSWERS) == True:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        lives -= 1
                          