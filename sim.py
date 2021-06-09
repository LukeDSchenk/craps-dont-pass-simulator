import random
import sys

# random.randint(1, 101) # returns a random number between 1 and 100

### Returns a dice roll integer (1 thru 6).
def roll_die():
    return random.randint(1, 7)

### Rolls dice and plays a roll until a loss on don't pass
def play_dont_pass(start_cash, min_bet, roll_num):
    cash = start_cash
    on = None
    win = None
    print(f"Roll #{roll_num}; Cash: ${cash}; ", end='')
    cash -= min_bet

    while True:
        die_1 = roll_die()
        die_2 = roll_die()
        roll = die_1 + die_2

        # set the on number if nothing has been set
        if on == None:
            if 4 <= roll <= 10:
                on = roll
            elif roll == 2 or roll == 3:
                win = True
            elif roll == 7 or roll == 11:
                win = False
        else:
            if roll == on:
                win = False
            elif roll == 7:
                win = True

        if win == True:
            cash += (2 * min_bet)
            print(f"Won ${min_bet}")
            return win, cash
        elif win == False:
            print(f"Lost ${min_bet}")
            return win, cash


def main(start_cash=200, min_bet=25, num_rolls=100):
    print(f"Playing {num_rolls} rolls, starting with ${start_cash}, betting ${25}")

    cash = start_cash
    roll_num = 1
    for x in range(num_rolls):
        if cash < min_bet:
            break
        else:
            win, cash = play_dont_pass(cash, min_bet, roll_num)
            roll_num += 1

    print(f"\nFinished with ${cash} after {roll_num - 1} rolls!")

if __name__ == '__main__':
    help = '''
    Craps Don't Pass Line Betting Simulator v1.0

    Simulates playing the "don't pass" line in Craps, starting with
    $200 cash and always playing the minimum bet of $25.
    The Default number of rolls played is 100.

    Usage: sim.py [NUMBER OF ROLLS]
    '''

    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(help)
            sys.exit(0)
        else:
            num_rolls = int(sys.argv[1])
    except IndexError:
        num_rolls = None

    if num_rolls is not None:
        main(num_rolls=num_rolls)
    else:
        main()
