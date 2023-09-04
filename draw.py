
# This file takes care of drawing a tic-tac-toe board in the console.

board = [[" " for _ in range(3)], [" " for _ in range(3)], [" " for _ in range(3)]]

def draw(board):
    """
    This function takes in a board variable which is a two dimensional array. The possible values can be "x", "o" or " ".
    There is no return value.
    """

    print("     |     |     ")
    print("  " + board[0][0] + "  |  " + board[0][1] + "  |  " + board[0][2] + "  ")
    print("     |     |     ")
    print("_________________")
    print("     |     |     ")
    print("  " + board[1][0] + "  |  " + board[1][1] + "  |  " + board[1][2] + "  ")
    print("     |     |     ")
    print("_________________")
    print("     |     |     ")
    print("  " + board[2][0] + "  |  " + board[2][1] + "  |  " + board[2][2] + "  ")
    print("     |     |     ")
    print("\n\n")
    
