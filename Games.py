import Mood
from sys import exit
from random import randint

def main():

    while True:
        #input1 = input("> What's your current mood? (Happy/Angry/Stressed/Sad): " ).lower()
        if input1 == "happy":
            mood = Mood.Happy()
            break
        elif input1 == "angry":
            mood = Mood.Angry()
            break
        elif input1 == "stressed":
            mood = Mood.Stressed()
            break
        elif input1 == "sad":
            mood = Mood.Sad()
            break
        else:
            input1 = print ("Invalid input! Please enter Happy, Angry, Stressed or Sad only!\n> ")
        


        
    def calc(mood):
        return mood.stability * (mood.HMULT/mood.SMULT) * 100/randint(5, 10)
            
    def RPG():
        if input1 == "happy":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
        
    def FPS():
        if input1 == "angry":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
            
    def PnC():
        if input1 == "stressed":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
            
    def Sim():
        if input1 == "sad":
            print ("100% stability achieved!")
        else:
            print(f"Your mental stability is: {round(calc(mood), 2)}%.")
           
           

    while True:
        #input2 = input("> What game do you want to play?\nRPG/FPS/PnC/Sim?: ").lower()
        if input2 == "rpg":
            RPG()
            break
        elif input2 == "fps":
            FPS()
            break
        elif input2 == "pnc":
            PnC()
            break
        elif input2 == "sim":
            Sim()
            break
        else:
            input2 = print("Please choose from the option!")


main()