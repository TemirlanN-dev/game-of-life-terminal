class checkBorder:
    @staticmethod
    def topLeft(board, x, y):
        num = 0
        if x == 0 and y == 0:
            if board[x][y+1] == "■": # Right Side
                num+=1
            if board[x+1][y+1] == "■": # Bottom Right
                num+=1
            if board[x+1][y] == "■": # Bottom Middle
                num+=1
        return num

    @staticmethod
    def topBorder(board, x, y):
        num = 0
        if x == 0 and (len(board[x])-1) > y > 0:
            if board[x][y-1] == "■": # Left Side
                num+=1
            if board[x][y+1] == "■": # Right Side
                num+=1
            if board[x+1][y-1] == "■": # Bottom Left
                num+= 1
            if board[x+1][y] == "■": # Bottom Middle
                num+=1
            if board[x+1][y+1] == "■": # Bottom Right
                num+=1
        return num
    
    @staticmethod
    def topRight(board, x, y):
        num = 0
        if x == 0 and y == (len(board[x])-1):
            if board[x][y-1] == "■": # Left Side
                num+=1
            if board[x+1][y-1] == "■": # Bottom Left
                num+= 1
            if board[x+1][y] == "■": # Bottom Middle
                num+=1
        return num

    @staticmethod
    def rightBorder(board, x, y):
        num = 0
        if (len(board)-1) > x > 0 and y == (len(board[x])-1):
            if board[x-1][y] == "■": #Top Middle
                num+=1
            if board[x-1][y-1] == "■": #Top Left 
                num+=1
            if board[x][y-1] == "■": # Left Side
                num+=1
            if board[x+1][y-1] == "■": # Bottom Left
                num+= 1
            if board[x+1][y] == "■": # Bottom Middle
                num+=1
        return num
    
    @staticmethod
    def bottomRight(board, x, y):
        num = 0
        if x == (len(board)-1) and y == (len(board[x])-1):
            if board[x-1][y] == "■": #Top Middle
                num+=1
            if board[x-1][y-1] == "■": #Top Left 
                num+=1
            if board[x][y-1] == "■": # Left Side
                num+=1
        return num
    
    @staticmethod
    def bottomBorder(board, x, y):
        num = 0
        if x == (len(board)-1) and (len(board[x])-1) > y > 0:
            if board[x][y+1] == "■": # Right Side
                num+=1
            if board[x-1][y+1] == "■": #Top Right
                num+=1
            if board[x-1][y] == "■": #Top Middle
                num+=1
            if board[x-1][y-1] == "■": #Top Left 
                num+=1
            if board[x][y-1] == "■": # Left Side
                num+=1
        return num

    @staticmethod
    def bottomLeft(board, x, y):
        num = 0
        if x == (len(board)-1) and y == 0:
            if board[x-1][y] == "■": #Top Middle
                num+=1
            if board[x-1][y+1] == "■": #Top Right
                num+=1
            if board[x][y+1] == "■": # Right Side
                num+=1
        return num
    
    @staticmethod
    def leftBorder(board, x, y):
        num = 0
        if 0 < x < (len(board)-1) and y == 0:
            if board[x-1][y] == "■": #Top Middle
                num+=1
            if board[x-1][y+1] == "■": #Top Right
                num+=1
            if board[x][y+1] == "■": # Right Side
                num+=1
            if board[x+1][y+1] == "■": # Bottom Right
                num+=1
            if board[x+1][y] == "■": # Bottom Middle
                num+=1
        return num
    
    @staticmethod
    def center(board, x, y):
        num = 0
        if (len(board)-1)> x > 0 and (len(board[x])-1) > y > 0:
            # Covers the top of the cell
            if board[x-1][y-1] == "■": #Top Left 
                num+=1
            if board[x-1][y] == "■": #Top Middle
                num+=1
            if board[x-1][y+1] == "■": #Top Right
                num+=1

            # Covers the sides of the cell
            if board[x][y-1] == "■": # Left Side
                num+=1
            if board[x][y+1] == "■": # Right Side
                num+=1

            # Covers the bottome of the cell
            if board[x+1][y-1] == "■": # Bottom Left
                num+=1
            if board[x+1][y] == "■": # Bottom Middle
                num+=1
            if board[x+1][y+1] == "■": # Bottom Right
                num+=1
            
        return num