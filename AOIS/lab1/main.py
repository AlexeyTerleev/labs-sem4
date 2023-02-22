def get_binary(x: int, length: int = 16) -> list:
    lst, sign = [], 0

    if x < 0:
        x *= -1
        sign = 1

    while x > 0:
        lst.append(x % 2)
        x = x // 2
    while len(lst) < length - 1:
        lst.append(0)
    lst.append(sign)

    return lst[::-1]


def binary2addition_binary(lst: list, length: int = 16) -> list:
    if not lst[0]:
        return lst.copy()

    out = [lst[0]]

    for i in range(1, len(lst)):
        out.append(0) if lst[i] else out.append(1)

    out = addition(out, get_binary(1, length))

    return out


def binary2reverse_binary(lst: list) -> list:
    if not lst[0]:
        return lst.copy()

    out = [int(not x) for x in lst]
    out[0] = int(not out[0])
    return out


def get_reverse_binary(x: int, length: int = 16) -> list:
    return binary2reverse_binary(get_binary(x, length))


def get_addition_binary(x: int, length: int = 16) -> list:
    return binary2addition_binary(get_binary(x, length), length)


def addition_binary2reverse_binary(lst: list, length: int = 16) -> list:
    if not lst[0]:
        return lst.copy()

    return addition(lst, [1 for x in range(length)]) if lst[0] else lst.copy()


def reverse_binary2binary(lst: list) -> list:
    return binary2reverse_binary(lst)


def addition(a: list, b: list) -> list:
    out, flag = [], False

    for i in range(len(a), 0, -1):
        if (not a[i - 1] and not b[i - 1] and not flag) or \
                (((a[i - 1] and not b[i - 1]) or (not a[i - 1] and b[i - 1])) and flag):
            out.append(0)
        elif (a[i - 1] and b[i - 1] and flag) or \
                (((a[i - 1] and not b[i - 1]) or (not a[i - 1] and b[i - 1])) and not flag):
            out.append(1)
        elif (not a[i - 1] and not b[i - 1] and flag) or (a[i - 1] and b[i - 1] and not flag):
            out.append(int(flag))
            flag = not flag

    return out[::-1]


def more_or_equal(a: list, b: list) -> bool:
    if a[0] != b[0]:
        return not a[0]

    for i in range(1, len(a)):
        if a[i] != b[i]:
            return a[i]
    return True


def mult(a: list, b: list, length: int = 16) -> list:
    out = get_binary(0, length)

    flag = (a[0] == b[0])
    a[0], b[0] = 0, 0

    while b != get_binary(0, length):
        out = addition(a, out)
        b = addition(b, [1 for x in range(length)])

    out[0] = 0 if flag else 1

    return out


def division(a: list, b: list) -> list:
    out = get_binary(0)

    flag = (a[0] == b[0])
    a[0], b[0] = 0, 0

    while more_or_equal(a, b):
        b[0] = 1
        a = addition(a, binary2addition_binary(b))
        out = addition(out, get_binary(1))
        b[0] = 0

    return [0] + out if flag else [1] + out


def sum_bin(a: list, b: list, length: int = 16) -> list:
    out = addition(binary2addition_binary(a, length), binary2addition_binary(b, length))
    return reverse_binary2binary(addition_binary2reverse_binary(out, length))


def get_binary_float(x: float) -> list:
    sign = 0
    if x < 0:
        x *= -1
        sign = 1

    mantissa = int(''.join(str(x).split(".")))
    if mantissa % 10 == 0:
        mantissa //= 10

    if int(x) == x:
        exp = 0
    else:
        exp = str(x).find('.') - (len(str(x)) - 1)

    lst_mantissa = []
    while mantissa > 0:
        lst_mantissa.append(mantissa % 2)
        mantissa = mantissa // 2
    while len(lst_mantissa) < 23:
        lst_mantissa.append(0)

    lst_exp = get_binary(exp, 8)

    return (lst_mantissa + lst_exp[::-1] + [sign])[::-1]


#-2.55, 3. => -255 * 10 ^ -2, 3 * 10 ^ 1 => -255 * 10 ^ -2, 300 * 10 ^ -2
def float_addition(a: list, b: list):

    if more_or_equal(b[1:9], a[1:9]):
        a, b = b, a

    while a[1:9] != b[1:9]:

        a[1:9] = sum_bin(a[1:9], get_binary(-1, 8), 8)
        a[9:] = mult(a[9:], get_binary(10, 23), 23)

    out = sum_bin([a[0]] + a[9:], [b[0]] + b[9:], 24)
    return [out[0]] + a[1:9] + out[9:]


def binary2int(lst: list) -> int:
    num = 0

    for i in range(len(lst), 1, -1):
        num += pow(2, (len(lst) - i)) * lst[i - 1]

    return num if not lst[0] else -num


def binary_float2float(x: list):
    return (1 - 2 * x[0]) * binary2int(x[9:]) * pow(10, binary2int(sum_bin(x[1:9], get_binary(127), 8)))


def main():
    x, y = 5, 4  # 4, 5 //1056

    print(binary_float2float(float_addition(get_binary_float(2.55), get_binary_float(-3.))))
    '''float_addition(Float(mantissa=get_binary(x), ind=get_binary(-1)),
                   Float(mantissa=get_binary(y), ind=get_binary(-2)))'''


if __name__ == '__main__':
    main()
