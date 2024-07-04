def make_parole(a):
    for L in range(1, a+1):
        Parole = str()
        for i in range(1, L):
         for j in range(i+1, L):
            if L % (i +j) == 0:
             Parole = Parole + str(i) + str(j)
    print(f'Пароль для {a}: {Parole}')
while 1>0:
    x = (input ('Значение первого камня (от 3 до 20):'))
    if x.isnumeric():
        n_stone = int(x)
        if n_stone>= 3 and n_stone<=20:
            make_parole(n_stone)
            break
        else:
            print("Некорректное значение. Попробуйте снова")
    else:
        print('Используйте, пожалйста, цифры')
        continue
