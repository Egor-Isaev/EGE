from functools import lru_cache

nums = set()

# @lru_cache(None) - аннтотация, увеличивающая скорость работы функций
@lru_cache(None)
def f(x, step):
    if step == 68:
        nums.add(x)
        return
    f(x + 3, step + 1)
    f(x - 3, step + 1)


f(1, 0)
print(len(nums))