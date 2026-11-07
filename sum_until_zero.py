total = 0
count = 0

while True:
    number = int(input("Введите число (0 — завершить): "))

    if number == 0:
        break

    total += number
    count += 1

print(f"Сумма чисел: {total}")
print(f"Количество чисел: {count}")