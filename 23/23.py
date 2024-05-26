def f(x, y, k):
    if x % 2 == 0:
        k += 1
    if x > y or k > 4:
        return 0
    if x == y and k <= 4:
        return 1
    return f(x + 1, y, k) + f(x * 2, y, k)


print(f(1, 17, 0))
       