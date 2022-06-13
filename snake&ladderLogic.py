
import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
SLEEP_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# snake takes you down from 'key' to 'value'
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87
}

# ladder takes you up from 'key' to 'value'
ladders = {
    4: 20,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

player_turn_text = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang",
    "ouch",
    "It hurted"

]

ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]


def welcome_msg():
    msg = """
    Welcome to Snake and Ladder Game
    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Hit enter to roll the dice.
         Move forward the number of spaces shown on the dice.

      2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
         You have Ladder @ block number 4,11,15,17,22,38,49,57,61,73,81 and 88.

      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
         You Have snakes @ block Number 8,18,26,39,51,54,56,60,75,83,85,90,92 and 97. 
                Aaah...there  are more snakes than the ladder!
                 Not fair enough :-(

      4. The first player to get to the FINAL position is the winner.
      
      5.Are You Brave Enough to Get to the 100th Block?  
    """
    print(msg)


def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name


def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        replay=input("Do you wish to play the game again?\n Type Yes/No")
        if replay=="yes" :
            start()
        else :
            sys.exit()
            

def start():
    welcome_msg()
    status=input("\n Type 'yes' if you are brave enough to continue with the game.\n If you wish to give upp the game type 'no'  \n")
    if status=="yes" :
        time.sleep(SLEEP_BETWEEN_ACTIONS)
        player1_name, player2_name = get_player_names()
        time.sleep(SLEEP_BETWEEN_ACTIONS)

        player1_current_position = 0
        player2_current_position = 0

        while True:
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            input_1 = input("\n" + random.choice(player_turn_text) + player1_name + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player1_name + " moving....")
            player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

            check_win(player1_name, player1_current_position)

            input_2 = input("\n" + random.choice(player_turn_text) + player2_name  + " Hit the enter to roll dice: ")
            print("\nRolling dice...")
            dice_value = get_dice_value()
            time.sleep(SLEEP_BETWEEN_ACTIONS)
            print(player2_name + " moving....")
            player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

            check_win(player2_name, player2_current_position)
    else :
        sys. exit()




if __name__ == "__main__":
    start()
    while 1:
        game=input("Sure to exit?\n Yes/No")
        if game!="yes":
            start()
        else:
            sys.exit()   