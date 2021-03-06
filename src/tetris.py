#!/usr/bin/env python

"""
Written by Chris Moultrie <chris@moultrie.org> @tebriel
Available on Github at https://github.com/tebriel/tetris
This was a lot of fun, thanks.

Usage: cat <filename> | python tetris.py
"""

import sys

def mark_for_moving(board):
    """Runs up the board from the bottom, finding a floating piece and marking
    it to be moved down one square, returns True if there's a piece to move"""
    marked_a_piece = False
    found_piece = False
    found_emptiness = False
    for row, line in enumerate(reversed(board)):
        row_empty = True
        for column, block in enumerate(line):
            if block == 'X':
                if not found_emptiness:
                    row_empty = False
                    break
                else:
                    # Doesn't work because it's by value not by reference
                    row_calc = len(board) - row - 1
                    board[row_calc][column] = 'Y'
                    marked_a_piece = True
            elif block == '.':
                row_empty = row_empty and True
        if row_empty and not found_emptiness:
            found_emptiness = True
    return marked_a_piece

def can_move_piece_down(board):
    # Pretend it's a graph, bottom left is (0,0)
    backwards_board = reversed(board)
    cant_go_no_further_down = False
    for row, line in enumerate(backwards_board):
        if cant_go_no_further_down:
            break

        for column, block in enumerate(line):
            # These aren't the blocks you're looking for
            if block != 'Y':
                continue
            # We've hit rock bottom
            row_calc = len(board) - row
            if (row == 0) or (board[row_calc][column] == 'X'):
                cant_go_no_further_down = True
                break
    return not cant_go_no_further_down

def read_in_board(board_input):
    """Builds the 2D list with all the board's blocks"""
    board = []
    board_lines = board_input.split('\n')
    for line in board_lines:
        if line == '':
            continue
        board.append(list(line))

    return board

def duplicate_board(board):
    """Make a copy so we can update"""
    new_board = []
    for line in board:
        new_board.append([block for block in line])
    return new_board


def move_piece_downward(board):
    """Move our piece down one row, return a new board with our moved stuff"""
    new_board = duplicate_board(board)
    backwards_board = reversed(board)
    for row, line in enumerate(backwards_board):
        for column, block in enumerate(line):
            if block == 'Y':
                row_calc = len(board) - row
                new_board[row_calc][column] = 'Y'
                new_board[row_calc-1][column] = '.'
    return new_board

def clear_out_lines(board):
    """Remove our solid lines"""
    new_board = duplicate_board(board)
    num_cleared = 0
    for row, line in enumerate(board):
        is_all_x = True
        for column, block in enumerate(line):
            is_all_x = is_all_x and block in ['X','Y']
        if is_all_x:
            del new_board[row]
            new_board.insert(0, ['.' for i in range(0,len(line))])
            num_cleared += 1

    return new_board, num_cleared

def debug_board(board):
    for index, line in enumerate(board):
        print index + 1, line


if __name__ == "__main__":
    tetris_board = read_in_board(sys.stdin.read())
    mark_for_moving(tetris_board)
    while can_move_piece_down(tetris_board):
        tetris_board = move_piece_downward(tetris_board)
        #debug_board(tetris_board)
    tetris_board, num_cleared = clear_out_lines(tetris_board)

    print num_cleared
