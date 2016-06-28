
# 4 ways to cover a board :  relative postion [dy, dx]
coverType = [
    [ [0, 0], [1, 0], [0, 1] ],
    [ [0, 0], [0, 1], [1, 1] ],
    [ [0, 0], [1, 0], [1, 1] ],
    [ [0, 0], [1, 0], [1, -1] ], 
]

# (y, x) of cell can be covered or removed by type
# delta = 1 means 'cover' and -1 does 'remove'
# invaild cover will return false
def set(board, y, x, t, delta):
    ok = True
    for i in range(0, 3):
        ny = y + coverType[t][i][0]
        nx = x + coverType[t][i][1]
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        else:
            board[ny][nx] += delta
            if board[ny][nx] > 1:
                ok = False
    
    return ok

# Upper limit: 50/3 = 16, 4^16 = 2^32
def cover(board):
    y = -1
    x = -1
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    
    if y == -1:
        return 1
    
    ret = 0
    
    for t in range(0, 4):
        # if board[y][x] can be covered by type, do recursion
        if set(board, y, x, t, 1):
            ret += cover(board)
        # uncover
        set(board, y, x, t, -1)
        
    return ret


# board[i][j] = 1 means '# covered'
# board[i][j] = 0 means '. empty'
if __name__ == '__main__': 
    cases = raw_input('num of cases(<=30): ')
    for i in range(int(cases)):
        # cells <= 50
        
        # hw = raw_input('High(H>=1) | Width(W<=20): ')
        # temp = hw.split()
        # board = []
        # h = int(temp[0])
        # w = int(temp[1])
        # for j in range(0, h):
        #     h_temp = raw_input()
        #     board.append([int(cell) for cell in h_temp.split()])

        board = [
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1],
            ]
            
        print(cover(board))


# 3 7
# 1000001
# 1000001
# 1100111

# 8 10
# 1111111111
# 1000000001
# 1000000001
# 1000000001
# 1000000001
# 1000000001
# 1000000001
# 1111111111