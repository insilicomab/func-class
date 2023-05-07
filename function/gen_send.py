# リスト9.8
def gen_com():
    while True:
        # 入力ボックスの呼び出し
        n = yield input("名前を教えて下さい：")
        # sendメソッドからの値でメッセージを生成
        yield f"こんにちは、{n}さん！"


if __name__ == "__main__":
    gen = gen_com()
    for name in gen:
        res = gen.send(name.upper())
        print(res)
