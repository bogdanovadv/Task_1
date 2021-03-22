letters = ('a', 'o', 'u', 'i', 'e', 'y')
string = input("Введите строку: ").lower()
for i in letters:
    print(i, string.count(i), end=", " if letters[-1] != i else "")
