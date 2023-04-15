''' 3. ИСТИННОСТЬ ПРЕДИКАТ
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
Данное выражение истинно при любых значениях предикат (предикат -
переменная, которая может иметь только два значения True или False)
Напишите программу, которая докажет это. '''

for x in range(0, 2):
    #   print(x)
    for y in range(0, 2):
        #      print(y)
        for z in range(0, 2):
            #           print(z)
            res = (not(x or y or z)) == ((not x) and (not y) and (not z))

            if res is True:
                res = True
            else:
                res = False
            if x == 0:
                x = False
            else:
                x = True
            if y == 0:
                y = False
            else:
                y = True
            if z == 0:
                z = False
            else:
                z = True

            print(f' X = {x}  Y = {y}  Z =  {z}')
            print(f'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z >>> {res}')
            print()

