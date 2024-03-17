nums = set()


def f(x, step):
    if step == 13:
        nums.add(x)
        return
    f(x - 3, step + 1)
    f(x * (-3), step + 1)


f(333, 0)
print(len([x for x in nums if x < 0]))
