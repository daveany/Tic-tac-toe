import random

class TicTacToe:
    def __init__(self):
        # your original variables (cleaned)
        self.board = ["-"] * 9
        self.currentPlayer = "X"
        self.winner = None
        self.gameRunning = True

    def printBoard(self):
        print()
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("---------")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("---------")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])
        print()

    def playerInput(self):
        while True:
            try:
                inp = int(input("Enter a number (1-9): "))
                if 1 <= inp <= 9 and self.board[inp-1] == "-":
                    self.board[inp-1] = "X"
                    break
                else:
                    print("Invalid move, try again.")
            except:
                print("Enter a valid number.")

    def checkHorizontal(self):
        if self.board[0] == self.board[1] == self.board[2] != "-":
            return self.board[0]
        if self.board[3] == self.board[4] == self.board[5] != "-":
            return self.board[3]
        if self.board[6] == self.board[7] == self.board[8] != "-":
            return self.board[6]
        return None

    def checkRow(self):
        if self.board[0] == self.board[3] == self.board[6] != "-":
            return self.board[0]
        if self.board[1] == self.board[4] == self.board[7] != "-":
            return self.board[1]
        if self.board[2] == self.board[5] == self.board[8] != "-":
            return self.board[2]
        return None

    def checkDiag(self):
        if self.board[0] == self.board[4] == self.board[8] != "-":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != "-":
            return self.board[2]
        return None

    def checkWinner(self):
        return self.checkHorizontal() or self.checkRow() or self.checkDiag()

    def isTie(self):
        return "-" not in self.board

    def switchPlayer(self):
        self.currentPlayer = "O" if self.currentPlayer == "X" else "X"

    def randomAI(self):
        while True:
            pos = random.randint(0, 8)
            if self.board[pos] == "-":
                return pos

    def minimax(self, board, isMaximizing):
        winner = self.evaluate(board)

        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif "-" not in board:
            return 0

        if isMaximizing:
            bestScore = -float("inf")
            for i in range(9):
                if board[i] == "-":
                    board[i] = "O"
                    score = self.minimax(board, False)
                    board[i] = "-"
                    bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float("inf")
            for i in range(9):
                if board[i] == "-":
                    board[i] = "X"
                    score = self.minimax(board, True)
                    board[i] = "-"
                    bestScore = min(score, bestScore)
            return bestScore

    def evaluate(self, board):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for a,b,c in combos:
            if board[a] == board[b] == board[c] != "-":
                return board[a]
        return None

    def bestMove(self):
        bestScore = -float("inf")
        move = 0

        for i in range(9):
            if self.board[i] == "-":
                self.board[i] = "O"
                score = self.minimax(self.board, False)
                self.board[i] = "-"
                if score > bestScore:
                    bestScore = score
                    move = i
        return move

    # choose difficulty
    def computerMove(self, difficulty="hard"):
        if difficulty == "easy":
            return self.randomAI()
        else:
            return self.bestMove()

    # main game loop (your original loop improved)
    def run(self):
        difficulty = input("Choose difficulty (easy/hard): ").lower()

        while self.gameRunning:
            self.printBoard()

            if self.currentPlayer == "X":
                self.playerInput()
            else:
                move = self.computerMove(difficulty)
                self.board[move] = "O"

            winner = self.checkWinner()

            if winner:
                self.printBoard()
                print(f"The winner is {winner}!")
                break

            if self.isTie():
                self.printBoard()
                print("It is a tie!")
                break

            self.switchPlayer()


game = TicTacToe()
game.run()