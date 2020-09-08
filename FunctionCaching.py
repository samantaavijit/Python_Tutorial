import time
from functools import lru_cache


def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n


@lru_cache(maxsize=3)  # by default save the value last 3 value
def cacheWork(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done... Calling again")
    some_work(3)
    print("Done")

    print("Now running Cache work")
    cacheWork(3)
    print("Done... Calling again")
    cacheWork(3)
    print("Done")
