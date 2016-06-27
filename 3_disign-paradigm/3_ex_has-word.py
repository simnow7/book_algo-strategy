board = [ 
          [ 'U', 'R', 'L', 'P', 'M' ],
          [ 'X', 'P', 'R', 'E', 'T' ], 
          [ 'G', 'I', 'A', 'E', 'T' ], 
          [ 'X', 'T', 'N', 'Z', 'Y' ], 
          [ 'X', 'O', 'Q', 'R', 'S' ], 
        ]

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

# O(N^8)
def hasWord(y, x, word):
    try:
        board[y][x]
    except IndexError:
        return False

    if board[y][x] != word[0]:
        return False

    if len(word) == 1:
        return True

    for direction in range(0, 8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if hasWord(nextY, nextX, word[1:]):
        	return True

    return False


if __name__ == '__main__':
    print(hasWord(0, 3, 'PRETTY'))
    print(hasWord(2 ,0 ,'GIRL'))
    print(hasWord(1 ,2 ,'REPEAT'))
    print(hasWord(0 ,3 ,'PIZZA'))