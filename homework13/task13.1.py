def fibonachi(n):
    if n <= 0:
        raise ValueError("Введите положительное число")
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Введите номер числа Фибоначчи для вывода последовательности "))

for num in fibonachi(n):
    print(num)
