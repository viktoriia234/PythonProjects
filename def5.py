def mark (food):
    if  food > 80:
        return "Наградить дипломом"
    elif food > 50 and food <= 80 :
        return "Наградить похвальной грамотой"
    else:
        return "ВЫдать грамоту об участии"

while True:
    name = input('Имя студента')
    if name == "стоп":
        break
    subject = int(input('Число предметов'))
    ball = 0
    for i in range(subject):
        ball += int(input('Число баллов'))
    print('Итоговый счёт:',ball )
    print(mark (ball))
