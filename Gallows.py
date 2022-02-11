pazzleword = 'красота'
usedlett = ''
setwsmall = ''
nosimlett = ''
knownword = '*' * len(pazzleword)
alphabet_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
tries = 0                                        # Правила.
print('Правила игры: \n1 Вводите по одной букве или сразу слово, такой же длинны, как загаданное\
слово.\n2 У вас 10 попыток! Если ошибетесь, при написании слова или введете не букву,\n  или же введете \
букву, которую уже использовали до этого, то попытка не защитывается.\n3 Играйте в радость! Удачи!\nЕсли\
забудите правила, напишите в стоке команду: "!help", тамже можно узнать о других командах')
print('Ваше слово:\n' + knownword)
while tries != 10:
    print('Введите букву или слово. Количество оставшихся попыток:', str(10 - tries) + '.')
    setw = input()
    sacksetw = set(setw)
    for i in sacksetw:
        nosimlett += i
    if setw[0] == '!':                               # Команды.
        if setw[1:] == 'help':
            print('Была использована команда "!help".\nПравила игры: \n1 Вводите по одной букве или \
сразу слово, такой же длинны, как загаданноеслово.\n2 У вас 10 попыток! Если ошибетесь, \
при написании слова или введете не букву,\n  или же введете букву, которую уже использовали \
до этого, то попытка не защитывается.\nДругие комманды, их вы можете использовать в любое \
время игры:\n"!tries" - показывает сколько попыток остальсь.\n"!letters" - показывает \
какие буквы были использованы по ходу игры.\n"!word" - показывает известное слово')
        elif setw[1:] == 'tries':
            print('У вас осталось попыток:', str(10 - tries) + '.')
        elif setw[1:] == 'letters':
            print('Все использованные буквы, не зависимо от регистра: "' + usedlett + '".')
        elif setw[1:] == 'word':
            print('Слово, известное на данный момент: "' + knownword + '".')
        else:
            print('Повторю, пиши букву или слово! Никаких иных символов или слогов! Попытка не защитана.')
        tries -= 1
                           # Есть ли буква в загаданном слове + проверка повторялась ли буква + проверка буква ли это.
    elif len(setw) == 1 and ((setw in alphabet_big) or (setw in alphabet_small)) and (setw not in usedlett):
        if setw in alphabet_big:
            setw = chr(ord(setw) + 32)
        for i in range(len(pazzleword)):
            if setw == pazzleword[i]:
                knownword = knownword[:i] + setw + knownword[i + 1:]  # Составление слова, если буква правильная.
        usedlett += setw + chr(ord(setw) - 32)  # Фиксация использованной буквы.
        if setw in pazzleword:
            print("Буква '" + setw + "' есть в загаданном слове.")      # Показывание игроку информации.
        else:
            print("Буквы '" + setw + "' в загаданном слове нет.")
        print(knownword)
        if pazzleword == knownword:                    # Проверка составлино ли слово.
            tries = 9
    elif len(setw) == 1 and ((setw in alphabet_big) or (setw in alphabet_small)):        # Ответ, если буква уже была использована.
        print('Введенная буква уже была испльзована. Попытка не защитана.')
        tries -= 1
    elif len(setw) == len(pazzleword) and (nosimlett in (alphabet_big + alphabet_small)):        # Проверка слова, введенного, как правильного.
        for i in range(len(setw)):
            if ord(setw[i]) < 1072:
                setwsmall += chr(ord(setw[i]) + 32)
            else:
                setwsmall += setw[i]
        if setwsmall == pazzleword:
            knownword = pazzleword
            tries = 9
        else:
            setwsmall = ''
                                       # Проверка нарушения правил.
    else:
        print('Повторю, пиши букву или слово! Никаких иных символов или слогов! Попытка не защитана.')
        tries -= 1
    nosimlett = ''
    sacksetw = ''
    tries += 1
                                       # Вывод результата.
if pazzleword == knownword:
    print('Позравляю! Слово найдено! Затарачено попыток:', tries + '.')
else:
    print('Попытки кончились. Не расстраивайся, повезет в следующий раз!')