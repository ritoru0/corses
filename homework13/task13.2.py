def cyclic_sequence():
    seq = [1, 2, 3, 6, 8]
    index = 0
    while True:
        yield seq[index]
        index = (index + 1) % len(seq)

n = int(input("Введите количество чисел для вывода "))
if n <= 0:
    raise ValueError("Количество должно быть положительным числом")

gen = cyclic_sequence()

for _ in range(n):
    print(next(gen))
