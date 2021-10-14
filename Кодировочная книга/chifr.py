def text_to_sequence(text):
    text = (text + ' ').lower()
    word_sequence = []
    word = ''
    dots = 0
    for char in text:
        if 'a' <= char <= 'z' and (word.isalpha() or word == ''):
            word += char
        elif char == '.':
            dots += 1
        elif char in (',?!-+."' + "'"):
            if word: word_sequence.append(word)
            if dots == 3:
                word_sequence.append('...')
                dots = 0
            word = char
            if word: word_sequence.append(word)
            word = ''
        else:
            if word: word_sequence.append(word)
            word = ''
            if dots == 3:
                word_sequence.append('...')
                word = ''
                dots = 0
    return word_sequence


def code(message):  # кодирование
    encrytped_msg = ''

    def sequence():
        for i in range(len(book)):
            for j in range(len(book[i])):
                yield i, j

    for word in message:
        find = False
        coded = False
        for i, j in sequence():
            if word == book[i][j][0]:
                find = True
                if not book[i][j][1]:
                    coded = True
                    encrytped_msg += str(i).rjust(3, '0') + str(j).rjust(2, '0')
                    book[i][j][1] = True
                    break
        if find and not coded:
            reset_word(word)
            for i, j in sequence():
                if word == book[i][j][0]:
                    if not book[i][j][1]:
                        encrytped_msg += str(i).rjust(3, '0') + str(j).rjust(2, '0')
                        book[i][j][1] = True
                        break
    return encrytped_msg


def decode(crypted_msg):  # декодирование
    decrypted_msg = ''
    sequence = []
    for i in range(len(crypted_msg) // 5):
        sequence.append([int(crypted_msg[5 * i:+ 5 * i + 3]), int(crypted_msg[5 * i + 3: 5 * i + 5])])
    print(sequence)
    for i in range(len(sequence)):
        if sequence[i][0] < len(book) and sequence[i][1] < len(book[sequence[i][0]]):
            row = sequence[i][0]
            column = sequence[i][1]
            decrypted_msg += book[row][column][0] + ' '
        else:
            return -1
    if len(crypted_msg) % 5 != 0:
        decrypted_msg += "\nчасть текста утеряна"
    return decrypted_msg


name = "book.txt"
file = open(name, 'r')
book = []


def reset_book():
    for line in book:
        for word in line:
            word[1] = False


def reset_word(wordReset):
    for line in book:
        for word in line:
            if wordReset == word[0]:
                word[1] = False


words = [text_to_sequence(line) for line in file]
for line in words:
    book.append([[i, False] for i in line])
file.close()
#print(book)
# ----------------------------------------
# ------------начало программы------------
# ----------------------------------------
prog_end = False  # флаг завершения программы
while not prog_end:  # пока программу не закрыли
    print('Меню:\n'
          '1) Кодирование.\n'
          '2) Декодирование.\n'
          '0) Выход.')  # вывод меню
    choice = input()  # ввод выбора
    if choice == '1':  # Кодирование
        print('Введите сообщение.')
        input_msg = input()
        f = open('messageInPut.txt', 'w')  # запись в файл
        f.write(input_msg)
        f.close()
        input_msg_sqnce = text_to_sequence(input_msg)
        msg_encrypted = code(input_msg_sqnce)
        f = open('messageToSend.txt', 'w')  # запись в файл
        f.write(msg_encrypted)
        f.close()
    elif choice == '2':  # Декодирование
        decode_end = False  # флаг конца декодирования
        while not decode_end:
            print('Выберите метод ввода:\n'
                  '1)Ввод с клавиатуры.\n'
                  '2)Считать из файла.')  # ввывод меню (уточнение про ввод сообщения: набор на
            choice_method = input()  # клавиатуре, либо подгрузка с файла)
            if choice_method == '1':  # ручной ввод
                print('Введите сообщение.')
                msg_encrypted = input()
                f = open('messageToSend.txt', 'w')  # запись в файл
                f.write(msg_encrypted)
                f.close()  # считываение собщения
                msg_decrypted = decode(msg_encrypted)  # Декодирование
                if msg_decrypted != -1:
                    print(msg_decrypted)
                    f = open('messageDecrypted.txt', 'w')
                    f.write(msg_decrypted)
                    f.close()
                else:
                    print('Cлова с таким номером нет.')
                    decode_end = True  # переключение флага, для завершения Декодирования
            elif choice_method == '2':  # подгрузка с файла
                f = open('messageToSend.txt', 'r')  # открытие файла
                msg_encrypted = f.read()  # считывание текста
                f.close()
                msg_decrypted = decode(msg_encrypted)  # Декодирование
                if msg_decrypted != -1:
                    print(msg_decrypted)
                    f = open('messageDecrypted.txt', 'w')
                    f.write(msg_decrypted)
                    f.close()
                else:
                    print('Cлова с таким номером нет.')
                    decode_end = True  # переключение флага, для завершения декодирования
            else:
                print('Сделайте корректный выбор.\n')  # сообщение о не правильном выборе
    elif choice == '0':  # завершение программы
        prog_end = True
    else:
        print('Сделайте корректный выбор.\n')
