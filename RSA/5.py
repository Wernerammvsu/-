import codecs
message_text = 0
# сохраняет в себе количество символов файла
# count_text
# хэш-образ электронной подписи
# hash_message
# электронная подпись
# electronic_signature
# сохраняет в себе сумму кодов ASCII символов файла для проверки электронной подписи
check_message_text = 0
# сохраняет в себе количество символов файла для проверки электронной подписи
# check_count_text
# хэш-образ проверяемой электронной подписи
# check_hash_message
# электронная подпись для проверки
# check_electronic_signature
# переменные для работы с данными
print('Введите значение открытого ключа е')
open_key_e = int(input())
print('Введите значение открытого ключа n')
open_key_n = int(input())
print('Введите значение закрытого ключа d')
close_key_d = int(input())
f = codecs.open('message.txt',  encoding='utf-8')
text_message = f.read()
count_text = len(text_message)
# сохраняет в себе сумму кодов ASCII символов файла
if (open_key_e > 0) and (open_key_n > 0) and (close_key_d > 0) and (count_text > 0):
    for i in range(count_text):
        message_text = message_text + ord(text_message[i])
    # сохраняет в себе количество символов файла
    print('Сумма кодов символов, полученного сообщения: ', message_text)
    hash_message = (message_text // count_text) % 4
    print('Хэш-образ: ', hash_message)
    electronic_signature = (pow(hash_message, close_key_d)) % open_key_n
    print('Электронная подпись файла отправителя: ', electronic_signature)

    f_1 = codecs.open('message_check.txt',  encoding='utf-8')
    text_check_message = f_1.read()
    check_count_text = len(text_check_message)
    if check_count_text > 0:
        for i in range(check_count_text):
            check_message_text = check_message_text + ord(text_check_message[i])
        print('Сумма кодов символов, полученного сообщения для проверки: ', check_message_text)
        check_hash_message = (check_message_text // check_count_text) % 4
        print('Хэш-образ полученного сообщения: ', check_hash_message)
        check_electronic_signature = (pow(electronic_signature, open_key_e)) % open_key_n
        print('Хэш-образ из электронной подписи', check_electronic_signature)
        if check_hash_message == check_electronic_signature:
            print('Полученное сообщение действительно отправлено отправителем')
        else:
            print('Полученное сообщение не соответствует отправленному')
    else:
        print('Полученное сообщение пусто')
else:
    print('Значения ключей меньше либо равны нулю или сообщение пусто')