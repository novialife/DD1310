def intro():
    print(
        "Välkommen till spelet Chomp.\nInstruktioner: I spelet kommer du utmanas om att välja ett blocknummer från spelplanen.\nDet valda blocket och alla block under och till högre kommer att raderas.\nSpelet går ut på att undvika välja P, den spelare som väljer P förlorar och den andra spelare vinner")


def print_board_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()


def player_move(board):
    valid_choice = False
    while not valid_choice:
        choice = input("Ange blocknummer: ")
        valid_choice = player_choice_control(board, choice)
    return choice


def player_choice_control(board, play_choice):
    try:
        play_choice = int(play_choice)
    except ValueError:
        print("Skriv ett tal med siffor")
        return False

    board_check = play_choice in (item for sublist in board for item in sublist)
    if not board_check:
        print("Skriv ett värde som finns i listan din koskesh")
        return False
    else:
        return True


def update_board(board, play_choice):
    play_choice = int(play_choice)
    row = int(play_choice // 10)
    col = int(play_choice % 10)
    for i in range(row - 1, len(board)):
        for j in range(col - 1, len(board[i])):
            board[i][j] = ""


def main():
    intro()
    print()
    num_rows = int(input("Ange antal rader: "))
    num_cols = int(input("Ange antal kolumner: "))

    board = []
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_cols + 1):
            row.append(int(i * 10 + j))
        board.append(row)
    board[0][0] = "P"
    print(board)

    game_running = True
    turn = "spelar1"
    print_board_matrix(board)

    while game_running:
        if turn == "spelar1":
            print("Första spelarens tur")
            play_choice = player_move(board)
            update_board(board, play_choice)
            if board[0][1] == "" and board[1][0] == "":
                print_board_matrix(board)
                print()
                print("Spelar 2 vinner")
                game_running = False
            else:
                print_board_matrix(board)
                print()
                turn = "spelar2"

        else:
            print("Andra spelarens tur")
            play_choice = player_move(board)
            update_board(board, play_choice)
            if board[0][1] == "" and board[1][0] == "":
                print_board_matrix(board)
                print()
                print("Spelar 1 vinner")
                game_running = False
            else:
                print_board_matrix(board)
                print()
                turn = "spelar1"


main()
