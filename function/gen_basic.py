# リスト9.6
def my_gen():
    yield "あいうえお"
    yield "かきくけこ"
    yield "さしすせそ"


if __name__ == "__main__":
    for value in my_gen():
        print(value)
