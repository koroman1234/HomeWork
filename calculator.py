print("=== Калькулятор ===")

first = input("Введите первое число: ")
operation = input("Введите знак операции (+, -, *, /): ")
second = input("Введите второе число: ")

a = float(first)
b = float(second)

# 3. Вычисление и вывод результата
if operation == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
elif operation == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif operation == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif operation == "/":
    if b == 0:
        print("Ошибка: деление на ноль")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
else:
    print("Ошибка: неизвестная операция. Используйте +, -, * или /")