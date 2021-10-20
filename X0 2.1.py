print("-=Х Крестики - Нолики 0=-")
print("-" * 26)
print("Правила игры!")
print("Формат ввода для своего знака используется две координаты введенные через пробел: ")
print("Первая введённая Вами цифра отвечает за координату по вертекальи")
print("Вторая введённая Вами цифра через пробле отвечает за координату по горизонтали")
print("-" * 82)

def game_place():
    print(f"   0 1 2")
    for i in range(3):
        row_info = ' '.join(field[i])
        print(f"{i}  {row_info}")

def player_input():
    while True:
        cords = input("    Ваш ход:    "). split()
        if len(cords) != 2:
            print(" Введите 2 координаты через пробел ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Нужно ввести числа координат!")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты недопустимы! Введите координаты которые находятся в допустимом дипзоне игрового поля")
            continue

        if field[x][y] != " ":
            print("Выбраное поле уже занято")
            continue
        return x, y

def win_coords():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Победил Крестик, урааа!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победили нолики, урааа!!!")
            return True
    return False

field = [[""] * 3 for i in range(3)]  # размер игрового поля
num = 0
while True:
    num += 1

    game_place()

    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = player_input()  # Распаковка двух переменых из функции ask

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if win_coords():
        break

    if num == 9:
        print('Ничья!!!')
        break