# リスト8.30
def factorial(num):
    if num != 0:
        return num * factorial(num-1)
    return 1


if __name__ == '__main__':
    print(factorial(5))