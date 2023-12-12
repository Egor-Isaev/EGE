def f(n):
    a = ''
    while n > 0:
        a = str(n % 6) + a
        n //= 6
    return a

c = 3 * 216 ** 4 + 2 * 36 ** 6 - 648
b = str(f(c))
print(b.count('5'))