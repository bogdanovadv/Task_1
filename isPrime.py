digit = input("Введите число: ")
while not digit.isdigit():
    digit = input("Введено не число. Попробуйте еще раз: ")
digit = int(a);
i = 2
k = True
while k and i <= digit // 2:
    k = digit % i != 0
    i += 1
    print(i)
if k:
    print("Простое число")
else:
    print("Не простое число")