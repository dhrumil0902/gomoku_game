def is_empty(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != " " :
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    count = 0
    start_x = x_end - (length-1)*d_x
    start_y = y_end - (length-1)*d_y
    if (d_y == 1 and d_x == -1) or(d_y == 1 and d_x == 1):
        if start_x != 0 and start_y != 0 and start_y != 7 and start_x!=7:
            if board[start_y - d_y][start_x - d_x] == ' ':
                count+=1
        if x_end != 0 and y_end != 0 and y_end!= 7 and x_end != 7:
            if board[y_end + d_y][x_end + d_x] == ' ':
                count+=1
        if count == 0:
            return "CLOSED"
        if count == 1:
            return "SEMIOPEN"
        if count == 2:
            return "OPEN"
    if d_y == 1 and d_x == 0:
        if start_y != 0:
            if board[start_y - d_y][start_x - d_x] == ' ':
                count+=1
        if y_end != 7:
            if board[y_end + d_y][x_end + d_x] == ' ':
                count+=1
        if count == 0:
            return "CLOSED"
        if count == 1:
            return "SEMIOPEN"
        if count == 2:
            return "OPEN"
    if d_y == 0 and d_x == 1:
        if start_x != 0:
            if board[start_y - d_y][start_x - d_x] == ' ':
                count+=1
        if x_end != 7:
            if board[y_end + d_y][x_end + d_x] == ' ':
                count+=1
        if count == 0:
            return "CLOSED"
        if count == 1:
            return "SEMIOPEN"
        if count == 2:
            return "OPEN"


def range_row(y_start,x_start,d_y,d_x):
    if d_y == 0 and d_x ==1:
        return abs(x_start -8)
    if d_y == 1 and d_x == 0:
        return abs(y_start - 8)
    if d_y == 1 and d_x == -1:
        return x_start - y_start + 1
    if d_x == 1 and d_y == 1:
        return abs(x_start -8) - y_start

def detects_row_win(board, col, y_start, x_start, length, d_y, d_x):
    run = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    closed_count = 0
    length_start = 0
    j = y_start - d_y
    k = x_start - d_x
    rows = range_row(y_start,x_start,d_y,d_x)
    for i in range(rows):
        j += d_y
        k += d_x
        if board[j][k] == col and run == 0:
            first_y = j
            first_x = k
            run = 1
            length_start = i
        if run == 1 and i == rows-1 and board[j][k]== col:
            y_end = j
            x_end = k
            length_2 = i- length_start +1
            run = 0
            if length_2 == length:
                output = is_bounded(board, y_end, x_end, length_2, d_y, d_x)
                if output == "CLOSED":
                    closed_count +=1
                if output == "OPEN":
                    open_seq_count +=1
                if output == "SEMIOPEN":
                    semi_open_seq_count += 1
        if board[j][k]!= col and run==1:
            y_end = j - d_y
            x_end = k - d_x
            length_2 = i - length_start
            run = 0
            if i - length_start == length:
                output = is_bounded(board, y_end, x_end, length_2, d_y, d_x)
                if output == "CLOSED":
                    closed_count += 1
                if output == "OPEN":
                    open_seq_count +=1
                if output == "SEMIOPEN":
                    semi_open_seq_count += 1
    return open_seq_count, semi_open_seq_count, closed_count

def detects_rows_win(board, col,length):
    open_seq_count, semi_open_seq_count,closed_count = 0, 0,0
    countL = []
    for i in range(8):
        for j in [[0,1],[1,1]]:
            y_start = i
            x_start = 0
            d_y = j[0]
            d_x = j[1]
            countL.append(detects_row_win(board, col, y_start, x_start, length, d_y, d_x))

    for i in range(8):
        y_start = 0
        x_start = i
        d_y = 1
        d_x = 0
        countL.append(detects_row_win(board, col, y_start, x_start, length, d_y, d_x))

    for i in range(1,7):
        for j in [[1,1],[1,-1]]:
            y_start = 0
            x_start = i
            d_y = j[0]
            d_x = j[1]
            countL.append(detects_row_win(board, col, y_start, x_start, length, d_y, d_x))
    for i in range(8):
        y_start = i
        x_start = 7
        d_y = 1
        d_x = -1
        countL.append(detects_row_win(board, col, y_start, x_start, length, d_y, d_x))
    for i in countL:
        open_seq_count += i[0]
        semi_open_seq_count += i[1]
        closed_count += i[2]
    return open_seq_count, semi_open_seq_count,closed_count


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    run = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    length_start = 0
    j = y_start - d_y
    k = x_start - d_x
    rows = range_row(y_start,x_start,d_y,d_x)
    for i in range(rows):
        j += d_y
        k += d_x
        if board[j][k] == col and run == 0:
            first_y = j
            first_x = k
            run = 1
            length_start = i
        if run == 1 and i == rows-1 and board[j][k]== col:
            y_end = j
            x_end = k
            length_2 = i- length_start +1
            run = 0
            if length_2 == length:
                output = is_bounded(board, y_end, x_end, length_2, d_y, d_x)
                if output == "OPEN":
                    open_seq_count +=1
                if output == "SEMIOPEN":
                    semi_open_seq_count += 1
        if board[j][k]!= col and run==1:

            y_end = j - d_y
            x_end = k - d_x
            length_2 = i - length_start
            run = 0
            if i - length_start == length:
                output = is_bounded(board, y_end, x_end, length_2, d_y, d_x)
                if output == "OPEN":
                    open_seq_count +=1
                if output == "SEMIOPEN":
                    semi_open_seq_count += 1
    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    count = []
    for i in range(8):
        for j in [[0,1],[1,1]]:
            y_start = i
            x_start = 0
            d_y = j[0]
            d_x = j[1]
            count.append(detect_row(board, col, y_start, x_start, length, d_y, d_x))

    for i in range(8):
        y_start = 0
        x_start = i
        d_y = 1
        d_x = 0
        count.append(detect_row(board, col, y_start, x_start, length, d_y, d_x))
    for i in range(1,7):
        for j in [[1,1],[1,-1]]:
            y_start = 0
            x_start = i
            d_y = j[0]
            d_x = j[1]
            count.append(detect_row(board, col, y_start, x_start, length, d_y, d_x))

    for i in range(8):
        y_start = i
        x_start = 7
        d_y = 1
        d_x = -1
        count.append(detect_row(board, col, y_start, x_start, length, d_y, d_x))

    for i in count:
        open_seq_count += i[0]
        semi_open_seq_count += i[1]
    return open_seq_count, semi_open_seq_count

def search_max(board):
    score_count = []
    coordinates = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == " ":
                board[i][j] = "b"
                coordinates.append([i,j])
                score_count.append(score(board))
                board[i][j] = " "

    index_max = score_count.index(max(score_count))
    move_y = coordinates[index_max][0]
    move_x = coordinates[index_max][1]
    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    col = "w"
    if detects_rows_win(board, col, 5)[0]>0 or detects_rows_win(board, col, 5)[1] >0 or detects_rows_win(board, col, 5)[2] >0 :
        return "White won"
    col = "b"
    if detects_rows_win(board, col, 5)[0]>0 or detects_rows_win(board, col, 5)[1] >0 or detects_rows_win(board, col, 5)[2] >0:
        return "Black won"
    for i in range(8):
        for j in range(8):
            if board[i][j] == " " :
                return "Continue playing"
    return "Draw"



def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))

def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

if __name__ == '__main__':
    play_gomoku(8)
