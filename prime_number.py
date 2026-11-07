number = int(input("Введите целое число: "))

if number < 2:
    print(f"Число {number} — не простое")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print(f"Число {number} — не простое, делится на {divisor}")
            break
    else:
        print(f"Число {number} — простое")