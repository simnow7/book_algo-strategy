def loop(n):
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    print(i, j, k, l)


def recursion(n, picked, toPick):
    if toPick == 0:
        print(picked)
        return

    if not picked:
        smallest = 0
    else:
        smallest = picked[-1] + 1
    
    for nxt in range(smallest, n):
        picked.append(nxt)
        recursion(n, picked, toPick - 1)
        picked.pop()


if __name__ == '__main__':
    loop(5)
    recursion(5, [], 4)