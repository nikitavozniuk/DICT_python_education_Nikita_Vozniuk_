in_range = [int(i) for i in range(1, 4)]

def tic_tac_toe():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    end = False

    def draw():
        print('---------')
        print('| {} {} {} |'.format(board[0][0], board[0][1], board[0][2]))
        print('| {} {} {} |'.format(board[1][0], board[1][1], board[1][2]))
        print('| {} {} {} |'.format(board[2][0], board[2][1], board[2][2]))
        print('---------')
        print()

    def p1():
        row, col = choose_number()
        if board[row][col] == "X" or board[row][col] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[row][col] = "X"

    def p2():
        row, col = choose_number()
        if board[row][col] == "X" or board[row][col] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[row][col] = "O"

    def choose_number():
        while True:
            try:
                row, col = input().split(' ')
                row = int(row)
                col = int(col)
            except ValueError:
                print('You should enter numbers!')
                continue
            if row and col not in in_range:
                print('Coordinates should be from 1 to 3!')
            return row-1, col-1

    def check_board():
        count = 0
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True

        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][1] == "O" and board[1][1] == "X" and board[2][1] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True
        if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
            print("Player 1 Wins!\n")
            print("Congratulations!\n")
            return True

        for a in range(3):
            for b in range(3):
                if board[a][b] == "X" or board[a][b] == "O":
                    count += 1
                if count == 9:
                    print("The game ends in a Tie\n")
                    return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 1 choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        p2()
        print()

    if input("Play again (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()