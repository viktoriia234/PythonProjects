def imt (x,y):
    return x/(y*y)

def result (some):
    if some < 18.5:
        print("Недостаточный вес")
    elif some >= 18.5 and some <= 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")

weight = int(input("Сколько вес?"))
height = int(input("Сколько рост?"))
index = imt(weight, height)
result(index)
