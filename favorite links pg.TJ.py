import pyautogui as pg
import webbrowser

video = ["https://www.youtube.com/watch?v=v-1MQ0Cnbhs", "https://www.youtube.com/watch?v=4P8gBYkh2oo"]

sports = ["https://www.google.com/search?q=nhl&rlz=1C1GCEA_enUS752US752&oq=nhl&aqs=chrome..69i57j69i60l3j0l2.3011j0j4&sourceid=chrome&ie=UTF-8#sie=lg;/g/11c2l9b6b6;7;/m/05gwr;mt;fp;1", "https://www.google.com/search?q=nba&rlz=1C1GCEA_enUS752US752&oq=nba&aqs=chrome..69i57j0l5.1033j0j9&sourceid=chrome&ie=UTF-8#sie=lg;/g/11b_2r7j6m;3;/m/05jvx;mt;fp;1", "https://www.nfl.com/", "https://www.google.com/search?q=baseball&rlz=1C1GCEA_enUS752US752&oq=baseball&aqs=chrome..69i57j0l5.7005j1j4&sourceid=chrome&ie=UTF-8#sie=lg;/x/384qrgqnmrx4_;4;/m/09p14;mt;fp;1"]

answer = pg.prompt(
"""

what do you want to do?

a) watch videos

b) sports standings

""")
if answer == "a":
     for i in video:
         webbrowser.open(i)
elif answer == "b":
    for i in sports:
        webbrowser.open(i)
