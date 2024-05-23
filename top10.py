import random

score = 0
MAX_TURNS = 10

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