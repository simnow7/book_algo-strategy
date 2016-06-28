
INF = 9999
SWITCHES = 10
CLOCKS = 16
linked = [ 
    "xxx.............",
    "...x...x.x.x....",
    "....x.....x...xx",
    "x...xxxx........",
    ".....xxx..x.x...",
    "x.x...........xx",
    "...x..........xx",
    "....xx.x......xx",
    ".xxxxx..........",
    "...xxx...x...x..",
]

def areAligned(clocks):
    for clock in clocks:
        if clock != 12:
            return False
    
    return True

def push(clocks, swtch):
    for clock in range(CLOCKS):
        if linked[swtch][clock] == 'x':
            clocks[clock] += 3
            if clocks[clock] == 15:
                clocks[clock] = 3

def solve(clocks, swtch):
    if swtch == SWITCHES:
        if areAligned(clocks):
            return 0
        else:
            return INF
    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, swtch + 1))
        push(clocks, swtch)
    # push x 4 = original state
    return ret


if __name__ == '__main__':
    # cases = raw_input('num of cases(<=30): ')
    # for i in range(int(cases)):
        # clocks = raw_input('16 clocks : ')
        # cl = [int(clock) for clock in clocks.split()]
        
    # cl = [12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]
    cl = [12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6]
    print(solve(cl, 0))