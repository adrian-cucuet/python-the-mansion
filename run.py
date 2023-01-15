import pyfiglet
import emoji
from termcolor import colored

"""
Printing the Game Name
"""
game_name = pyfiglet.figlet_format("THE MANSION")
print(colored(game_name, 'yellow'))

"""
Asking the player for name and introduction to story
"""

player_name = input('Enter your name:\n')
print(f"Hello, {player_name} \U0001F603")
print("This game is a quest where you choose how the game ends.")
print("You will need to answer questions and take decissions.")
print("It's 3:30 AM. The phone's ringing. Who could it be?")
print("You answer. A voice at the other end says that it's the police.")
print("Your uncle, a noted scientist, has been found dead.")
print("Time to investigate the house for any clues to his death...")
print(f"Good luck \U0001F929 {player_name}!\n")
print("You are standing at entrance of the mansion.")
print("The gothic architecture lends a creepy feel to the entrance hall.")
print("You can go FORWARD to the other side of the entrance hall.")
print("There is also a door to your LEFT.")
print("You can see a glass-panel door to the RIGHT.")

"""
Second Bedroom quest
"""

def second_bedroom():
    print("\n")
    print("You find a letter where the killer is revealed!")
    answer_letter = input("\U0001F914 Would you give it to the police? (Y or N):\n")
    if answer_letter == "y":
        print("\n")
        you_win = pyfiglet.figlet_format("YOU WIN")
        print(colored(you_win, 'green'))
        print("\U0001F603 Good job! Police is going to arrest the killer")
    elif answer_letter == "n":
        print("\n")
        game_over = pyfiglet.figlet_format("GAME OVER")
        print(colored(game_over, 'red'))
        print("\U0001F61E The killer got away with the murder.")
    else:
        print(colored('Not a valid answer. You need to choose "y" or "n"!', 'red'))
        second_bedroom()

"""
Staircase quest
"""

def staircase():
    print("\n")
    print("You go up the stairs. You decide to check your uncles bedroom.")
    print("You find the bed made. \U0001F914 Looks like he didn't get to his bedroom the day he died.")
    answer_second_bedroom = input("\U0001F914 Would you like to check the second bedroom? (Y or N):\n")
    if answer_second_bedroom == "y":
        print("\n")
        second_bedroom()
    elif answer_second_bedroom == "n":
        print("\n")
        game_over = pyfiglet.figlet_format("GAME OVER")
        print(colored(game_over, 'red'))
        print("\U0001F61E You missed an important clue in the second bedroom.")
    else:
        print(colored('Not a valid answer. You need to choose "y" or "n"!', 'red'))
        staircase()

"""
Closet Hall quest
"""

def closet_hall():
    print("\n")
    print("You open the closet and you find a woman hat.")
    print("You realize the hat belongs to a collegue of your uncle.")
    answer_hat = input("\U0001F914 Would you INFORM the police about it or CONFRUNT the lady yourself?:\n")
    if answer_hat == "inform":
        print("\n")
        print("\U0001F603 Good job! Police is gonna question the lady about her hat.")
        staircase()
    elif answer_hat == "confrunt":
        print("\n")
        print("Because it's too late at night, you have to wait untill tomorrow.")
        print("\U0001F61E Now it's too late to use the hat as evidence.")
        staircase()
    else:
        print(colored('Not a valid answer. You need to choose "inform" or "confrunt"!', 'red'))
        closet_hall()

"""
Forward quest
"""

def forward():
    print("\n")
    print("You reached the end of the entrance hall.")
    print("There is a STAIRCASE here.\nYou can also go to CLOSET under the stairs.")
    answer_forward = input("\U0001F914 You want to go up the STAIRCASE or check the CLOSET:\n")
    if answer_forward == "staircase":
        staircase()
    elif answer_forward == "closet":
        closet_hall()
    else:
        print(colored ('Not a valid answer. You have to type "staircase" or "closet"!', 'red'))
        forward()

"""
Intro quest
"""

def intro():
    print("\n")
    answer_intro = input("\U0001F914 Where do you want to go? forward/left/right:\n")
    if answer_intro == "forward":
        forward()
    elif answer_intro == "left":
        print("\n")
        print("You enter in your late uncle's office and see on his desk a letter.")
        print("You pick up the letter an read it \U0001F9D0")
        print("You find out he had a meeting with the University dean two days ago.")
        print("You call the dean but he said your uncle never made it to ther meeting \U0001F615")
        intro()
    elif answer_intro == "right":
        print("\n")
        print("You have a walk in the garden and realize the flower beds are dry.")
        print("That is a clue your uncle didn't take care of the garden lately.")
        print("You are back in the house")
        intro()
    else:
        print(colored('Not a valid answer. You need to type "forward", "left" or "right"!', 'red'))
        intro()

intro()