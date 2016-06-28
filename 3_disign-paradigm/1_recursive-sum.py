def for_sum(n):
    ret = 0
    for i in range(0, n+1):
        ret += i
    return ret

def recur_sum(n):
    if n == 1:
        return 1
    return n + recur_sum(n-1)


if __name__ == '__main__':
	print(for_sum(5))
	print(recur_sum(5))