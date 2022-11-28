def school(some):
    if some > 50:
        print("True")
    else:
        print("Вы отчислены")

count = int(input("Число учеников"))
for i in range(count):
    ball = int(input("Сколько баллов?"))
    school(ball) 
