'''
Conway's Game of Life with set borders, using python.

- '■' are alive cells.
- '.' are dead cells.

The Four Rules:
1. Any live cell with fewer than two live neighbors dies, by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, by reproduction.
'''
import random
import curses
from checkBorder import checkBorder

def dead_board(width, height): # Creates a board full of 0s based on width and height
    board = []
    for i in range(height):
        board.append([0]*width)
    return board

def random_board(board): 
    # updates a board to be full of either 0s or 1s
    for i in range(len(board)):
        for n in range(len(board[i])):
            random_Num = random.randint(0, 1)
            board[i][n] = random_Num
    
    return board

def next_board_state(board):
    board2 = dead_board(30, 30) # A copy that will update based on the 0s and 1s in the inital board
    
    #Loop through each cell
    for x in range(len(board)): 
        for y in range(len(board[x])):
            if board[x][y] == "■": # Check if the cell is alive
                count = num_neighbours(board, x, y) # Count how many neighbours around the point
            
                if count == 0 or count == 1: # Underpopulated so dies
                    board2[x][y] = 0
                elif count == 2 or count == 3: # Perfect conditions so lives
                    board2[x][y] = 1
                elif count > 3: # Overpopulated so dies
                    board2[x][y] = 0

            elif board[x][y] == ".": # Check if the cell is dead
                count = num_neighbours(board, x, y) # Count the number of its neighbours
                if count == 3: # Turns alive if exactly 3 
                    board2[x][y] = 1
    
    return board2

def num_neighbours(board, x, y): # x and y are indexes
    num = 0

    # Checks if it's top left corner
    num+=checkBorder.topLeft(board, x, y)

    # Checks if it's on the top border
    num+=checkBorder.topBorder(board, x, y)
    
    # Checks if it's on the top right corner
    num+=checkBorder.topRight(board, x, y)
    
    # Checks if it's on the right side border
    num+=checkBorder.rightBorder(board, x, y)
    
    # Checks if it's on the bottom right corner
    num+=checkBorder.bottomRight(board, x, y)
    
    # Checks if it's on the bottom border
    num+=checkBorder.bottomBorder(board, x, y)
    
    # Checks if it's on the bottom left corner
    num+=checkBorder.bottomLeft(board, x, y)
    
    # Checks if it's on the left side border
    num+=checkBorder.leftBorder(board, x, y)
    
    # If not on the border then checks all spaces around the cell
    num+=checkBorder.center(board, x, y)
    
    return num

def pretty_board(board):
    # To make it easier to see whats alive or dead
    for i in range(len(board)):
        for n in range(len(board[i])):
            if board[i][n] == 1:
                board[i][n] = "■"
            else:
                board[i][n] = "."

def main(stdscr):
    board = random_board(dead_board(30, 30)) # Creates a board full of random placements of 1s and 0s
    pretty_board(board) # Replaces those ones and zeroes with a square and a dot
    tempBoard = next_board_state(board) # Acts as a temporary board that will constatly change and be used to display the new screen

    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1) # So the system can run without having need an input
    stdscr.timeout(100) # Refreshes every 100 milliseconds so no screen tearing visible
    stdscr.clear() # Clears the screen

    while True:
        board2 = tempBoard 
        pretty_board(board2)

        max_y, max_x = stdscr.getmaxyx() # gets size of the terminal window
        start_row = 0
        
        # Displays the cells within the screen size
        for i in range(min(len(board2), max_y)):
            for j, cell in enumerate(board2[start_row + i]):
                stdscr.addstr(i, j, cell) # i and j are positions in which the cell will be displayed at

        stdscr.refresh() # Updates the terminal

        tempBoard = next_board_state(board2) # Now the temporary board will equal to the next state of the board
        
        key = stdscr.getch() # Checks if a key is pressed
        
        if key == 32:
            break  # Quit when space bar is pressed

curses.wrapper(main)


    
 

    


        