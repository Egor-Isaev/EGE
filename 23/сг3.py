def f(x, y, s):
    if x % 2 == 0:
        s = s + 1
    if x > y or s > 4:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, s) + f(x * 2, y, s)
print(f(1,19,0))