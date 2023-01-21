from env import Reversi
import sys
if __name__ == "__main__":
    print("Welcome to Reversi!")
    print("What would you like to do?")
    print("1. Start a new game.")
    print("2. Exit")
    while True:
        try:
            choice = int(input())
            if choice == 1:
                print("What size do you want the board to be? \nEnter a positive even integer greater than 2.")
                while True:
                    try:
                        choice = int(input())
                        break
                    except ValueError:
                        print("Please enter a positive even integer greater than 2!")

                board = Reversi(choice)
                print()


                end = False
                while end == False:
                    if (board.white_move):
                        print()
                        print("White's turn to play!")
                    else:
                        print()
                        print("Black's turn to play!")
                    board.rendor()
                    print(f"Action space: {board.action_space}")
                    print("Where would you like to place your piece? Enter a coordinate in the form (x,y)")
                    while True:
                        try:
                            choice = tuple(input().split(','))
                            coordinate = (int(choice[0].replace('(', '')), int(choice[1].replace(')', '')))
                            if coordinate not in board.action_space:
                                raise ValueError
                            break
                        except ValueError:
                            print("Please enter a valid coordinate!")

                    win = board.step(coordinate)

                    if win != 0:
                        end = True

            elif choice == 2:
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid choice!")



