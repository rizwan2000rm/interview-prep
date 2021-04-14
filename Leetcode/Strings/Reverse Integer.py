def reverse(x):
    rev = 0

    if x > 0:
        sign = 1
    else:
        sign = -1
        x = -x

    while x:
        rev = rev * 10 + x % 10
        x //= 10

    if rev > pow(2, 31):
        return 0
    else:
        return rev * sign
