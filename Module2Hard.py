def make_parole (n): # n - значение 1-ого камня
    list_ = list() # список кратных делителей n
    list_.append(n)
    for i in range(n): # составление списка кратных делителей n
        if n % (i + 1) == 0 and (i + 1) > 2 and (i + 1) != n:
            list_.append(i + 1)
    pary = list()# список слагаемых для списка list_
    for index in list_:
        for i in range(index):
            j = index - i - 1
            if i + 1 < j:
                summ = str(i + 1) + str(j)
                pary.append(summ)
    pary.sort()
    parole = str()
    for i in pary:
        parole = parole + i
    return parole
first_stone = list()
stone_min = 3
stone_max = input( 'Максимальное значение первого камня (по условию - 20):')
stone = int (stone_min)
while stone <= int (stone_max):#формирование "базы" первых камней
    first_stone.append(stone)
    stone = stone +1
for i in first_stone:
    print ('Для', i, 'Пароль:', make_parole(i))