# リスト10.29


class MyStack:
    # 委譲先のオブジェクトを変数に保持
    def __init__(self):
        self.__data = []

    # 必要に応じて処理を委譲
    def push(self, elem):
        self.__data.append(elem)

    def pop(self):
        return self.__data.pop()


if __name__ == "__main__":
    s = MyStack()
    s.push(40)
    print(s.pop())
