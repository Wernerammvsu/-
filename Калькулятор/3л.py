from math import gcd


def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "Число не простое.")
                return False
            else:
                print(num, "Простое число.")
                return True
    else:
        print(num, "Число не простое.")
        return False


def add(x, y, mod):
    return (x + y) % mod


def subtract(x, y, mod):
    return (x - y) % mod


def multiply(x, y, mod):
    return ((x % mod) * (y % mod)) % mod


def divide(x, y, mod):
    if isPrime(mod):
        return int(((x % mod) / (y % mod)) % mod)
    else:
        print("Невозможно.")
        return None


def power(a, b, mod):
    return ((a % mod) ** (b % mod)) % mod


def mod_inv(y, mod):
    if gcd(y, mod) == 1:
        totient = 0
        for k in range(1, mod + 1):
            if gcd(mod, k) == 1:
                totient += 1
        return y ** (totient - 1) % mod
    else:
        print("Инверсия невозможна")
        return None


def squareRoot(n, mod):
    n = n % mod
    res = []
    for x in range(-mod, mod):
        if (x * x) % mod == n:
            res.append(x)
            print("Квадратный корень равен ", x)
    if len(res) == 0:
        print("Не существует.")


def QuadResidue(a, mod):
    QR = 0
    for b in range(1, ((mod - 1) // 2) + 1):
        if (b ** 2) % mod == a:
            QR = 1

    if QR == 1:
        print("{} является квадратичным вычетом {}".format(a, mod))
    else:
        print("{} является квадратичным невычетом {}".format(a, mod))


program_end = False
while not program_end:
    print("1) Сложение.")
    print("2) Вычитание.")
    print("3) Умножение.")
    print("4) Деление.")
    print("5) Степень.")
    print("6) Корень.")
    print("7) Модульная инверсия.")
    print("8) Квадратичный вычет.")
    print("0) Выход.")

    choice = input()
    if choice == '0':
        program_end = True
        print('Выход.')
        break
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        num1 = int(input("Введите первое число.\n"))

        if choice == '1':
            num2 = int(input("Введите второе число.\n"))
            m = int(input("Введите mod.\n"))
            print(num1, "+", num2, "=", add(num1, num2, m), " mod ", m)

        elif choice == '2':
            num2 = int(input("Введите второе число.\n "))
            m = int(input("Введите mod.\n"))
            print(num1, "-", num2, "=",
                  subtract(num1, num2, m), " mod ", m)

        elif choice == '3':
            num2 = int(input("Введите второе число.\n"))
            m = int(input("Введите mod.\n"))
            print(num1, "*", num2, "=",
                  multiply(num1, num2, m), " mod ", m)

        elif choice == '4':
            num2 = int(input("Введите второе число.\n"))
            m = int(input("Введите mod.\n"))
            print(num1, "/", num2, "=",
                  divide(num1, num2, m), " mod ", m)
        elif choice == '5':
            num2 = int(input("Введите второе число: \n"))
            m = int(input("Введите mod:\n"))
            print(num1, "^", num2, "=",
                  power(num1, num2, m), "mod", m)
        elif choice == '6':
            m = int(input("Введите mod.\n"))
            squareRoot(num1, m)
        elif choice == '7':
            m = int(input("Введите mod.\n"))
            print("Инверсия", mod_inv(num1, m), " mod ", m)
        elif choice == '8':
            m = int(input("Введите mod.\n"))
            QuadResidue(num1, m)
    else:
        print("Неверный ввод.\n")
