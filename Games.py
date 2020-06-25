import Mood
from sys import exit
from random import randint

def calc(setting):
    return setting.stability * (setting.HMULT/setting.SMULT) * 100/randint(5, 10)

def RPG(mood):
    if mood == "happy":
        data = "100% stability achieved!"
    else:
        data = f"Your mental stability is: {round(calc(mood), 2)}%."
    return data

def FPS(mood):
    if mood == "angry":
        data = "100% stability achieved!"
    else:
        data = "Your mental stability is: {round(calc(mood), 2)}%."
    return data

def PnC(mood):
    if mood == "stressed":
        data = "100% stability achieved!"
    else:
        data = "Your mental stability is: {round(calc(mood), 2)}%."
    return data

def Sim(mood):
    if mood == "sad":
        data = "100% stability achieved!"
    else:
        data = "Your mental stability is: {round(calc(mood), 2)}%."
    return data

def main(mood, games):

    if mood == "happy":
        setting = Mood.Happy()
    elif mood == "angry":
        setting = Mood.Angry()
    elif mood == "stressed":
        setting = Mood.Stressed()
    elif mood == "sad":
        setting = Mood.Sad()
                   
    if games == "rpg":
        games_result = RPG(mood)
    elif games == "fps":
        games_result = FPS(mood)
    elif games == "pnc":
        games_result = PnC(mood)
    elif games == "sim":
        games_result = Sim(mood)

    return games_result, mood
