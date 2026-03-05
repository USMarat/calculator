import random

number = random.randint(1, 10)

print("Я загадал число от 1 до 10")

guess = int(input("Попробуй угадать: "))

if guess == number:
    print("🎉 Ты угадал!")
else:
    print("❌ Не угадал")
    print("Я загадал число:", number)
