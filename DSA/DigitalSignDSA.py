import hashlib
from random import randint as rand

global UsePrimeNumbers
UsePrimeNumbers = True


def toBinary(n):
    r = []
    while n > 0:
        r.append(n % 2)
        n = n / 2
        return r


def isPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def textToDigital(text):
    text = text.encode('utf-8')
    m = hashlib.sha1()
    m.update(text)
    message = int("0x" + m.hexdigest(), 0)
    return message


def randomPrime():
    global min, max
    common = False
    while not common:
        number = rand(min, max)
        if isPrime(number):
            common = True
    return number


def commonDividers(num, qmin):
    dividers = [1]
    for i in range(2, num // 2 + 1):
        while (num % i) == 0:
            dividers.append(i)
            num = num // i
            if i > qmin:
                return [i]
    return dividers


def generateKeys(bits=8):
    global min, max
    min = 2 ** (bits - 1)
    max = 2 ** bits
    qmin = 2 ** (int(bits / 3.2))
    p = randomPrime()
    # p = 10034911
    # p = 23
    print("p: ", p)
    divs = commonDividers(p - 1, qmin)
    q = divs[-1]
    q = int(q)
    print("q: ", q)
    h = rand(1, p - 1)
    g = pow(h, ((p - 1) // q), p)
    print("g: ", g)

    closeKey = rand(1, q)
    print("closeKey: ", closeKey)
    openKey = pow(g, closeKey, p)
    print("openKey: ", openKey)
    return g, p, q, closeKey, openKey


def generateDigitalSign(g, p, q, closeKey, message):
    r = 0
    s = 0
    while r == 0 or s == 0:
        k = rand(1, q)
        r = pow(g, k, p) % q
        kReverse = pow(k, q - 2, q)
        s = (kReverse * (message + closeKey * r)) % q
    return r, s


def checkDigitalSign(g, p, q, openKey, message, r, s):
    sReverse = pow(s, q - 2, q)
    w = sReverse
    u1 = (message * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(openKey, u2, p)) % p % q
    if v == r:
        return True
    else:
        return False


progEnd = False
message = 0
R = 0
S = 0
G, P, Q, closeKey, openKey = generateKeys(25)
while not progEnd:
    print("1) Ввести сообщение\n"
          "2) Сгенерировать подпись\n"
          "3) Проверить подпись\n"
          "9) Сгенерировать новые ключи\n"
          "0) Выход")
    chose = input()
    if chose == '1':
        print("Введите сообщение")
        text = input()
        message = textToDigital(text)
    elif chose == '2':
        if not message:
            print("Пожалуйста, сначала введите сообщение")
            text = input()
            message = textToDigital(text)
        R, S = generateDigitalSign(G, P, Q, closeKey, message)
        print("R, S:", R, S)
    elif chose == '3':
        print("1) Использовать полученную подпись\n"
              "2) Ввести подпись в ручную")
        choseRScheck = input()
        if choseRScheck == '1':
            if not R or not S:
                print("Сначала сгенерируйте подписи")
            else:
                print("Полученное сообщение: ")
                print(text)
                print("Полученная подпись: ")
                print(R, S)
                check = checkDigitalSign(G, P, Q, openKey, message, R, S)
                if check:
                    print("Подпись подлинная")
                else:
                    print("Подпись не верна")
        elif choseRScheck == '2':
            if not message:
                print("Пожалуйста, сначала введите сообщение")
                text = input()
                message = textToDigital(text)
            print("R: ")
            R = int(input())
            print("S: ")
            S = int(input())
            check = checkDigitalSign(G, P, Q, openKey, message, R, S)
            if check:
                print("Подпись подлинная")
            else:
                print("Подпись не верна")
    elif chose == '9':
        print("Укажите желаемую длину ключей в битах")
        bits = int(input())
        G, P, Q, closeKey, openKey = generateKeys(bits)
    elif chose == '0':
        progEnd = True
    else:
        print("Пожалуйста сделайте корректный выбор")
