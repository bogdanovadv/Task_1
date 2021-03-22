operations = ("+", "-", "*", "/", "//", "%", "**", "&", "|", "^", ">>", "<<")
digit = input("Введите число: ")
while not digit.isdigit():
    digit = input("Введено не число. Попробуйте еще раз: ")
result = int(digit)
while True:
    expression = input("Введите знак операции и число (или '='): ").split(' ')
    if expression[0] in operations and expression[1].isdigit():
        try:
            result = eval("{}{}{}".format(result, expression[0], expression[1]))
        except ValueError:
            print("Ошибка в выражении")
    elif expression[0] == "=":
        break
    else:
        print("Ошбка при вводе операции или числа")
print(f'Результат: {result}')

