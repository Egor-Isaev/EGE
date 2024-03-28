import itertools


def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n // 10) + n % 10
    if n % 2 != 0:
        return f(n // 10)


s = itertools.product('013579', repeat=9)
c = 0
for str in s:
    l=''.join(str)
    if l[0]!=0:
        c += 1
print(c)
