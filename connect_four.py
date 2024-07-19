def initialize_board(cols, rows):
    return[["-" for i in range(rows)] for j in range(cols)]

def print_board(board):
    for row in list(reversed(board)):     # row ["-", "-", "-"]
        for col in row:
            print(col, end=" ")
        print()
    return board


def insert_chip(board, col, chip_type): 
    for num in range(len(board)):
        if board[num][col] == "-":
            board[num][col] = chip_type
            return num


def board_is_full(board):
    for row in board:
        for chip in row:
            if chip == "-":
                return False
    return True


def check_if_winner(board, col, row, chip_type): #mimics consecutive fours function from 2B Pre work
    #check all rows
    count = 0
    for i in range(len(board[0])):
        if board[row][i] == chip_type:
            count = count + 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for i in range(len(board[i])):
        if board[i][col] == chip_type:
            count = count + 1
            if count == 4:
                return True
        else:
            count = 0

    return False



if __name__ == "__main__":
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be?"))
    board = initialize_board(height, length)
    print_board(board)

    print("")
    print("Player 1: x")
    print("Player 2: o")
    print("")

    player = 1
    chip = "x"
    game_continue = True
    #player_choice = input("Which column would you like to choose?")


    while game_continue:
        print("")
        #asks player 1 or 2 what column they want
        player_choice = input(f"Player {player}: Which column would you like to choose?")
        col = int(player_choice)

        insert = insert_chip(board, col, chip)
        print_board(board)

        if check_if_winner(board, col, insert, chip):
            print(f"\nPlayer {player} won the game!")
            game_continue = False
        else:
            if board_is_full(board):
                print("\nDraw. Nobody wins.")
                game_continue = False

        #alternating players and chips
        if player == 1:
            player = 2
        else:
            player = 1

        if chip == "o":
            chip = "x"
        else:
            chip = "o"






