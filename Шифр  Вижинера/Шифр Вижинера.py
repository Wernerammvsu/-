"""
ПРОГРАММА ИСПОЛЬЗУЕТ ДЛЯ ШИФРОВАНИЯ ЛАТИНСКИЙ АЛФАВИТ, БУКВЫ МОЖНО ВВОДИТЬ В ЛЮБОМ РЕГИСТРЕ ОНИ
АВТОМАТИЧЕСКИ ПЕРЕВЕДУТСЯ В ВЕРХНИЙ РЕГИСТР.
"""

save_non_letter_sign = True

"""
ЭТОТ ФЛАГ ОТВЕЧАЕТ ЗА ПРОБЕЛЫ И ПРОЧЕЕ, ЕСЛИ ОН [True], ТО ВСЁ ЧТО ВНЕ АЛФАВИТА
НЕ БУДЕТ ОБРАБАТЫВАТЬСЯ, ИНАЧЕ ВСЕ ПРОБЕЛЫ И ДРУГИЕ СИМВОЛЫ БУДУТ СМЕЩАТЬСЯ В АЛФАВИТ
И ТЕРЯТЬСЯ ПРИ ДЕКОДИРОВАНИИ
"""


def code():
    print('Введитет текст.')
    send_msg = str(input()).upper()  # считывание сообщения
    send_msg_len = len(send_msg)  # длина сообщения
    print('Введите ключ.')
    key_word = str(input()).upper()  # считывание ключ слова
    key_word_len = len(key_word)  # длина ключ слова
    key_sequence = ''  # создание ключа
    for i in range(send_msg_len):  # дополнение ключевого слова до ключевой последовательности
        key_sequence += key_word[i % key_word_len]  # цикла из ключевых слов длинной равной сообщению
    # print(key_sequence)

    encrypted_message = ''  # создание зашифрованного сообщения
    if save_non_letter_sign == True:  # Проверка функции сохранения знаков
        for i in range(send_msg_len):  # цикл по сообщению
            if send_msg[i] >= 'A' and send_msg[
                i] <= 'Z':  # проверка символа на принадлежность алфавиту и смещение символа по ключу
                encrypted_message += chr((ord(send_msg[i]) + ord(key_sequence[i]) - 2 * ord('A')) % 26 + ord('A'))
            else:
                encrypted_message += send_msg[i]  # запись не алфавитного символа
    else:
        for i in range(send_msg_len):  # смещение символа по ключу
            encrypted_message += chr((ord(send_msg[i]) + ord(key_sequence[i]) - 2 * ord('A')) % 26 + ord('A'))
    print(encrypted_message)
    with open('text.txt', 'w') as f:  # перезапись файла
        for i in encrypted_message:
            f.write(i)
    return encrypted_message


def encode(encrypted_message):  # Расшифровка
    get_msg = encrypted_message.upper()  # полученное сообщение
    get_msg_len = len(get_msg)  # и его длина
    print(encrypted_message)
    print('Введите ключ.')
    key_word = str(input()).upper()  # ключ слово
    key_word_len = len(key_word)  # и его длина
    key_sequence = ''  # создание ключа
    for i in range(get_msg_len):
        key_sequence += key_word[i % key_word_len]
    # print(key_sequence)

    decrypted_message = ''  # расшифрованное сообщение
    if save_non_letter_sign == True:  # проверка функции сохранения знаков
        for i in range(get_msg_len):  # цикл по сообщению
            if get_msg[i] >= 'A' and get_msg[
                i] <= 'Z':  # проверка символа на принадлежность алфавиту и смещение символа по ключу
                decrypted_message += chr((ord(get_msg[i]) - ord(key_sequence[i]) - 2 * ord('A') + 26) % 26 + ord('A'))
            else:
                decrypted_message += get_msg[i]  # запись не алфавитного символа
    else:
        for i in range(get_msg_len):  # смещение символа по ключу
            decrypted_message += chr((ord(get_msg[i]) - ord(key_sequence[i]) - 2 * ord('A') + 26) % 26 + ord('A'))
    # print(decrypted_message)
    with open('text.txt', 'w') as f:  # перезапись файла
        for i in decrypted_message:
            f.write(i)
    return decrypted_message


# ----------------------------------------
# ------------начало программы------------
# ----------------------------------------

prog_end = False  # флаг завершения программы
while not prog_end:  # пока программу не закрыли
    print('*******Меню********\n'
          '1) Шифрование.\n'
          '2) Расшифровка.\n'
          '0) Выход.')  # вывод меню
    choice = input()  # ввод выбора
    if choice == '1':  # шифрование
        msg_encrypted = code()
        f = open('text.txt', 'w')  # запись в файл
        f.write(msg_encrypted)
        f.close()
    elif choice == '2':  # расшифровка
        decode_end = False  # флаг конца расшифровки
        while not decode_end:
            print('Выберите один из предложенных вариантов:\n'
                  '1)Ввод с клавиатуры.\n'
                  '2)Загрузка из файла.')  # ввывод меню (уточнение про ввод сообщения: набор на
            choice_method = input()  # клавиатуре, либо подгрузка с файла)
            if choice_method == '1':  # ручной ввод
                print('Введите текст сообщения')
                msg_encrypted = input()  # считываение собщения
                with open('text.txt', 'w') as f:  # перезапись файла
                    for i in msg_encrypted:
                        f.write(i)
                msg_decrypted = encode(msg_encrypted)  # расшифровка
                print(msg_decrypted)  # печать сообщения
                decode_end = True  # переключение флага, для завершения дешифровки
            elif choice_method == '2':  # подгрузка с файла
                f = open('text.txt', 'r')  # открытие файла
                msg_encrypted = f.read()  # считывание текста
                f.close()
                msg_decrypted = encode(msg_encrypted)  # расшифровка
                print(msg_decrypted)  # печать сообщения
                decode_end = True  # переключение флага, для завершения дешифровки
            else:
                print('Некорректный выбор.')  # сообщение о не правильном выборе
    elif choice == '0':  # завершение программы
        prog_end = True
    else:
        print('Некорректный выбор.')  # сообщение о не правильном выборе
