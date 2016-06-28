n = 0
areFriends = [[False for col in range(10)] for row in range(10)]

def countPairingsFalse(taken):
    finished = True
    for i in range(0, n):
        if not taken[i]:
            finished = False

    if finished:
        return 1

    ret = 0
    
    for i in range(0, n):
        for j in range(0, n):
            if not taken[i] and not taken[j] and areFriends[i][j]:
                taken[i] = taken[j] = True
                ret += countPairingsFalse(taken)
                taken[i] = taken[j] = False

    return ret
 
# upper limit(n <= 10): 9 x 7 x 5 x 3 x 1 = 945
def countPairings(taken):
    firstFree = -1
    for i in range(0, n):
        if not taken[i]:
           firstFree = i
           break
    
    if firstFree == -1:         
        return 1
     
    ret = 0
    
    for pairWidth in range(firstFree+1, n):
        if not taken[pairWidth] and areFriends[firstFree][pairWidth]:
            taken[firstFree] = taken[pairWidth] = True
            ret += countPairings(taken)
            taken[firstFree] = taken[pairWidth] = False
     
    return ret

if __name__ == '__main__':
    cases = raw_input('num of cases(<=50): ')
    for i in range(0, int(cases)):
        # nm = raw_input('num of students(2<=N<=10) | num of pair of friends(0<=M<=N(N-1)/2): ')
        # pair = raw_input('pair of friends: ')
        
        # nm = '4 6'
        # pair = '0 1 1 2 2 3 3 0 0 2 1 3'
        
        nm = '6 10'
        pair = '0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5'
        
        temp = nm.split()
        n = int(temp[0])
        m = int(temp[1])
        pair = pair.split()
        pre = 0
        for i in range(0, m*2):
            if i & 1 == 0:
                pre = int(pair[i])
            else:
                areFriends[pre][int(pair[i])] = True
                areFriends[int(pair[i])][pre] = True

        taken = [False for row in range(10)]
        print(countPairings(taken))

