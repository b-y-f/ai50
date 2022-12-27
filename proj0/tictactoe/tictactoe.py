"""
Tic Tac Toe Player
"""

import math
from typing import List, Literal
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board) -> Literal:
    """
    Returns player who has the next turn on a board.
    The player function should take a board state as input, and return which player’s turn it is (either X or O).
        - In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
        - Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    countX = 0
    countO = 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1

    return X if countX == countO else O


def actions(board) -> set:
    """
    Returns set of all possible actions (i, j) available on the board.
    The actions function should return a set of all of the possible actions that can be taken on a given board.
        - Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2)
            and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
        - Possible moves are any cells on the board that do not already have an X or an O in them.
        - Any return value is acceptable if a terminal board is provided as input.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action) -> List:
    """
    Returns the board that results from making move (i, j) on the board.
    The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
        - If action is not a valid action for the board, your program should raise an exception.
        - The returned board state should be the board that would result from taking the original input board,
            and letting the player whose turn it is make their move at the cell indicated by the input action.
        - Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many
            different board states during its computation. This means that simply updating a cell in board itself is not
            a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    """
    i, j = action
    newBoard = copy.deepcopy(board)
    # if newBoard[i][j] == EMPTY:
    #     raise Exception
    if player(newBoard) == X:
        newBoard[i][j] = X
    else:
        newBoard[i][j] = O
    return newBoard


def winner(board) -> Literal:
    """
    Returns the winner of the game, if there is one.
    The winner function should accept a board as input, and return the winner of the board if there is one.
        - If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
        - One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
        - You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
        - If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    """
    winner = None
    # Hertizotal test
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            winner = board[i][0]
    # Vertical test
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            winner = board[0][i]
    # Diagnal test
    if (board[1][1] == board[0][0] == board[2][2]) or (
        board[1][1] == board[0][2] == board[2][0]
    ):
        winner = board[1][1]
    return winner


def terminal(board) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board) -> tuple:
    """
    Returns the optimal action for the current player on the board.
    """

    def calcScore(action, imagineBoard) -> int:
        # 1. make basic minmax without prune, just make sure everything works
        # TODO then try to use alpha-beta prune technology to optimzed the AI
        if terminal(imagineBoard):
            return utility(board)
        if player(imagineBoard) == X:
            XScore = float("-inf")
            afterAction = result(imagineBoard, action)
            for action in actions(afterAction):
                score = calcScore(action, afterAction)
                XScore = max(XScore, score)
            return XScore
        else:
            OScore = float("inf")
            afterAction = result(imagineBoard, action)
            for action in actions(afterAction):
                score = calcScore(action, afterAction)
                OScore = min(OScore, score)
            return OScore

    currBestMove = None
    bestScore = float("-inf") if player(board) == X else float("inf")
    for action in actions(board):
        if calcScore(action, board) != bestScore:
            bestScore = calcScore(action, board)
            currBestMove = action
    return currBestMove
