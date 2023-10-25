def print_seq(n):
    if n > 0:
        print_seq(n - 1)
        print(n, end=' ')


def sum_seq(n):
    if n > 0:
        return n + sum_seq(n - 1)
    else:
        return 0


print_seq(10)
print(f'\nSum = {sum_seq(10)}')