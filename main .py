board = [" " for _ in range(9)]
def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()
def check_win (player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)
def is_draw():
    return all(cell != " " for cell in board)
def play_game():
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print_board()
    while True:
        move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        if board[move] != " ":
            print("That spot is taken. Try again.")
            continue
        board[move] = current_player
        print_board()
        if check_win(current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw():
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

play_game()