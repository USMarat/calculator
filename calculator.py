a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Выберите операцию:")
print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")

choice = input("Введите номер операции: ")

if choice == "1":
    print("Результат:", a + b)
elif choice == "2":
    print("Результат:", a - b)
elif choice == "3":
    print("Результат:", a * b)
elif choice == "4":
    print("Результат:", a / b)
else:
    print("Неверный выбор")
