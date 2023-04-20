from functools import reduce
from time import sleep
import re

# def my_func(params):
#     print(f"I love {params}")

# my_func("args")


# *sleep(seconds)*


def introduction():
    print("   __________________________________________________________________________________")
    print(" / \                                                                                 \.")
    print("|   |                                                                                |.")
    print(" \_ |                                                                                |.")
    print("    |                                                                                |.")
    print("    |                      Welcome to my text adventure game.                        |.")
    print("    |                                                                                |.")
    print("    |                     Please enter your name and press ENTER                     |.")
    print("    |                         when you're ready to begin.                            |.")
    print("    |                                                                                |.")
    print("    |                                                                                |.")
    print("    |                                                                                |.")
    print("    |                                                                                |.")
    print("    |                                                                                |.")
    print("    |                                                                                |.")
    print("    |                                                                                |.")
    print("    |   _____________________________________________________________________________|___")
    print("    |  /                                                                                /.")
    print("    \_/dc__________________________________________________________________  __________/.")
    print("                                                                                         ")
    print("                                                                                         ")

    global player_name

    player_name = input("Enter you name here: ")

    cave_start(player_name)

def cave_start(player_name):
    sleep(1)
    print(f"   __________________________________________________________________________________")
    print(f" / \                                                                                 \.")
    print(f"|   |                                                                                |.")
    print(f" \_ |                                                                                |.")
    print(f"    |              {player_name} you wake up in a dark cave.                         |.")
    print(f"    |                                                                                |.")
    print(f"    |               You are surrounded by the bones of dead animals                  |.")
    print(f"    |               in a large pit with only a small shaft of light                  |.")
    print(f"    |               peeking through a crack in the roof of the cave.                 |.")
    print(f"    |                                                                                |.")
    print(f"    |               There are two passages in fron of you if you                     |.")
    print(f"    |               choose to CLIMB out of the pit.                                  |.")
    print(f"    |                                                                                |.")
    print(f"    |               You can feel a small breeze coming from the left passage,        |.")
    print(f"    |               and you hear grunting noises coming from the right passage.      |.")
    print(f"    |                               WHAT DO YOU DO?                                  |.")
    print(f"    |   _____________________________________________________________________________|___")
    print(f"    |  /                                                                                /.")
    print(f"    \_/________________________________________________________________________________/.")
    print(f"                                                                                         ")
    print(f"                                                                                         ")

    cave_choice = input("What do you do? ")

    clean_input = cave_choice.lower()
    if re.search("left", clean_input):
        cave_pit_fail()
    elif re.search("right", clean_input):
        cave_pit_fail()
    elif re.search("climb", clean_input):
        cave_pit_success()
    else: input("Try again. The hints are in the text. PRESS ANY BUTTON to continue"), cave_start(player_name)


def cave_pit_fail():
    print(f"   __________________________________________________________________________________")
    print(f" / \                                                                                 \.")
    print(f"|   |                                                                                |.")
    print(f" \_ |                                                                                |.")
    print(f"    |               You wake up in a dark cave with a huge headache.                 |.")
    print(f"    |                                                                                |.")
    print(f"    |               You are surrounded by the bones of dead animals                  |.")
    print(f"    |               in a large pit with only a small shaft of light                  |.")
    print(f"    |               peeking through a crack in the roof of the cave.                 |.")
    print(f"    |                                                                                |.")
    print(f"    |               There are two passages in fron of you if you                     |.")
    print(f"    |               choose to CLIMB out of the pit.                                  |.")
    print(f"    |                                                                                |.")
    print(f"    |               You should probably CLIMB out of the pit before you try          |.")
    print(f"    |               to do anything else.                                             |.")
    print(f"    |               WHAT DO YOU DO?                                                  |.")
    print(f"    |   _____________________________________________________________________________|___")
    print(f"    |  /                                                                                /.")
    print(f"    \_/________________________________________________________________________________/.")
    print(f"                                                                                         ")
    print(f"                                                                                         ")

    cave_choice = input("What do you do this time? ")

    clean_input = cave_choice.lower()
    if re.search("climb", clean_input):
        cave_pit_success()        
    else: 
        input("You fall and impale yourself on a jagged animal bone! ||RIP|| PRESS ENTER TO TRY AGAIN "), introduction()    
    

def cave_pit_success():
    
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |               You struggle to climb out of the trecherous pit,                 |.")
        print(f"    |               but you eventually reach the top of the pit.                     |.")
        print(f"    |                                                                                |.")
        print(f"    |               You can now see both the left and right passages clearly.        |.")
        print(f"    |               The left passage smells like a sewer, but you can feel air       |.")
        print(f"    |               moving from that direction.                                      |.")
        print(f"    |                                                                                |.")
        print(f"    |               The right passage is still and darker than the left              |.")
        print(f"    |               but it doesn't smell like death.                                 |.")
        print(f"    |                                                                                |.")
        print(f"    |                          Which path will you take?                             |.")
        print(f"    |                                                                                |.")
        print(f"    |   _____________________________________________________________________________|___")
        print(f"    |  /                                                                                /.")
        print(f"    \_/________________________________________________________________________________/.")
        print(f"                                                                                         ")
        print(f"                                                                                         ")
   
        direction_choice = input("What do you do? ")

        clean_input = direction_choice.lower()
        if re.search("left", clean_input):
            cave_path_left()
        elif re.search("right", clean_input):
            cave_path_right()    
        else: input("Try again. The hints are in the text. PRESS ANY BUTTON to continue"), cave_pit_success()

def cave_path_left():
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |               As you make your way down the left path you see                |.")
        print(f"    |               sunlight getting brighter as you make your way through                     |.")
        print(f"    |               the tunnel.                                                                 |.")
        print(f"    |                      |.")
        print(f"    |               As you get closer to the light you see a large rock        |.")
        print(f"    |               sitting in the sun.                                     |.")
        print(f"    |                                                                                |.")
        print(f"    |               The right passage is still and darker than the left              |.")
        print(f"    |               but it doesn't smell like death.                                 |.")
        print(f"    |                                                                                |.")
        print(f"    |                          Which path will you take?                             |.")
        print(f"    |                                                                                |.")
        print(f"    |   _____________________________________________________________________________|___")
        print(f"    |  /                                                                                /.")
        print(f"    \_/________________________________________________________________________________/.")
        print(f"                                                                                         ")
        print(f"                                                                                         ")
   


def cave_path_right():
    print("Right path")

introduction()