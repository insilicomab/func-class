# リスト8.32
def walk_list(data, func):
    for key, value in enumerate(data):
        func(value, key)


result = 0


def calcu_sum(value, key):
    global result  # グローバル変数の利用を宣言
    result += value


if __name__ == "__main__":
    data = [105, 53, 27, 87, 33]
    walk_list(data, calcu_sum)
    print(result)
