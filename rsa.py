def gcd(num1, num2):  # НОД.
    if num1 == 0 or num2 == 0:
        return num1 + num2

    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1

    return num1 + num2