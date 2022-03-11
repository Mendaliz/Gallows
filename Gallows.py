# Основные переменные.
sackpazzleword = {'бумагопрядильный', 'экспансия', 'четырёхполюсник', 'катаваси\
я', 'аксельбанты', 'трихомудии', 'шкандыбать', 'пердимонокль', 'драдедамовый'}
pazzleword = sackpazzleword.pop()
knownword = '*' * len(pazzleword)
alphabet_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
usedlett = ''
usedlett_small = ''
setwsmall = ''
nosimlett = ''
outletters = alphabet_small
gamerules = 'Правила игры: \n1 Вводите по одной букве или сразу верное слово. \
\n2 Если нарушите правило 1 или введёте букву, которую уже \
использовали до этого,\n  то попытка не защитывается.\
\n3 Играйте в радость! Удачи!\n'
mistake = 'Повторю, пиши букву или слово! Никаких иных символов или слогов!\
 Попытка не защитана.'
othercommands = 'Другие \
комманды:\n"!tries" - показывает сколько попыток остальсь.\n"!outletters" - \
показывает какие буквы еще не были использованы.\n"!word" - показывает \
известное слово.\n"!giveup" - позволяет сдаться.'

# Переменные благодаря которым осуществляется подсчет и вывод попыток.
endtr = 0
tries = 0

# Переменная использумая для осуществления команды !giveup.
gup = 0

# Определение количества попыток.
alltries = len(pazzleword) * 2 if (len(pazzleword) * 2) < 25 else 25

# Выдача информации о правилах игроку.
print(gamerules + 'Если забудите правила, напишите в строке команду: "!help", \
там же можно узнать о других командах')
print('Ваше слово:\n' + knownword, len(knownword), 'бкув.')

# Ограничение попыток ввода.
while endtr != alltries:
    print('Введите букву или слово. Количество оставшихся попыток:', str(alltries - tries) + '.')

# Побочные переменные.
    setw = input()
    setwsmall = ''
    nosimlett = ''
    sacksetw = ''    
    sacksetw = set(setw)
    for i in sacksetw:
        nosimlett += i

# Перевод всех написанных букв в прописные.
    for i in range(len(setw)):
        if ord(setw[i]) < 1072:
            setwsmall += chr(ord(setw[i]) + 32)
        else:
            setwsmall += setw[i]

# Центр нахождения неиспользованных букв алфавита.
    for i in range(len(usedlett_small)):
        numberoutlett = 0
        for j in outletters:
            if usedlett_small[i] == j:
                outletters = outletters[:numberoutlett] + outletters[numberoutlett + 1:]
            numberoutlett += 1

# Проверка была ли введена пустая строка.
    if setw == '':
        print(mistake)
        endtr -= 1
        tries -= 1

# Определение написана команда или ошибка ввода.
    elif setw[0] == '!':
  
# Перевод всех заглавных бкув в команде в прописные.
        setwsmall = ''
        for i in range(1, len(setw)):
            if ord(setw[i]) < 97:
                setwsmall += chr(ord(setw[i]) + 32)
            else:
                setwsmall += setw[i]
         
# Комманда "!help".
        if setwsmall == 'help':
            print('Была использована команда "!help".\n' + gamerules + othercommands)
   
# Комманда "!tries".
        elif setwsmall == 'tries':
            print('У вас осталось попыток:', str(alltries - tries) + '.')
   
# Комманда "!outletters".
        elif setwsmall == 'outletters':
            print('Оставшиеся буквы, не зависимо от регистра: "' + outletters + '".')
   
# Комманда "!word".
        elif setwsmall == 'word':
            print('Слово, известное на данный момент: "' + knownword + '"', str(len(knownword)), 'букв.')
   
# Комманда "!giveup".
        elif setwsmall == 'giveup':
            endtr = alltries
            gup = 1
    
# Вывод информации, если была введена не команда.
        else:
            print('Повторю, пиши букву или слово! Никаких иных символов или\
слогов! Попытка не защитана.')
   
# Восствновление количества попыток.
        tries -= 1
        endtr -= 1
        setwsmall = ''
        
# Проверка написана ли буква рус. алфавита и повторялась ли она.
    elif len(setw) == 1 and (setw in (alphabet_big + alphabet_small)) and (setw not in usedlett):
  
# Составление слова, если буква правильная.
        for i in range(len(pazzleword)):
            if setwsmall == pazzleword[i]:
                knownword = knownword[:i] + setwsmall + knownword[i + 1:]
     
# Фиксация использованной буквы.
        usedlett += setwsmall + chr(ord(setwsmall) - 32)
 
# Фиксация использованных букв с переводом в прописные.
        usedlett_small += setwsmall
 
# Вывод игроку информации, если была введена правильная буква.
        if setwsmall in pazzleword:
            print("Буква '" + setwsmall + "' есть в загаданном слове.")
   
# Вывод игроку информации, если была введена неправильная буква.
        else:
            print("Буквы '" + setwsmall + "' в загаданном слове нет.")
        print(knownword, len(knownword), 'букв.')
       
# Проверка составлино ли слово.
        if pazzleword == knownword:
            endtr = alltries - 1

# Ответ, если буква уже была использована.
    elif len(setw) == 1 and (setw in (alphabet_big + alphabet_small)):
        print('Введенная буква уже была испльзована. Попытка не защитана.')
   
# Восстановление количества попыток.
        tries -= 1
        endtr -= 1

# Проверка введенного слова.
    elif len(setw) == len(pazzleword):
  
# Проверка правильное ли слово.
        if setwsmall == pazzleword:
            knownword = pazzleword
            endtr = alltries - 1
        else:
            print('Введено неправильное слово.')

# Проверка нарушения правил.
    else:
        print(mistake)
   
# Восстановление количества попыток.
        endtr -= 1
        tries -= 1

# Защитывание попытки.
    tries += 1
    endtr += 1

# Вывод результата игры.

# Вывод если человек посмотрел слово.
if (pazzleword == knownword) and tries == 1:
    print('Как не стыдно!? Ты нарушил главное правило! Играть в радость!')
  
# Вывод если слово отгадано.
elif pazzleword == knownword:
    print('Позравляю! Слово найдено! Затрачено попыток: ' + str(tries) + '.')
  
# Вывод, если была использована команда !giveup.
elif gup == 1:
    print('Вы сдались. Печально. Загаданное слово было: ' + pazzleword + '.')
  
# Вывод, если слово не было отгадано.
else:
    print('Попытки кончились. Не расстраивайся, повезет в следующий раз!')
x = input()
