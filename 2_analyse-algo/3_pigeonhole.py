import sys


# fraction a/b to decimal
# suppose a>=0, b>0
def printDecimal(a, b):
    it = 0
    inf = []
    while a > 0:
        if it == 1:
            sys.stdout.write('.')

        sys.stdout.write(str(a/b))
        a = (a % b) * 10

        if it >= b + 1:
            sys.stdout.write('..')
            break

        it += 1

    print('')


if __name__ == '__main__':
    printDecimal(1, 111)