""" 2. ТАБЛИЦА УМНОЖЕНИЯ
Напишите программу, которая будет выводить в
консоль таблицу умножения от 1 до 10 (как в вконце
старых тетрадок, квадратная такая
"""

factor_1 = 1
factor_2 = 1

for i in range(10):
    while factor_2 < 11:
        product = factor_1 * factor_2
        print(f'{factor_1} * {factor_2} = {product}')
        factor_2 += 1

    else:
        print()
        factor_2 = 1
        factor_1 += 1
