#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – #гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы #все монетки были повернуты вверх одной и той же стороной. Выведите минимальное #количество монет, которые нужно перевернуть

from random import randint
amount = int(input("Введите количество манет = "))
count_zero = count_one = 0
for i in range(amount):
    many = randint(0,1)
    if many == 0:
        count_zero += 1
    else:
        count_one += 1
if count_zero > count_one:
    print(f"Необходимо перевернуть {count_one} монет")
else:
    print(f"Необходимо перевернуть {count_zero} монет")
