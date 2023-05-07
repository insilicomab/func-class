# リスト11.27, 28
import dataclasses


@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0
    memos: list = dataclasses.field(default_factory=list)

    def show(self):
        print(f"私の名前は{self.lastname}{self.firstname}です！")


if __name__ == "__main__":
    ms = ["married", "AB"]
    p = Person("太郎", "山田", 58, ms)
    ms.append("dog")
    print(p)
