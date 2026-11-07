numbers = []
for i in range(5):
    value = float(input(f"Введите число {i + 1}: "))
    numbers.append(value)

total = 0
for x in numbers:
    total += x

average = total / len(numbers)

maximum = numbers[0]
for x in numbers:
    if x > maximum:
        maximum = x

sorted_numbers = numbers[:]
n = len(sorted_numbers)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if sorted_numbers[j] < sorted_numbers[j + 1]:
            sorted_numbers[j], sorted_numbers[j + 1] = (
                sorted_numbers[j + 1], sorted_numbers[j]
            )

print(f"Сумма: {total:g}")
print(f"Среднее арифметическое: {average:g}")
print(f"Максимальное значение: {maximum:g}")
print("Список по убыванию:", ", ".join(f"{x:g}" for x in sorted_numbers))