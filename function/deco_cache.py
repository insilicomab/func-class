# リスト9.3
import random
from functools import lru_cache


@lru_cache(maxsize=8)
def get0to100():
    return random.randint(0, 100)


if __name__ == '__main__':
    print(get0to100())
    print(get0to100())