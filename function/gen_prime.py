# リスト9.7
import math


def is_prime(value):
    result = True  # 素数かどうかを表すフラグ
    # 2~sqrt(value)でvalueを割り切れる（=余りが0）ものがあるか
    for i in range(2, math.floor(math.sqrt(value)) + 1):
        if value % i == 0:
            result = False  # 割り切れるものがあれば素数でない
            break
        return result


# 素数を求めるジェネレーター
def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


if __name__ == "__main__":
    for prime in get_primes():
        print(prime)
        if prime > 100:
            break
