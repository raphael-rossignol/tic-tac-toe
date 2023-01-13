board = [" ", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
Running = True
def create_board():
    print(board[1] + board[2] + board[3])
    print(board[4] + board[5] + board[6])
    print(board[7] + board[8] + board[9])


create_board()


def wincon():
    global Running
    if board[1] == board[2] == board[3] and "-" not in board[1:3] or \
            board[4] == board[5] == board[6] and "-" not in board[4:6] or \
            board[7] == board[8] == board[9] and "-" not in board[7:9] or \
            board[1] == board[4] == board[7] and "-" not in board[1:7:3] or \
            board[2] == board[5] == board[8] and "-" not in board[2:8:3] or \
            board[3] == board[6] == board[9] and "-" not in board[3:9:3] or \
            board[1] == board[5] == board[9] and "-" not in board[1:9:4] or \
            board[3] == board[5] == board[7] and "-" not in board[3:7:2]:
        while Running:
            Running = False
            print("GG !")
            pass
    else:
        pass


def draw():
    global Running
    if "-" not in board[1:]:
        while Running:
            Running = False
            print("DRAW")
            pass


def playerinput():
    while Running:
        ch = input("PlayerX: Choose a number between 1-9")
        a = int(ch)
        for i in range(len(board)):
            if i == a:
                if "-" in board[i]:
                    board[i] = "X"
                    create_board()
                    wincon()
                    draw()
                    return True
                else:
                    print("Choose another number")
                    create_board()
                    return False
            else:
                continue


playerinput()


def player2input():
    while Running:
        ch = input("Player0: Choose a number between 1-9")
        a = int(ch)
        for i in range(len(board)):
            if i == a:
                if "-" in board[i]:
                    board[i] = "O"
                    create_board()
                    wincon()
                    draw()
                    return True
                else:
                    print("Choose another number")
                    create_board()
                    return False
            else:
                continue


player2input()


def turn():
    while Running:
        if playerinput() == True:
            player2input()
        elif player2input() == True:
            playerinput()
        if playerinput() == False:
            playerinput()
        elif player2input() == False:
            player2input()
        else:
            continue


turn()
