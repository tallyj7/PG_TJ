import random

number = random.randint (0,2)

words = ["FORTNITE","BLACK OPPS 2","ROBLOX"]
hint1 = ["Tacticle shot gun","Nuke Town 3","Game like Minecraft"]
hint2 = ["Title Towers","First person shooter","Hide and seek"]

secretword = words[number]
guess = ""
counter = 1

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input().upper()
    if guess == secretword:
        print("Congrats, you won!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "HINT1":
        print(hint1[number])

    elif guess == "HINT2":
        print(hint2[number])

    elif guess == "FIRST LETTER":
        print(secretword[0])

    elif guess == "GIVE UP":
        print("The secret word was " + secretword)
        print("You failed " + str(counter) + " times.")

    else:
        counter += 1
        print("Guess again.")

