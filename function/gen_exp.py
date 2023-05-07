# リスト9.10
import random

gen = (random.random() for i in range(100))
# def my_gen():
#   for i in range(100):
#     yield random.random()
# gen = my_gen()

if __name__ == "__main__":
    for num in gen:
        print(num)
