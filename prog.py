letters = ('a', 'o', 'u', 'i', 'e', 'y')
string = input("Введите строку: ")
for i in letters:
    print(i, string.count(i), end=', ')
