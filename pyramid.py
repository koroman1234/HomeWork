n = int(input("Введите высоту пирамиды (положительное целое число): "))

if n <= 0:
    print("Ошибка: высота должна быть положительным целым числом")
else:
    for i in range(n):
        for _ in range(n - i - 1):
            print(" ", end="")

        for _ in range(2 * i + 1):
            print("*", end="")

        print()