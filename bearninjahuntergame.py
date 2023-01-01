import random
import time

competitor = ["Bear", "Ninja", "Hunter"]

print("\nWelcome to The Bear, The Ninja and The Hunter\n")
points = 0
aipoints = 0

while True:
    playerchoice = None
    aichoice = random.choice(competitor) # to allow the computer to pick random competitor from the list
    while playerchoice not in competitor:
        playerchoice = input("\nPlease pick your character to fight with! \nHere are your choices: \n 1. Bear \n 2. Ninja \n 3. Hunter \nEnter your option: \n").capitalize()

    # starting game
    print(f"\nYou have choosen {playerchoice}, Goodluck! \n {playerchoice} proceeds to move through the woods....")
    game_encounter = "\n Traversing...\n"
    for char in game_encounter:
        print(char) 
        time.sleep(.25)
    # game conditions
    if playerchoice == aichoice: # both player and AI have choosen the same competitor, therefore a draw!!
        print(f"\n You have encounted a friendly {aichoice}, you are able to proceed on safely!\n")


    elif playerchoice == competitor[0]: # Player has choosen a bear
        if aichoice == competitor[1]:
            print(f"\n You have encountered a {aichoice}!! \n You have survived the encounter!! \n Moving on...")
            points += 1
        elif aichoice == competitor[2]:
            print(f"\n You have encountered a {aichoice}!! \n You have fell during the encounter!!\n Reviving...")
            aipoints += 1


    elif playerchoice == competitor[1]: # Player has choosen a Ninja
        if aichoice == competitor[2]: # met a hunter therefore win
            print(f"\n You have encountered a {aichoice}!! \n You have survived the encounter!! \n Moving on...")
            points += 1
        elif aichoice == competitor[0]: # met a bear therefore lose
            print(f"\n You have encountered a {aichoice}!! \n You have fell during the encounter!!\n Reviving...")
            aipoints += 1

    
    elif playerchoice == competitor[2]: # Player has choosen a hunter
        if aichoice == competitor[2]: # met a bear therefore win
            print(f"\n You have encountered a {aichoice}!! \n You have survived the encounter!! \n Moving on...")
            points += 1
        elif aichoice == competitor[0]: # met a ninja therefore lose
            print(f"\n You have encountered a {aichoice}!! \n You have fell during the encounter!!\n Reviving...")
            aipoints += 1

    print(f"\n Current Scoreboard: \n  1. Player {points}\n  2. Computer {aipoints}\n")
    
    
    if points == len(competitor):
        print(f"Congrats, You have won the game!\n Final Scores: \n  1. Player {points}\n  2. Computer {aipoints}\n ")
        break
    elif aipoints == len(competitor):
        print(f" Aww, You have lost the game!\n Final Scores: \n  1. Player {points}\n  2. Computer {aipoints}\n")
        break