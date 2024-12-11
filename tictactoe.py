from sys import *
from collections import *
from math import *

def tictactoeWinner(board):
    def check_winner(board):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '_':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != '_':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != '_':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '_':
            return board[0][2]
        return None

    def is_draw(board):
        # Check if the board is full and no winner
        return all(cell != '_' for row in board for cell in row)

    def minimax(board, is_maximizing):
        winner = check_winner(board)
        if winner == 'X':  # N wins
            return 1
        if winner == 'O':  # Opp wins
            return -1
        if is_draw(board):  # Draw
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = 'X'
                        score = minimax(board, False)
                        board[i][j] = '_'
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        board[i][j] = 'O'
                        score = minimax(board, True)
                        board[i][j] = '_'
                        best_score = min(best_score, score)
            return best_score

    def find_best_move(board):
        best_score = -float('inf')
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = '_'
                    if score > best_score or (score == best_score and (i < best_move[0] or (i == best_move[0] and j < best_move[1]))):
                        best_score = score
                        best_move = (i, j)
        return best_score, best_move
    # Get the best score and best move
    score, move = find_best_move(board)
    return (score, move[0] + 1, move[1] + 1) 
