import functools

"""
Fibonacci Array, python3下借助lru_cache实现.
"""


# python3 新增lru_cache形式.
@functools.lru_cache(maxsize=None)
def fibonacci_cache(n):
    """基本形式, 可加缓存改良."""
    if n < 2:
        return n
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


if __name__ == "__main__":

    fibonacci_cache = []
    for i in range(0, 10):
        fibonacci_cache.append(fibonacci_cache(i))

    print(fibonacci_cache)
