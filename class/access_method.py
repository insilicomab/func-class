# リスト10.19


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # nameのゲッター
    def get_name(self):
        return self.__name

    # ageのゲッター
    def get_age(self):
        return self.__age

    # nameのセッター
    def set_name(self, value):
        self.__name = value

    # ageのセッター
    def set_age(self, value):
        if value <= 0:
            raise ValueError("ageは正数で指定します。")
        self.__age = value

    def show(self):
        print(f"私の名前は{self.get_age()}、{self.get_age()}歳です！")


if __name__ == "__main__":
    p = Person("山田太郎", 15)
    p.set_age(35)
    print(p.get_age())
    p.set_age(-15)
