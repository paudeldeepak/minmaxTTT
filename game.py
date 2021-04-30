from TTT import TTT
from minimaxAlg import Bot

if __name__ == "__main__":

    # welcome message
    print("---------------")
    print("--Tic Tac Toe--")
    print("---------------\n")
    
    continueGame = True

    while continueGame:
    # initialize the game 
        game = TTT()
        # create the game board
        game.createBoard()

        # keep the game looping until there is a win or tie
        while not game.checkTie() and not game.checkWin():

            print(game)
            print()
            print("---Currently playing:",game.turn+"---")

            validInput = False
                #check for valid input
            while not validInput:
                try:
                    legalMoves = game.legalMoves()
                    print(legalMoves)
                    if game.turn == "X":
                        xCoord = input("What is your X coordinate?: ")
                        yCoord = input("What is your Y coordinate?: ")
                    else:
                        gameBot = Bot(game.turn)
                        moves = gameBot.selectMoves(game)
                        xCoord = moves[0]
                        yCoord = moves[1]
                        print("Playing on X coordinate?:",xCoord)
                        print("Playing on Y coordinate?:",yCoord)
                    game.play(int(yCoord),int(xCoord))
                except:
                    print("\nInput not valid: Try Again\n")
                else:
                    validInput = True
            # change the player turn
            game.changeTurn()

        print(game)

        if game.checkWin():
            game.changeTurn()
            print("\nWinner: ",game.turn,"\n")
        else:
            print("\nTie\n")
        
        playAgain = input("Would you like to play again? [Y/N]: ")
        if playAgain.upper() != "Y":
            continueGame = False

    print("Thank You for playing")

    

