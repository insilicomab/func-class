import types


def show_first(self):
    print(f"名前は{self.firstname}です！")


def show_last(self):
    print(f"苗字は{self.firstname}です！")


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f"私の名前は{self.lastname}{self.firstname}です！")


if __name__ == "__main__":
    p1 = Person("太郎", "山田")
    p2 = Person("次郎", "鈴木")

    # メソッドを動的に追加
    Person.show_first = show_first
    p1.show_last = types.MethodType(show_last, p1)
    p1.show_first()  # 結果：名前は太郎です！
    p1.show_last()  # 結果：苗字は山田です！
    p2.show_first()  # 結果：名前は次郎です！
    p2.show_last()  # 結果：エラー
