won = False
count = 0
board_piece = [["   ", "   ", "   "],
               ["   ", "   ", "   "],
               ["   ", "   ", "   "], ]


def start():
    name = input("Enter you name: ")
    print(f"GAME IS ABOUT TO START {name.upper()}")


def board():
    print("--------------")
    for row in range(3):
        print("|", end='')
        for col in range(3):
            print(board_piece[row][col], end='')
            print("|", end='')
        print()
        print("--------------")


def move(player):
    pos = int(input("Enter the number from 1 to 9: ")) - 1
    while board_piece[2-pos//3][pos % 3] != "   ":
        pos = int(input("Error can not over ride /n number(1-9): ")) - 1
    board_piece[2-pos//3][pos % 3] = player


def check():
    # check rows
    for row in range(3):
        if board_piece[row][0] == board_piece[row][1] and board_piece[row][2] == board_piece[row][1] and board_piece[row][1] != '   ':
            return board_piece[row][0]
    # check cols
    for col in range(3):
        if board_piece[0][col] == board_piece[1][col] and board_piece[2][col] == board_piece[1][col] and board_piece[1][col] != '   ':
            return board_piece[0][col]
    # check diagonals
        if board_piece[0][0] == board_piece[1][1] and board_piece[2][2] == board_piece[1][1] and board_piece[1][1] != '   ':
            return board_piece[0][0]
        if board_piece[0][2] == board_piece[1][1] and board_piece[2][0] == board_piece[1][1] and board_piece[1][1] != '   ':
            return board_piece[0][2]


start()
while won != True:
    count += 1
    board()

    if count % 2 == 0:
        move(" x ")
    else:
        move(" o ")

    who_won = check()
    if(who_won != None):
        board()
        print(who_won, end='')
        print(" won!")
        won = True