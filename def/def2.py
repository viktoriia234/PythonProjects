def discount(some):
    if some >= 0 and some <=49:
        return "Скидка 10%"
    elif some >= 50 and some <= 99:
        return "Скидка 15%"
    elif some >= 100:
        return "Скидка 20%"
    else:
        return "Скидки нет"



ball = int(input("Вашши баллы"))
print("Ваша скидка: ", discount(ball))



