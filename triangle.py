class SideCannotBeZero(Exception):
    pass


while True:
    try:
        first_side = abs(int(input('Длина первого катета: ')))
        if first_side == 0:
            raise SideCannotBeZero
        second_side = abs(int(input('Длина второго катета: ')))
        if second_side == 0:
            raise SideCannotBeZero

        hypotenuse = (first_side**2 + second_side**2)**0.5

        print(f'Площадь треугольника: {round(first_side * second_side / 2, 2)}')
        print(f'Периметр треугольника: {round(first_side + second_side + hypotenuse, 2)}')

        break

    except SideCannotBeZero:
        print('Длина катета не может быть равна нулю')
        continue
    except ValueError:
        print('В строке должны быть только цифры')
        continue
