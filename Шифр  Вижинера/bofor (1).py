"""
ПРОГРАММА ИСПОЛЬЗУЕТ ДЛЯ ШИФРОВАНИЯ ЛАТИНСКИЙ АЛФАВИТ, БУКВЫ МОЖНО ВВОДИТЬ В ЛЮБОМ РЕГИСТРЕ ОНИ
АВТОМАТИЧЕСКИ ПЕРЕВЕДУТСЯ В ВЕРХНИЙ РЕГИСТР.
Сложение
вычитание
умножение
возведение в степень
поиск обратного(мультипликативное(умножить два числа и сравнимы с нулём по модулю) и аддитивное)
- ессли обратного нет выдать сообщение
квадратичный вычет(не вычет)
найти квадратный корень
"""

save_non_letter_sign = True

"""
ЭТОТ ФЛАГ ОТВЕЧАЕТ ЗА ПРОБЕЛЫ И ПРОЧЕЕ, ЕСЛИ ОН [True], ТО ВСЁ ЧТО ВНЕ АЛФАВИТА
НЕ БУДЕТ ОБРАБАТЫВАТЬСЯ, ИНАЧЕ ВСЕ ПРОБЕЛЫ И ДРУГИЕ СИМВОЛЫ БУДУТ СМЕЩАТЬСЯ В АЛФАВИТ
И ТЕРЯТЬСЯ ПРИ ДЕКОДИРОВАНИИ
"""

def code(send_msg):
    send_msg = send_msg.upper()         # считывание сообщения
    send_msg_len = len(send_msg)            # длина сообщения
    print('input KEYWORD please.')
    key_word = str(input()).upper()         # считывание ключ слова
    key_word_len = len(key_word)            # длина ключ слова
    key_sequence = ''               #создание ключа
    for i in range(send_msg_len):                           # дополнение ключевого слова до ключевой последовательности
        key_sequence += key_word[i % key_word_len]          # цикла из ключевых слов длинной равной сообщению
    #print(key_sequence)

    encrypted_message = ''  #создание зашифрованного сообщения
    if save_non_letter_sign == True:                        # Проверка функции сохранения знаков
        for i in range(send_msg_len):                       # цикл по сообщению
            if send_msg[i] >= 'A' and send_msg[i] <= 'Z':   # проверка символа на принадлежность алфавиту и смещение символа по ключу
                encrypted_message += chr((ord(key_sequence[i]) - ord(send_msg[i]) - 2 * ord('A')) % 26 + ord('A'))
            else:
                encrypted_message += send_msg[i]            # запись не алфавитного символа
    else:
        for i in range(send_msg_len):                       # смещение символа по ключу
            encrypted_message += chr((ord(key_sequence[i]) - ord(send_msg[i]) - 2 * ord('A')) % 26 + ord ('A'))
    print(encrypted_message)
    return encrypted_message

def encode(encrypted_message): #Дешифрование
    get_msg = encrypted_message.upper()             # полученное сообщение
    get_msg_len = len(get_msg)              # и его длина

    print('input KEYWORD please.')
    key_word = str(input()).upper()             # ключ слово
    key_word_len = len(key_word)                # и его длина
    key_sequence = '' #создание ключа
    for i in range(get_msg_len):
        key_sequence += key_word[i % key_word_len]
    #print(key_sequence)


    decrypted_message = ''  #дешифрованное сообщение
    if save_non_letter_sign == True:                        # проверка функции сохранения знаков
        for i in range(get_msg_len):                        # цикл по сообщению
            if get_msg[i] >= 'A' and get_msg[i] <= 'Z':     # проверка символа на принадлежность алфавиту и смещение символа по ключу
                decrypted_message += chr((ord(key_sequence[i]) - ord(get_msg[i]) - 2 * ord('A')) % 26 + ord('A'))
            else:
                decrypted_message += get_msg[i]             #запись не алфавитного символа
    else:
        for i in range(get_msg_len):                        #смещение символа по ключу
            decrypted_message += chr((ord(key_sequence[i]) - ord(get_msg[i]) - 2 * ord('A')) % 26 + ord ('A'))
    #print(decrypted_message)
    return decrypted_message

#----------------------------------------
#------------начало программы------------
#----------------------------------------

prog_end = False                                # флаг завершения программы
while not prog_end:                             # пока программу не закрыли
    print('chose one of actions bellow:\n'  
          '1) code your message\n'
          '2) decode message\n'
          '0) exit')                            # вывод меню
    choice = input()                            # ввод выбора
    if choice == '1':       #шифрование
        print('text your message please.')
        input_msg = str(input())
        f = open('messageInPut.txt','w')       # запись в файл
        f.write(input_msg)
        f.close()
        msg_encrypted = code(input_msg)
        f = open('messageToSend.txt','w')       # запись в файл
        f.write(msg_encrypted)
        f.close()
    elif choice == '2':     #дешифровка
        decode_end = False                      # флаг конца дешифровки
        while not decode_end:
            print('chose method of input message\n'
                  '1)manual by keyboard\n'
                  '2)load from file')                       # ввывод меню (уточнение про ввод сообщения: набор на
            choice_method = input()                         # клавиатуре, либо подгрузка с файла)
            if choice_method == '1':    #ручной ввод
                print('please text your message')
                msg_encrypted = input()
                f = open('messageToSend.txt','w')       # запись в файл
                f.write(msg_encrypted)
                f.close()                   # считываение собщения
                msg_decrypted = encode(msg_encrypted)                 # дешифровка
                print(msg_decrypted)
                f = open('messageDecrypted.txt','w')       # запись в файл
                f.write(msg_decrypted)
                f.close()
                decode_end = True                           # переключение флага, для завершения дешифровки
            elif choice_method == '2': #подгрузка с файла
                f = open('messageToSend.txt','r')           # открытие файла
                msg_encrypted = f.read()                    # считывание текста
                f.close()
                msg_decrypted = encode(msg_encrypted)       # дешифровка
                print(msg_decrypted)
                f = open('messageDecrypted.txt','w')        # запись в файл
                f.write(msg_decrypted)
                f.close()
                decode_end = True                           # переключение флага, для завершения дешифровки
            else:
                print('please make a corect choise\n')        # сообщение о не правильном выборе
    elif choice == '0':     #завершение программы
        prog_end = True
    else:
        print('please make a corect choise\n')            # сообщение о не правильном выборе