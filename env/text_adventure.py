from functools import reduce
from time import sleep
import re
from playsound import playsound
import logging


# def my_func(params):
#     print(f"I love {params}")

# my_func("args")


# *sleep(seconds)*
logging.basicConfig(filename="logs.txt", encoding="utf-8", level=logging.INFO)

def introduction():
    sleep(1)
    playsound("./creepy-cave-47164.mp3")
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
    print("    |                    WARNING: Some sounds are a little loud.                     |.")
    print("    |                   You might want to turn your volume down a little             |.")
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
    logging.info({player_name})

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
    print(f"    |               You can feel a small breeze coming from the LEFT passage,        |.")
    print(f"    |               and you hear grunting noises coming from the RIGHT passage.      |.")
    print(f"    |                               WHAT DO YOU DO?                                  |.")
    print(f"    |   _____________________________________________________________________________|___")
    print(f"    |  /                                                                                /.")
    print(f"    \_/________________________________________________________________________________/.")
    print(f"                                                                                         ")
    print(f"                                                                                         ")
    playsound('./quake-and-break-99034.mp3')

    cave_choice = input("What do you do? ")
    logging.info({cave_choice})
    clean_input = cave_choice.lower()
    if re.search("left", clean_input):
        cave_pit_fail()
    elif re.search("right", clean_input):
        cave_pit_fail()
    elif re.search("climb", clean_input):
        cave_pit_success()
    else: input("Try again. The hints are in the text. PRESS ANY BUTTON to continue"), cave_start(player_name)


def cave_pit_fail():
    sleep(1)
    print(f"   __________________________________________________________________________________")
    print(f" / \                                                                                 \.")
    print(f"|   |                                                                                |.")
    print(f" \_ |                                                                                |.")
    print(f"    |               You wake up in a dark cave with a huge headache.                 |.")
    print(f"    |                                                                                |.")
    print(f"    |               You are back in the pit.                                         |.")
    print(f"    |               Your head hurts a lot. You must have hit it on something.        |.")
    print(f"    |                                                                                |.")
    print(f"    |                                                                                |.")
    print(f"    |               There are two passages in front of you if you                    |.")
    print(f"    |               choose to CLIMB out of the pit.                                  |.")
    print(f"    |                                                                                |.")
    print(f"    |               You should probably CLIMB out of the pit before you try          |.")
    print(f"    |               to do anything else.                                             |.")
    print(f"    |                                WHAT DO YOU DO?                                 |.")
    print(f"    |   _____________________________________________________________________________|___")
    print(f"    |  /                                                                                /.")
    print(f"    \_/________________________________________________________________________________/.")
    print(f"                                                                                         ")
    print(f"                                                                                         ")
    playsound('./quake-and-break-99034.mp3')

    cave_choice = input("What do you do this time? ")

    logging.info({cave_choice})

    clean_input = cave_choice.lower()
    if re.search("climb", clean_input):
        cave_pit_success()        
    else: 
        sleep(1)
        playsound('./quake-and-break-99034.mp3')
        input("You fall and impale yourself on a jagged animal bone! ||RIP|| PRESS ENTER TO TRY AGAIN "), introduction()    
    

def cave_pit_success():
        sleep(1)
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |               You struggle to climb out of the trecherous pit,                 |.")
        print(f"    |               but you eventually reach the top of the pit.                     |.")
        print(f"    |                                                                                |.")
        print(f"    |               You can now see both the LEFT and RIGHT passages clearly.        |.")
        print(f"    |               The LEFT passage smells like a sewer, but you can feel air       |.")
        print(f"    |               moving from that direction.                                      |.")
        print(f"    |                                                                                |.")
        print(f"    |               The RIGHT passage is still and darker than the LEFT              |.")
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

        logging.info({direction_choice})

        clean_input = direction_choice.lower()
        if re.search("left", clean_input):
            cave_path_left()
        elif re.search("right", clean_input):
            cave_path_right()    
        else: input("Try again. The hints are in the text. PRESS ANY BUTTON to continue"), cave_pit_success()

