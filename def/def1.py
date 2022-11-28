def print_label(name):
    print('Колледж Сириус')
    print('Имя:', name)
    print('Группа:')

print('Печать бейджков')
amount = int(input('Число учеников'))
for i in range(amount):
    name = input('Имя ученика:')
    print_label(name)
print('Готово! Заберите бейджики!')
