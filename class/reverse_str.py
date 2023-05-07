# リスト11.8, 11.9


class Person:
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    # インスタンスの文字列表現を生成
    def __str__(self):
        return f"{self.lastname} {self.firstname}"

    def __repr__(self) -> str:
        return f"Person({self.lastname} {self.firstname})"

    # プロパティを定義
    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname


if __name__ == "__main__":
    p = Person("太郎", "山田")
    print(p)
    print(repr(p))
