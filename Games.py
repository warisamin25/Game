import Mood
from sys import exit
from random import randint

def main():

    while True:
        #input1 = input("> What's your current mood? (Happy/Angry/Stressed/Sad): " ).lower()
        if set_mood == "happy":
            setting = Mood.Happy()
            break
        elif mood == "angry":
            setting = Mood.Angry()
            break
        elif mood == "stressed":
            setting = Mood.Stressed()
            break
        elif mood == "sad":
            setting = Mood.Sad()
            break
        #else:
            #nput1 = print ("Invalid input! Please enter Happy, Angry, Stressed or Sad only!\n> ")
        


        
    def calc(setting):
        return setting.stability * (setting.HMULT/setting.SMULT) * 100/randint(5, 10)
            
    def RPG():
        if mood == "happy":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
        
    def FPS():
        if mood == "angry":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
            
    def PnC():
        if mood == "stressed":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
            
    def Sim():
        if mood == "sad":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
           
           

    while True:
        #input2 = input("> What game do you want to play?\nRPG/FPS/PnC/Sim?: ").lower()
        if set_games == "rpg":
            RPG()
            break
        elif games == "fps":
            FPS()
            break
        elif games == "pnc":
            PnC()
            break
        elif games == "sim":
            Sim()
            break
        #else:
            #input2 = print("Please choose from the option!")


main()