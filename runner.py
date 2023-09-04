from helpers import minimax, winner, player, terminal, reset
from draw import draw, board  

"""
This file runs the actual game.
"""


while True:
    print("Enter if you would like to play as x or as o")
    play = input().lower().strip()
    if play not in ["x", "o"]:
        raise ValueError 
    
    while not terminal(board)[0]:
        draw(board) 
        if player(board) == play:
            while True:
                move = input("Enter your move (0-9)")
                try:
                    move = int(move)
                except ValueError:
                    print("Invalid Entry. Try Again.")
                    continue
                if move < 4:
                    pos = (0, move - 1)
                    if board[0][pos[1]] != " ":
                        print("This move isn't available")
                        continue
                    board[0][move - 1] = player(board)
                elif move < 7:
                    pos = (1, move - 4)
                    if board[1][pos[1]] != " ":
                        print("This move isn't available")
                        continue
                    board[1][move - 4] = player(board)
                else:
                    pos = (2, move - 7)
                    if board[2][pos[1]] != " ":
                        print("This move isn't available")
                        continue
                    board[2][move - 7] = play
                break  

        else:
            print("Thinking......")
            move = minimax(board)
            board[move[0]][move[1]] = player(board) 

    player_win = winner(board)
    if player_win == None:
        print("Tie Game!")
    else:
        draw(board)
        print(f"{player_win} wins!")
    board = reset()