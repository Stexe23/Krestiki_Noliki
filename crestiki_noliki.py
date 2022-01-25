Pole = list(range(1, 10))
win_coord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def Gen_Pole():
    print("-------------")
    for i in range(3):
        print("|", Pole[0+i*3], "|", Pole[1+i*3], "|", Pole[2+i*3], "|")
        print("-------------")


def hod(hod_p):
    while True:
        pole = input('Выбери поле для хода ' +hod_p+ ': ')
        if not (pole in '123456789'):
            print('Не верный ввод. Повторите ещё раз')
            continue
        pole = int(pole)
        if str(Pole[pole-1]) in 'X0':
            print('Эта клетка уже занята')
            continue
        Pole[pole-1] = hod_p
        break


def winter():
    for ex in win_coord:
        if Pole[ex[0]-1] == Pole[ex[1]-1] == Pole[ex[2]-1]:
            return Pole[ex[1]-1]
    else:
        return False


def igra():
    counter = 0
    while True:
        Gen_Pole()
        if counter % 2 == 0:
            hod("X")
        else:
            hod("O")
        counter += 1
        if counter > 4:
            tmp = winter()
            if tmp:
                Gen_Pole()
                print(tmp, "Выиграл!")
                break
        if counter > 8:
            print("Ничья!")
            break


igra()
