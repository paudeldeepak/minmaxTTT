class TTT:
    """
    A class to represent TTT
    ...
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the TTT object.

        Parameters
        ----------
        N/A
        """
        self.size = 3
        self.board = []
        self.boardCount = 0
        self.playerX = "X"
        self.playerO = "O"
        # player x always gets to go first
        self.turn = self.playerX

    def createBoard(self):
        """
        create the TTT Board
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        # for each row index
        for rowIndex in range(self.size):
            row = []
            #for each column index
            for columnIndex in range(self.size):
                # create a empty board
                row.append(None)
            # append row to the baord
            self.board.append(row)

    def changeTurn(self):
        """
        Change the turn from one player to the other player
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        # check the current turn and change it 
        if self.turn == self.playerX:
            self.turn = self.playerO
        else:
            self.turn = self.playerX

    def play(self,row,col):
        """
        play at the specified row, column position from the board
        Parameters
        ----------
        row: int
            the row postion of the board
        col: int
            the column postion of the board
        Returns
        -------
        None
        """
        # can only play if there is no player in the baord
        if not self.checkEmptySpace(row,col):
            raise Exception(print("\ncan not play at {}, {}, its alredy filled".format(row, col)))
        else:
            self.board[row][col] = self.turn
            self.boardCount += 1
        
    def checkTie(self):
        """
        check if game is tied
        Parameters
        ----------
        None
        Returns
        -------
        True if tie, false otherwise
        """
        # return true when baord is full
        return self.boardCount == 9
    
    def checkWin(self):
        """
        check if a player has won
        Parameters
        ----------
        None
        Returns
        -------
        True if tie, false otherwise
        """
        # check for 3 types of win
        rowWin = self.checkRowWin()
        colWin = self.checkColWin()
        diagWin = self.checkDiagWin()

        win = rowWin or colWin or diagWin

        return win

    def checkRowWin(self):
        """
        check if row has all the same player 
        Parameters
        ----------
        None
        Returns
        -------
        True if same player, false otherwise
        """
        rowWin = False

        # iterate through each row
        for row in self.board:
            # get one value 
            player = row[0]
            # if there is a player
            if player != None:
                # check if the player match match
                if row[1] == player and row[2] == player:
                    rowWin = True
        return rowWin
        
    def checkColWin(self):
        """
        check if column has all the same player 
        Parameters
        ----------
        None
        Returns
        -------
        True if same player, false otherwise
        """
        colWin = False

        # iterate through the board to find the columns
        for column_index in range(self.size): 
            column = [] 
            for row in self.board: # iterate through the board to get rows
                column.append(row[column_index])
            player = column[0]
            # if there is a player
            if player != None:
                # check if the player match
                if column[1] == player and column[2] == player:
                    colWin = True
        return colWin

    def checkDiagWin(self):
        """
        check if diagonal has all the same player 
        Parameters
        ----------
        None
        Returns
        -------
        True if same player, false otherwise
        """
        diagWin = False

        diagonals = [[], []]
        for index in range(self.size):
            # get the diagonal values
            diagonals[0].append(self.board[index][index]) 
            diagonals[1].append(self.board[index][self.size-1-index])

        for diagonal in diagonals:
            player = diagonal[0]
            # if there is a player
            if player != None:
                # check if the player match
                if diagonal[1] == player and diagonal[2] == player:
                    diagWin = True
        return diagWin

    def checkEmptySpace(self,row,col):
        """
        check if the row and col of board is empty 
        Parameters
        ----------
        row: int
            the row postion of the board
        col: int
            the column postion of the board
        Returns
        -------
        True if empty, false otherwise
        """

        return self.board[row][col] == None

    def legalMoves(self):
        """
        find all the legalMoves
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        legalMoves = []
        # get row index
        for row in range(self.size):
            # get col index
            for col in range(self.size):
                # check if empty
                if self.checkEmptySpace(row,col):
                    legalMoves.append([row,col])
        return legalMoves

    def getBoard(self):
        """
        return the current state of the board
        Parameters
        ----------
        None
        Returns
        -------
        board
        """
        return self.board
        
    def __str__(self):
        """
        string representation of the game
        """
        boardAsString =""
        # iterate to get values on the side
        boardAsString += "  -----------\n"
        for rowIndex in range(self.size):
            boardAsString += ("{:<1d}".format(rowIndex))
            # iterate to get index to find the value of the list inside of list
            for columnIndex in range(self.size):
                if self.board[rowIndex][columnIndex] == None:
                    boardAsString += ("    ")
                else:
                    boardAsString += (" |{:<1s}|".format(str((self.board[rowIndex][columnIndex]))))
            boardAsString += "\n"
        boardAsString += "  -----------\n"
        # iterate to get values to on the bottom
        for index in range(self.size):
            boardAsString += ("   {}".format(index))
        return boardAsString

if __name__ == "__main__":
    pass