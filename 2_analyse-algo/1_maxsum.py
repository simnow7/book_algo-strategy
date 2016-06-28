import sys


MIN = -sys.maxsize - 1
arr = [-7, 4, -3, 6, 3, -8, 3, 4]
# arr =[-2, 3, 1, 2]

# O(N^3)
def inefficientMaxSum():
    n = len(arr)
    ret = MIN

    for i in range(0, n):
        for j in range(i, n):
            s = 0
            for k in range(i, j+1):
                s += arr[k]
            ret = max(ret, s)

    return ret

# O(N^2)
def betterMaxSum():
    n = len(arr)
    ret = MIN

    for i in range(0, n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            ret = max(ret, s)

    return ret

# O(NlogN)
def fastMaxSum(arr, lo, hi):
    if(lo == hi):
        return arr[lo]

    mid = (lo + hi) / 2

    left = MIN
    right = MIN
    s = 0

    for i in range(mid, lo-1, -1):
        s += arr[i]
        left = max(left, s)

    s = 0
    for j in range(mid+1, hi+1):
        s += arr[j]
        right = max(right, s)

    single = max(fastMaxSum(arr, lo, mid),
                 fastMaxSum(arr, mid+1, hi))

    return max(left + right, single)

# O(N)
def fastestMaxSum():
    n = len(arr)
    ret = MIN
    psum = 0
    for i in range(0, n):
        psum = max(psum, 0) + arr[i]
        ret = max(psum, ret)

    return ret


if __name__ == '__main__':
    print(inefficientMaxSum())
    print(betterMaxSum())
    print(fastMaxSum(arr, 0, len(arr)-1))
    print(fastestMaxSum())