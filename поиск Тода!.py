from random import*
import time
print("""Приветствую!
Это игра поиск Тода,в которой тебе нужно найти этого Тода!
Для этого я буду задавать тебе три вопроса:
какой корпус корабля посмотреть,какую комнату,и какой угол.
Желаю удачи!!!
Текущая версия: 1.2""")
a1 = input("играем?(да / нет)")
while a1 != "да" and a1 != "нет":
    print("некоректный ввод!попробуйте снова!")
    a1 = input("играем?(да / нет)")
while a1 != "нет":
    zal = randint(1,3+1)
    komnata = randint(1,10+1)
    ugol = randint(1,4+1)
    kuda_zal = int(input("выберите,в какой зал пойти:"))
    kuda_komnata = int(input("выберите в какую комнату пойти: "))
    kuda_ugol = int(input("выберите,какой угол посмотреть: "))
    while zal != kuda_zal and komnata != kuda_komnata and ugol != kuda_ugol:
        print('тод пока не найден!')
        kuda_zal = int(input("выберите,в какой зал пойти:"))
        kuda_komnata = int(input("выберите в какую комнату пойти: "))
        kuda_ugol = int(input("выберите,какой угол посмотреть: "))
    else:
        print("тод найден!")
if a1 == "нет":
    print("спасибо за использование игры! она закроется через 5 секунд")
    time.sleep(5)
    print(" ")