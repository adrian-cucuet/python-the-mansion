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