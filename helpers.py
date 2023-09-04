from draw import draw, board
from copy import deepcopy


def player(board):
    """
    This function takes in the board variable and returns which player's turn it is. The return value is either "o" or "x".
    """
    # Count how many places are not blank.
    count = 0 
    for li in board:
        for item in li:
            if item != " ":
                count += 1 

    if count % 2 == 0:
        return "o"
    else:
        return "x"


def actions(board):
    """
    This function takes in the board variable and returns all possible moves in a list of tuples, which represent positions on the board.
    If there is no open positions on the board, the function returns None.
    """
    # Loop through the positions, if they are blank add a tuple with the positions to the moves list.
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                moves.append((r, c,))

    if len(moves) != 0:
        return moves
    return None


def terminal(board):
    """
    This function will return a tuple. The first is True if the board is terminal (Meaning that it is either a tie, or one player has won.), Else it will return False. The second item is who won, o or x or None if either the game isn't terminal or it is a tie.
    """
    # Check if any player won 
    # Check horizontal
    is_terminal = False
    for r in board:
        if r[0] != " " and r[0] == r[1] and r[1] == r[2]:
            is_terminal = True
            pos = r[0] 
            break 
    if is_terminal == True:
        return (True, pos)
    # Check Vertical 
    for i in range(3):
        if board[0][i] != " " and board[0][i] == board[1][i]  and board[1][i] == board[2][i]:
            is_terminal = True 
            pos = i
            break 
    if is_terminal == True:
        return (True, board[0][pos])
    # Check diagnol 
    if board[0][0] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        is_terminal = True 
        pos = board[0][0]
    elif board[0][2] != " " and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        is_terminal = True 
        pos = board[0][2]
    if is_terminal:
        return (True, pos)
    
    
    # Check if the board is full 
    is_terminal = True
    for i in board:
        if " " in i:
            is_terminal = False 
            break

    return (is_terminal, None)


def winner(board):
    """
    This function returns the winner (If there is one). The return Value is x or o or None (If the board isn't terminal or if it is a tie).
    """
    data = terminal(board) 
    return data[1]


def utility(board):
    """
    This function accepts a board as input and returns the utility of the board. This function can only be called on a terminal board.
    """
    winner_data = winner(board)
    if winner_data == None:
        return 0
    elif winner_data == "o":
        return 1 
    else:
        return -1 


def result(board, action):
    """
    This function accepts a board and an action (as a tuple representing the position) and returns a copy of the board with that action applied. It doesn't change the original board.
    """ 
    copy_board = deepcopy(board)
    if copy_board[action[0]][action[1]] != " ":
        raise ValueError
    copy_board[action[0]][action[1]] = player(copy_board)
    return copy_board


def minimax(board):
    """
    This function takes in a board and returns the best move possible for the current player.
    """
    moves = actions(board)
    utils = {}
    if player(board) == "o":
        for action in moves:
            util = min_value(result(board, action))
            if util == 1:
                return action 
            else:
                utils[util] = action  

        if 0 in utils:
            return utils[0]
        else:
            return utils[-1]
    else:
        for action in moves:
            util = max_value(result(board, action))
            if util == -1:
                return action 
            else:
                utils[util] = action  

        if 0 in utils:
            return utils[0]
        else:
            return utils[1]


def max_value(board):
    v = -100 

    if terminal(board)[0]:
        return utility(board)
    moves = actions(board)
    for action in moves:
        state = result(board, action)
        v = max(v, min_value(state))
    return v

def min_value(board):
    v = 100 
    if terminal(board)[0]:
        return utility(board)
    moves = actions(board)
    for action in moves:
        state = result(board, action)
        v = min(v, max_value(state))
    return v 


def reset():
    """
    This function just returns a blank board
    """
    return [[" " for _ in range(3)], [" " for _ in range(3)], [" " for _ in range(3)]]



    