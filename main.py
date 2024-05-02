print ("Hello")
score = 0

name = input("What is your name?")

print("Hello",name,", welcome to Fortnite.")
print("This quiz is about airplanes.")

answer = input("Which 2 companies are the main manufacturers for the global amount of aircraft fleets?")

if answer == "boeing and airbus":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "airbus and boeing":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "":
    print("An answer is required.")
else:
    print("lol no it's Boeing and Airbus.")

answer = input("Which of the 2 mentioned companies were founded first?")

if answer == "boeing":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "":
    print("An answer is required.")
else:
    print("lol no it's Boeing.")

answer = input("Which wide-body is the most recent in the Airbus company?")

if answer == "A350":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "airbus a350":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "airbus a350-900":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "a350-900":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "":
    print("An answer is required.")
else:
    print("lol no it's the A350-900.")

answer = input("Apart from the B747, which other Boeing wide-body aircraft is also well known?")

if answer == "b777":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "boeing 777":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "boeing 777 family":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "777":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "":
    print("An answer is required.")
else:
    print("lol no it's the B777.")

answer = input("True or False, air travel is the most safest mode of transport.")

if answer == "true":
    print("Correct.")
    print("Next Question.")
    score += 1
elif answer == "":
    print("An answer is required.")
elif answer == "True":
    print("Correct.")
    print("Next Question.")
    score += 1
else:
    print("Wrong, it's true.")

print("You've reached the end of the quiz.")
print("Your score is", score)

if score == 0:
    print("Are you even trying?")
elif score == 1:
    print("You need to improve a lot more.")
elif score == 2:
    print("You can try harder!")
elif score == 3:
    print("Not bad, decent knowledge.")
elif score == 4:
    print("Well done!")
elif score == 5:
    print("Awesome work!")