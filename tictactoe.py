"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    
    count=0
    if board == initial_state():
        return X
    for row in board:
        for x in row:
            if x != EMPTY:
                count =  count + 1
    if terminal(board):
        return 1
    if count%2 == 0:
        return X
    else:
        return O
"""
    if board == initial_state():
        return X
    xcount , ocount = 0 , 0
    for row in board:
        for i in row:
            if i == X:
                xcount += 1
            elif i == O:
                ocount += 1
    if terminal(board):
        return 1
    elif xcount > ocount:
        return O
    elif ocount == xcount:
        return X
    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return 1
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions
    
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyBoard = copy.deepcopy(board)
    copyBoard[action[0]][action[1]] = player(board)

    return copyBoard
    
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #Row Check
    for row in board:
        if row[0]==row[1]==row[2]:
            return row[0]

    #Column Check
    row,col = 0,0
    for i in range(3):
        if board[row][col + i] == board[row+1][col + i] == board[row+2][col + i]:
            return board[row][col + i]

    #Major Diagonal Check
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    #Minor Diagonal Check
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        count = 0
        for row in board:
            for item in row:
                if item == EMPTY:
                    count = count + 1
        if count == 0:
            return True
        else:
            return False
                    
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win_player = winner(board)
    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0
    #raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        value = -math.inf
        for action in actions(board):
            value = max(value, min_value(result(board,action)))
            if value == 1:
                break
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    else:
        value = math.inf
        for action in actions(board):
            value = min(value, max_value(result(board,action)))
            if value == -1:
                break
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value = v = -math.inf
            move = ()
            for action in actions(board):
                v = max(v, min_value(result(board,action)))
                if value < v:
                    value = v
                    move = action
                    if value == 1:
                        break
            return move
        else:
            value = v = math.inf
            move = ()
            for action in actions(board):
                v = min(v, max_value(result(board,action)))
                if value > v:
                    value = v
                    move = action
                    if value == -1:
                        break
            return move
    #raise NotImplementedError
