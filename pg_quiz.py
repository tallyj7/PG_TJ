import pyautogui as pg
import time
import webbrowser

points = 0

# Question

answer = pg.prompt(
"""
Which would you rather do

a) Study for a test and get an A, but not play Fortnite
b) Play Fortnite and win in solos, but fail the test
c) Get top 20 in Fortnite with 5 kills, study, and get a B+
"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 5
elif answer == "c":
    points += 3

# Question 2

answer = pg.prompt(
"""
Which weapon in Fortnite?

a) Blue Tacticle Shotgun
b) Scar
c) Rocket Launcher
"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 3
elif answer == "c":
    points += 4


    # Question 3

answer = pg.prompt(
"""
Which has the most loot?

a) Titled Towers
b) Snobby Shores
c) Moisty Mire
"""
    )
# Give points

if answer == "a":
    points += 4
elif answer == "b":
    points += 3
elif answer == "c":
    points += 1

    # Question 4

answer = pg.prompt(
"""
Which one of these is a new place on the map?

a) Moisty Mire
b) Greasy Grove
c) Shaky Shack
"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 1
elif answer == "c":
    points += 4

     # Question 5

answer = pg.prompt(
"""
Which of these places has a name on the map?

a) The Prison
b) Flush Factory
c) The Motel
"""
    )
# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 4
elif answer == "c":
    points += 1

    # end of survey

pg.alert("You are...")

# Noob
if points < 7:
    pg.alert("You are a NOOB")
    webbrowser.open("https://www.youtube.com/watch?v=Pji0pE0gpNY")
# Inexperienced
elif points >= 8 and points < 14:
    pg.alert("Your bad")
    webbrowser.open("https://www.youtube.com/watch?v=YHVTnI7NnOc")
#Skilled
elif points >= 15 and points < 21:
    pg.alert("Your sick")
    webbrowser.open("https://www.youtube.com/watch?v=XorRpjCoRBE")
#ZSTERNY
elif points >= 21:
    pg.alert("You are ZSTERNY")
    webbrowser.open("webrowser.open("")")
