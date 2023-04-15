''' 1. ПАЛИНДРОМЫ
а) на вход подается слово - проверить, является ли оно палиндромом
Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
Больше примеров слов-палиндромов
довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
level deified noon Racecar radar repaper
б) на вход подается фраза - проверить, является ли она палиндромом
Не учитывается регистр, знаки препинания и пробелы.
Примеры фраз-палиндромов
А роза упала на лапу Азора
Я иду с мечем судия
Хил, худ, а дух лих. ——> точки и запятые?
Тарту дорог, как город утрат
А путана тупа
И темен город. Мороз, узором дорог не мети.
Леша на полке клопа нашел.
Аргентина манит негра
Straw? No, too stupid a fad. I put soot on warts
Was it a cat I saw?
Do geese see God?
Madam, I'm Adam
Pull up if I pull up
No lemon, no melon '''

palindrome = str(input('Введите палиндром: '))
pal = palindrome.replace(" ", "")
pal = pal.lower()
pal = "".join(i for i in pal if i.isalpha())

#print(pal)

first_midl = pal[:len(pal) // 2]
sec_midl = pal[len(pal) // 2:]

if len(sec_midl) % 2:
    sec_midl = sec_midl
else:
    sec_midl = pal[len(pal) // 2 + 1:]
    sec_midl = sec_midl[::-1]

    if len(sec_midl) % 2:
        sec_midl = sec_midl
    else:
        sec_midl = pal[len(pal) // 2 + 1:]
        sec_midl = sec_midl[::-1]

if len(first_midl) % 2:
    first_midl = first_midl
else:
    sec_midl = pal[len(pal) // 2 + 1:]
    sec_midl = sec_midl[::-1]

if first_midl == sec_midl:
    print(f'{palindrome} >>> ПАЛИНДРОМ')
else:
    print(f'{palindrome} >>> НЕ ПАЛИНДРОМ')

#print(first_midl, sec_midl)
