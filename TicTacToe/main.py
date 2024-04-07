from game_module import TicTacToe
from menu_module import menu

import os 

def clear():
    os.system('cls')

def main():
    while True:
        ex=False
        op=input(menu.main_menu())
        match op:
            case '1':
                clear()
                game_obj=TicTacToe.new_game()
                while True:
                    clear()
                    game_obj.print()
                    ## To check whether the board is full or not
                    full_check=game_obj.isfull()
                    if full_check:
                        break
                    ## get the position player wants to put the sign on
                    index=int(input(f"Select a position {game_obj.turn.name}:"))
                    move_check=game_obj.move(index)
                    if move_check:                     ## If the index has been already filled
                        continue
                    ## To check whether we have a winner or not
                    winner_check=game_obj.check_winner()
                    if winner_check:
                        break                        
                    game_obj.change_turn()
            case '2':
                ex=True
            case _:
                raise RuntimeError("Entered operation doesn't exist try again")
        if ex:
            break

if __name__=="__main__":
    main()