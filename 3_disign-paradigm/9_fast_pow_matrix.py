
import numpy as np

def pow(squareMatrix, m):
    if m == 0:
        return len(squareMatrix)
    if m % 2 > 0:
        return np.power(squareMatrix, m-1) @ squareMatrix
    half = np.power(squareMatrix, m / 2)

    return half @ half

a = np.array([[1, 2], [3, 4]])
print(pow(a, 3))