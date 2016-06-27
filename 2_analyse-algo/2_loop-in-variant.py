# arr is sorted in ascending order
# return i of arr[i-1] < x <= arr[i]
# arr[-1] = -infinite / arr[n] = +infinite
def binsearch(arr, x):
    n = len(arr)
    lo = -1
    hi = n
    # loop-in-variant: lo < hi
    # loop-in-variant: arr[lo] < x <= arr[hi]
    while lo + 1 < hi:
        mid = (lo + hi) / 2

        if(arr[mid] < x):
            lo = mid
        else:
            hi = mid
        # loop-in-variant
    return hi


def insertionSort(arr):
    for i in range(0, len(arr)):
    	# loop-in-vaiant: arr[0..i-1] already sorted
        # insert arr[i] at arr[0..i-1]
        j = i
        while j > 0 and arr[j-1] > arr[j]:
        	# loop-in-variant: arr[j] < arr[j+1..i]
        	# loop-in-variant: arr[0..i] sorted except arr[j]
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1

    print(arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binsearch(arr, 5))

    arr = [8, 7, 6, 5, 4, 3, 2, 1]
    insertionSort(arr)    