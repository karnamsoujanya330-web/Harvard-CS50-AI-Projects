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
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count == o_count:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    
    new_board = copy.deepcopy(board)
    
    i, j = action
    
    current_player = player(board)
    
    new_board[i][j] = current_player
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check rows
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        
    #Check columns
    for j in range(3):
        if board[0][j] != EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    #Check first diagonal
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    #Check second diagonal
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    #No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    if len(actions(board)) == 0:
        return True
    
    return False
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    
    if game_winner == X:
        return 1
    
    elif game_winner == 0:
        return -1
    
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
      return None
  
    current_player = player(board)
  
    if current_player == X:
        
        best_score = -math.inf
        best_action = None
        
      
        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board)
      
            if score > best_score:
                best_score = score
                best_action = action
        
        return best_action
    
    else:
        
         best_score = math.inf
         best_action = None
        
         for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board)
              
            if score < best_score:
                  best_score = score
                  best_action = action
                  
    return best_action

def max_value(board):

    if terminal(board):
        return utility(board)

    value = -math.inf

    for action in actions(board):
        value = max(
            value,
            min_value(result(board, action))
        )

    return value


def min_value(board):

    if terminal(board):
        return utility(board)

    value = math.inf

    for action in actions(board):
        value = min(
            value,
            max_value(result(board, action))
        )

    return value