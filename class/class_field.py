# リスト11.26
import dataclasses


@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = dataclasses.field(default=0, compare=False)

    def show(self):
        print(f"私の名前は{self.lastname}{self.firstname}です！")


if __name__ == "__main__":
    p1 = Person("太郎", "山田", 58)
    p2 = Person("太郎", "山田", 11)
    print(p1 == p2)
