#!/usr/bin/env python
# coding: utf-8


import random


# наибольший общий делитель
def greatCommonDivisor(a, b):
    while a and b:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


# Генерация больших случайных чисел

def generation(q):
    key = random.randint(min, q)
    while greatCommonDivisor(q, key) != 1:
        key = random.randint(min, q)
    return key


# Модульное возведение в степень (a ^ b) mod c

def mod_power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c


# Асимметричное шифрование

def encrypt(msg, q, h, g):
    en_msg = []
    k = generation(q)  # Закрытый ключ для отправителя
    s = mod_power(h, k, q)  # Маска
    openKey = mod_power(g, k, q)  # Открытый ключ, передается вместе с сообщением
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    print("Открытый ключ g^k(openKey): ", openKey)  # ключ, чтобы снять маску
    print("Маска g^ak: ", s)  # маска
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])  # ord() возвращает порядковый номер символа Юникода, переданного в качестве
        # аргумента
    return en_msg, openKey


# Расшифровка
def decryption(en_msg, openKey, key, q):  # на вход подаются зашифрованное сообщение, открытый ключ, закрытый ключ
    # для получателя и сгенерированное большое число
    decryption_msg = []
    h = mod_power(openKey, key, q)  # с помощью модульного возведения в степень считаем h
    for i in range(0, len(en_msg)):
        decryption_msg.append(chr(int(en_msg[i] / h)))   # Функция chr( ) возвращает строку с символом Юникода номер
        # которого равен значению аргумента. Метод append вставляет в конец исходного списка значение аргумента.
    return decryption_msg


def main():
    programEnd = False  # флаг конца программы
    while not programEnd:   # пока не конец программы
        print("Меню:\n"
              "1)Зашифровать\n"
              "2)Расшифровать\n"
              "0)Выйти")
        chose = input()  # принимаем выбор пользователя
        if chose == '1':
            print("Введите желаемую длину ключа.")
            global DigitalCount, min, max
            DigitalCount = int(input())  # длина для генерируемого большого числа
            min = 10 ** (DigitalCount - 1)
            max = 10 ** DigitalCount
            print("Введите сообщение.")
            msg = input()
            print("Исходное сообщение:", msg)
            q = random.randint(min, max)  # Большое случайное число используется для генерации ключей из диапазона [
            # min;max]
            g = random.randint(2, q)   # Большое случайное число из диапазона [2, q]
            key = generation(q)  # Закрытый ключ для получателя
            h = mod_power(g, key, q)  # вычисляем h для маски
            print("Большое случайное число q: ", q)
            print("Закрытый ключ для получателя - key: ", key)
            print("Большое случайное число g: ", g)
            print("Маска g^a: ", h)
            encrypted_msg, openKey = encrypt(msg, q, h, g)
            print("Зашифрованное сообщение:", encrypted_msg)
        elif chose == '2':
            chosenDecryptMsgInput = False
            while not chosenDecryptMsgInput:
                print("Зашфированное сообщение:\n"
                      "1)Последнее сообщение\n"
                      "2)Ввести с клавиатуры")
                decryptMsgInput = input()
                if decryptMsgInput == '1':
                    msg_to_decrypt = encrypted_msg
                    chosenDecryptMsgInput = True
                elif decryptMsgInput == '2':
                    print("Введите сообщение.")
                    msgFromKeyboard = input().split()
                    msg_to_decrypt = []
                    for i in msgFromKeyboard:
                        msg_to_decrypt.append(int(i))
                    chosenDecryptMsgInput = True
                else:
                    print("Ошибка ввода\n")
            chosenDecryptParamInput = False
            while not chosenDecryptParamInput:
                print("Параметры расшифровки:\n"
                      "1)Последнее сообщение\n"
                      "2)Ввести с клавиатуры")
                decryptParamInput = input()
                if decryptParamInput == '1':
                    inputOpenKey = openKey
                    inputKey = key
                    inputQ = q
                    chosenDecryptParamInput = True
                elif decryptParamInput == '2':
                    print("Введите открытый ключ.")
                    inputOpenKey = int(input())
                    print("Введите сессионый ключ.")
                    inputKey = int(input())
                    print("Введите число Q.")
                    inputQ = int(input())
                    chosenDecryptParamInput = True
                else:
                    print("Ошибка ввода\n")

            decryptedmsg = ''.join(decryption(msg_to_decrypt, inputOpenKey, inputKey, inputQ))
            print("Расшифрованное сообщение:", decryptedmsg)
        elif chose == '0':
            programEnd = True
        else:
            print("Ошибка ввода\n")


if __name__ == '__main__':
    main()