def cave_path_left():
        sleep(1)
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |               As you make your way down the left path you see                  |.")
        print(f"    |               sunlight getting brighter as you make your way through           |.")
        print(f"    |               the tunnel.                                                      |.")
        print(f"    |                                                                                |.")
        print(f"    |               As you get closer to the light you WAIT andsee a large rock      |.")
        print(f"    |               sitting in the sunlight.                                         |.")
        print(f"    |                                                                                |.")
        print(f"    |               You can't make out the layout of the room because                |.")
        print(f"    |               your eyes are still adjusting to the bright sunlight.            |.")
        print(f"    |                                                                                |.")
        print(f"    |                         What do you do?                                        |.")
        print(f"    |                                                                                |.")
        print(f"    |   _____________________________________________________________________________|___")
        print(f"    |  /                                                                                /.")
        print(f"    \_/________________________________________________________________________________/.")
        print(f"                                                                                         ")
        print(f"                                                                                         ")
   
        left_entrance = input("What do you do? ")

        logging.info({left_entrance})

        clean_input = left_entrance.lower()
        if re.search("wait", clean_input):
            cave_left_wait()
        elif re.search("move", clean_input):
            cave_left_chamber()    
        elif re.search("continue", clean_input):
            cave_left_chamber()    
        elif re.search("enter", clean_input):
            cave_left_chamber()    
        else: input("Try again. The hints are in the text. PRESS ANY BUTTON to continue"), cave_path_left()


def cave_left_wait():
        sleep(1)
        playsound("./halloween-horror-sound-lurking-monster-145070.mp3")
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |               As your eyes adjust to the light you realize that the rock       |.")
        print(f"    |               is not a rock at all. It's a giant snake and it uncoils and      |.")
        print(f"    |               turn to look at you.                                             |.")
        print(f"    |                                                                                |.")
        print(f"    |               The snake says Hi, I just finished eating a bear. I'm not hungry |.")
        print(f"    |               so I'll let you pass if you can answer my riddle.                |.")
        print(f"    |                                                                                |.")
        print(f"    |               Tell me a palindrome that is longer than 5 letters.              |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                         What do you do?                                       |.")
        print(f"    |                                                                                |.")
        print(f"    |   _____________________________________________________________________________|___")
        print(f"    |  /                                                                                /.")
        print(f"    \_/________________________________________________________________________________/.")
        print(f"                                                                                         ")
        print(f"                                                                                         ")


        snake_palindrome = input("What do you do? ")

        logging.info({snake_palindrome})

        clean_str = reduce(lambda x, y: x + y, snake_palindrome.split(" "))

        if clean_str[::-1] == clean_str and len(clean_str) > 4:
             escape_cave()
        else: 
            sleep(2)
            playsound("./fuzzy-jumpscare-80560.mp3")
            print(f"   __________________________________________________________________________________")
            print(f" / \                                                                                 \.")
            print(f"|   |                                                                                |.")
            print(f" \_ |                                                                                |.")
            print(f"    |               The snake laughs and says: I think I might be hungry for         |.")
            print(f"    |               a snack after all.                                               |.")
            print(f"    |                                                                                |.")
            print(f"    |               The snake rears up and strikes at you and everything             |.")
            print(f"    |               goes dark.                                                       |.")
            print(f"    |                                                                                |.")
            print(f"    |                Never odd or even.                                              |.")
            print(f"    |                                                                                |.")
            print(f"    |                                                                                |.")
            print(f"    |                                                                                |.")
            print(f"    |                                                                                |.")
            print(f"    |                                                                                |.")
            print(f"    |   _____________________________________________________________________________|___")
            print(f"    |  /                                                                                /.")
            print(f"    \_/________________________________________________________________________________/.")
            print(f"                                                                                         ")
            print(f"                                                                                         ")

            sleep(5)

            input("You died! ||RIP|| PRESS ENTER TO START AGAIN")
            introduction()

