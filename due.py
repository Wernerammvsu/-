def encode():
    print('Введите текст:')
    text_to_encode = str(input())  # преобразование введённого текста в строку
    length = len(text_to_encode)  # вычисляем длину строки
    rows = int(length ** (1 / 2))  # делаем целое число столбцов корень из длины строки
    strings = int(length / rows)  # разбиваем на целое число строк
    size = rows * strings  # вычисляем размер матрицы
    if size < length:  # проверяем соответствие размерности матрицы и длины строки
        strings += 1  # добавляем 1 строку для того, чтоб матрица могла вместить всю строку
    print('Число стобцов:', rows, ', Число строк:', strings)
    print('Ввод последовательности для кодирования строк перестановкой:')
    sequence_strings_encode = [int(x) for x in
                               input().split()]  # split извлекает часть строки до разделителя, если разделитель не
    # задан, то разделителем считается
    # пробел или новая строка
    print('Введите последовательность для кодирования столбцов:')
    sequence_rows_encode = [int(x) for x in input().split()]
    if set(sequence_strings_encode) == set([x + 1 for x in range(strings)]) and set(sequence_rows_encode) == set(
            [x + 1 for x in range(rows)]):  # set создаёт множество
        dictionary = dict()  # создание словаря
        copy_text = text_to_encode  # работаем с копией введённого текста
        for i in sequence_strings_encode:  # с помощью срезов переставляем
            lst = copy_text[:rows]
            dictionary[lst] = i
            copy_text = copy_text[rows:]
        new_text = sorted(dictionary.items(), key=lambda x: (x[1], x[0]))  # sorted сохраняет новые элементы в
        # качестве копии
        new_text = dict(new_text)  # делаем словарь
        print(new_text)  # печатаем новый текст
        s = []  # создание массива
        for j in sequence_rows_encode:
            for array in new_text:
                if len(array) < len(sequence_rows_encode):
                    add_string = '_' * (len(sequence_rows_encode) - len(array))
                    array = array + add_string
                s.append(array[j - 1])
        with open('code.txt', 'w') as f:
            for i in s:
                f.write(i)
        return s, sequence_strings_encode, sequence_rows_encode
    else:
        print('Это неправильно')
        raise NotImplementedError


def decode():
    global new_string
    try:
        with open('code.txt', 'r') as f:   # запись в файл
            new_string = f.read()
            print(new_string)
    except:
        print('Файл повреждён')

    else:
        print('Введите последовательность для декодирования строк:')
    sequence_strings_decode = [int(x) for x in input().split()]
    print('Введите последовательность для декодирования столбцов:')
    sequence_rows_decode = [int(x) for x in input().split()]
    if sequence_strings_decode != sequence_strings or sequence_rows_decode != sequence_rows:
        print('Это неправильно')
        raise NotImplementedError
    else:
        dictionary_encode = dict()
        for i in sequence_rows_decode:
            lst = new_string[:len(sequence_strings_decode)]
            dictionary_encode[lst] = i
            new_string = new_string[len(sequence_strings_decode):]
        new = sorted(dictionary_encode.items(), key=lambda x: (x[1], x[0]))
        new = dict(new)
        s = []
        for j in sequence_strings_decode:
            for line in new.keys():
                try:
                    s.append(line[j - 1])
                except IndexError:
                    print(
                        'Так как файл был преобразован, данная последовательность не может быть расшифрована правильно')

        string = ''.join(map(str, s))  # join соединяет элементы, map применяет функцию ко всем элементам списка
        s = string.replace('_', '')  # возвращает копию строки, в которой вхождение старой подстроки будет заменено
        # новой подстрокой
        with open('code.txt', 'w') as f:    # перезапись файла
            for i in s:
                f.write(i)
        return s


# точка входа. Если импортировать этот файл, код далее исполняться не будет
if __name__ == '__main__':

    try:
        code = encode()
    except NotImplementedError:
        print('Список перестановок не отвечает последовательности')
    else:
        message, sequence_strings, sequence_rows = code[0], code[1], code[2]
        print(message)
    k = input()
    try:
        code = decode()
    except NotImplementedError:
        print('Список перестановок не отвечает последовательности')
    else:
        print(code)
