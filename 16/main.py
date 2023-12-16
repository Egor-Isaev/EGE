import sys
sys.setrecursionlimit(5000)


def sum_seq(n):
    if n == 0:
        return 0
    return n + sum_seq(n - 1)


print(sum_seq(100))
