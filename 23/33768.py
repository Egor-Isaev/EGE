def f(x, y):
    # Ограничение "траектория не содержит число n"
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)


print(f(2, 11) * f(11, 16))