def escape_cave():
     playsound("./throat-singing-in-a-cave-25481.mp3")
     print("The snake lets you pass, and you see a way out of the cave.")
     input("Congrats!!! You escaped the cave!!! THE END! PRESS ENTER TO PLAY AGAIN")
     logging.info(f"{player_name} beat the game")
     introduction()
        

def cave_left_chamber():
        sleep(1) 
        playsound("./fuzzy-jumpscare-80560.mp3")
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |               The snake rears up and strikes at you and everything             |.")
        print(f"    |               goes dark.                                                       |.")
        print(f"    |                                                                                |.")
        print(f"    |               Yes, the giant rock sitting in the sun was a giant snake.        |.")
        print(f"    |               Maybe you should have waited for your eyes to adjust.            |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |   _____________________________________________________________________________|___")
        print(f"    |  /                                                                                /.")
        print(f"    \_/________________________________________________________________________________/.")
        print(f"                                                                                         ")
        print(f"                                                                                         ")

        input("You died ||RIP|| PRESS ENTER TO TRY AGAIN")
        logging.info(f"{player_name} died")
        introduction()




def cave_path_right():

    sleep(1) 
    print(f"   __________________________________________________________________________________")
    print(f" / \                                                                                 \.")
    print(f"|   |                                                                                |.")
    print(f" \_ |                                                                                |.")
    print(f"    |               You can't see anything. There is no light at all.                |.")
    print(f"    |               You can feel your way FORWARD, but you can't see anything.       |.")
    print(f"    |                                                                                |.")
    print(f"    |               Do you continue FORWARD or go back to the LEFT passage?          |.")
    print(f"    |                                                                                |.")
    print(f"    |                                                                                |.")
    print(f"    |                              What do you do?                                   |.")
    print(f"    |                                                                                |.")
    print(f"    |                                                                                |.")
    print(f"    |                                                                                |.")
    print(f"    |                                                                                |.")
    print(f"    |                                                                                |.")
    print(f"    |   _____________________________________________________________________________|___")
    print(f"    |  /                                                                                /.")
    print(f"    \_/________________________________________________________________________________/.")
    print(f"                                                                                         ")
    print(f"                                                                                         ")
    
    
    right_passage = input("What do you do? ")

    logging.info({right_passage})

    clean_input = right_passage.lower()
    if re.search("forward", clean_input):
        cave_path_right_failure()
    elif re.search("left", clean_input):
        cave_path_left()    
    else: input("Try again. The hints are in the text. PRESS ANY BUTTON to continue"), cave_path_right()

def cave_path_right_failure():
        sleep(1) 
        print(f"   __________________________________________________________________________________")
        print(f" / \                                                                                 \.")
        print(f"|   |                                                                                |.")
        print(f" \_ |                                                                                |.")
        print(f"    |               You wake up and your body hurts all over.                        |.")
        print(f"    |               You don't know what happened but you're back in the pit again.   |.")
        print(f"    |               It feels like you fell back into the hole.                       |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                You will have to CLIMB out of the hole again.                   |.")
        print(f"    |                              What do you do?                                   |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |                                                                                |.")
        print(f"    |   _____________________________________________________________________________|___")
        print(f"    |  /                                                                                /.")
        print(f"    \_/________________________________________________________________________________/.")
        print(f"                                                                                         ")
        print(f"                                                                                         ")
        playsound('./quake-and-break-99034.mp3')

        pit_climb = input("What do you do this time? ")

        logging.info({pit_climb})

        clean_input = pit_climb.lower()
        if re.search("climb", clean_input):
            cave_pit_success()        
        else:
            sleep(1) 
            playsound('./quake-and-break-00934.mp3')
            input("You fall and impale yourself on a jagged animal bone! ||RIP|| PRESS ENTER TO TRY AGAIN "), introduction()
sleep(1)
introduction()