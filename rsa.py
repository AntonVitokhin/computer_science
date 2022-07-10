def is_prime(num):  # Проверка на простое число.
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def gcd(num1, num2):  # НОД.
    if num1 == 0 or num2 == 0:
        return num1 + num2

    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1

    return num1 + num2


def check_e(num):  # Проверка числа е. Простое, меньше функции Эйлера, взаимно простое с функцией Эйлера.
    condition1 = is_prime(num)
    condition2 = num < eulerFun
    condition3 = gcd(num, eulerFun) == 1

    return condition1 and condition2 and condition3