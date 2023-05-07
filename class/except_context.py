# リスト11.3


class MyContext:
    # コンテキストの作成
    def __enter__(self):
        print("**Enter**")
        return self

    # コンテキストの解放
    def __exit__(self, type, value, tb):
        # 例外の有無を判定
        if type is None:
            print("**EXIT**")
        else:
            print(f"**{value}**")
            return True

    def hoge(self):
        print("Hoge")


if __name__ == "__main__":
    with MyContext() as c:
        print("With Start")
        c.hoge()
