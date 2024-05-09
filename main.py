print ("Hello")
score = 0
play = "yes"

#Starting the quiz
name = input("What is your name?")

print("Hello {}, welcome to Fortnite.".format(name))
print("This quiz is about airplanes.")
while play == "yes":
    #Asking the question
    answer = input("Which 2 companies are the main manufacturers for the global amount of aircraft fleets?")

    #Answer lists
    if answer == "boeing and airbus" or answer == "airbus and boeing":
        print("Correct.")
        print("Next Question.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    else:
        print("lol no it's Boeing and Airbus.")

    #Repeat
    answer = input("Which of the 2 mentioned companies were founded first?")

    if answer == "boeing":
        print("Correct.")
        print("Next Question.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    else:
        print("lol no it's Boeing.")

    #Question 3
    answer = input("Which wide-body is the most recent in the Airbus company?")

    if answer == "A350" or answer == "airbus a350" or answer == "airbus a350-900" or answer == "a350-900" or answer == "a350":
        print("Correct.")
        print("Next Question.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    else:
        print("lol no it's the A350-900.")

    #Question 4
    answer = input("Apart from the B747, which other Boeing wide-body aircraft is also well known?")

    if answer == "b777" or answer == "boeing 777" or answer == "Boeing 777" or answer == "boeing 777 family" or answer == "777":
        print("Correct.")
        print("Next Question.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    else:
        print("lol no it's the B777.")

    #Question 5
    answer = input("True or False, air travel is the most safest mode of transport.")

    if answer == "true" or answer == "True":
        print("Correct.")
        print("Next Question.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    else:
        print("Wrong, it's true.")

    #Question 6
    question = "Which aircraft is known as the 'butter machine'? Type the letter."
    a = "Boeing 767"
    b = "Airbus A320"
    c = "Airbus A330"
    d = "Boeing 727"
    answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d))
    if answer == c or answer == "c":
        print("Correct.")
        print("Next Question.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    elif answer != c or answer != "c":
        print("No it's the A330 lol.")

    #Question 7
    question = "What aircraft type crashed landed on the Hudson River in a 2009 miraculous non-fatal accident?"
    a = "Boeing 737"
    b = "Airbus A320"
    c = "Airbus A300"
    d = "Boeing 707"
    answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d))
    if answer == b or answer == "b":
        print("Correct.")
        score += 1
    elif answer == "":
        print("An answer is required.")
    elif answer != b or answer != "b":
        print("No it's the A320 lol.")

    #Ending the quiz
    print("You've reached the end of the quiz.")
    print("Your score is", score)

    #Extra consideration
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
    elif score >= 5:
        print("Awesome work!")

    play = input("Do you want to play again?")
if answer == "No" or answer== "no":
    print("Thanks for playing!")