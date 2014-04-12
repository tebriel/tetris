#!/usr/bin/env python

"""
Written by Chris Moultrie <chris@moultrie.org> @tebriel
Available on Github at https://github.com/tebriel/tetris
This was a lot of fun, thanks.

Usage: cat <filename> | python tetris-sticky.py
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
                    row_calc = len(board) - row - 1
                    board[row_calc][column] = 'Y'
                    marked_a_piece = True
            elif block == '.':
                row_empty = row_empty and True
        if row_empty and not found_emptiness:
            found_emptiness = True
    return marked_a_piece

def can_move_piece_down(board):
    """Determine if the piece can move downwards"""
    # Pretend it's a graph, bottom left is (0,0)
    backwards_board = reversed(board)
    cant_go_no_further_down = False
    found_to_move = False
    for row, line in enumerate(backwards_board):
        if cant_go_no_further_down:
            break

        for column, block in enumerate(line):
            # These aren't the blocks you're looking for
            if block != 'Y':
                continue
            found_to_move = True
            # We've hit rock bottom
            row_calc = len(board) - row
            if (row == 0) or (board[row_calc][column] == 'X'):
                cant_go_no_further_down = True
                break
    # I DON'T NEED YOUR JUDGEMENT ON MY VARIABLE NAMES
    # TODO: This is crazy confusing, at some point I might actually need to
    #   know what this does...
    return not cant_go_no_further_down and found_to_move

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
            new_board[row] = ['.' for i in range(0,len(line))]
            num_cleared += 1

    return new_board, num_cleared

def stabilize_base(board):
    """Remove empty lines from the base, to give us a base that isn't expecting
    to fall"""
    new_board = duplicate_board(board)
    backwards_board = reversed(board)
    for row, line in enumerate(backwards_board):
        line_is_empty = True
        for column, block in enumerate(line):
            line_is_empty = line_is_empty and block == '.'
        if line_is_empty:
            row_calc = len(board) - 1 - row
            del new_board[row_calc]
            new_board.insert(0, ['.' for x in range(0,len(line))])
        else:
            break
    return new_board

def debug_board(board):
    """ Print out the board so that we can see what the heck is going on"""
    for index, line in enumerate(board):
        print index + 1, line


if __name__ == "__main__":
    tetris_board = read_in_board(sys.stdin.read())
    mark_for_moving(tetris_board)
    total_cleared = 0
    num_cleared = 1
    while num_cleared != 0:
        while can_move_piece_down(tetris_board):
            tetris_board = move_piece_downward(tetris_board)
            #debug_board(tetris_board)
        tetris_board, num_cleared = clear_out_lines(tetris_board)
        total_cleared += num_cleared
        tetris_board = stabilize_base(tetris_board)
        # Need to re-stabilize base before re-marking
        # debug_board(tetris_board)
        mark_for_moving(tetris_board)

    print total_cleared
    # debug_board(tetris_board)
