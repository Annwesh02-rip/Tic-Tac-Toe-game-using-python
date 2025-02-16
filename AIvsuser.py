import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def ai_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells) if empty_cells else None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user = "X"
    ai = "O"
    
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board(board)
    
    for turn in range(9):
        if turn % 2 == 0:
            player = user
            print("Your turn! Enter your move (row and column: 0 1 2): ")
            while True:
                try:
                    row, col = map(int, input().split())
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("Cell occupied! Choose another.")
                except (ValueError, IndexError):
                    print("Invalid input! Enter row and column numbers between 0 and 2.")
        else:
            player = ai
            print("AI's turn...")
            row, col = ai_move(board)
            board[row][col] = player
        
        print_board(board)
        
        if check_winner(board, player):
            print(f"Player {player} wins!")
            return
        
        if is_draw(board):
            print("It's a draw!")
            return
    
if __name__ == "__main__":
    tic_tac_toe()
