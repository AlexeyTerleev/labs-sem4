

def get_binary(x: int) -> list:
    lst, sign = [], 0

    if x < 0:
        x *= -1
        sign = 1

    while x > 0:
        lst.append(x % 2)
        x = x // 2
    while len(lst) < 15:
        lst.append(0)
    lst.append(sign)

    return lst[::-1]


def binary2addition_binary(lst: list) -> list:

    if not lst[0]:
        return lst.copy()

    out = [lst[0]]

    for i in range(1, len(lst)):
        out.append(0) if lst[i] else out.append(1)
    if lst[0]:
        out = addition(out, get_binary(1))

    return out


def binary2reverse_binary(lst: list) -> list:

    if not lst[0]:
        return lst.copy()

    out = [int(not x) for x in lst]
    out[0] = int(not out[0])
    return out


def get_reverse_binary(x: int) -> list:
    return binary2reverse_binary(get_binary(x))


def get_addition_binary(x: int) -> list:
    return binary2addition_binary(get_binary(x))


def addition_binary2reverse_binary(lst: list) -> list:

    if not lst[0]:
        return lst.copy()

    return addition(lst, [1 for x in range(16)]) if lst[0] else lst.copy()


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


def mult(a: list, b: list) -> list:
    out = get_binary(0)

    flag = (a[0] == b[0])
    a[0], b[0] = 0, 0

    while b != get_binary(0):
        out = addition(a, out)
        b = addition(b, [1 for x in range(16)])

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


def sum_bin(a: list, b: list) -> list:
    out = addition(binary2addition_binary(a), binary2addition_binary(b))
    return reverse_binary2binary(addition_binary2reverse_binary(out))


def get_binary_float(x: float) -> list:
    #10^38
    sign = 0
    if x < 0:
        x *= -1
        sign = 1

    mantissa = int(''.join(str(x).split(".")))
    exp = abs(str(x).find('.') - len(str(x))) - 1

    lst_mantissa = []
    while mantissa > 0:
        lst_mantissa.append(mantissa % 2)
        mantissa = mantissa // 2
    while len(lst_mantissa) < 23:
        lst_mantissa.append(0)

    lst_exp = []
    while exp > 0:
        lst_exp.append(exp % 2)
        exp = exp // 2
    while len(lst_exp) < 8:
        lst_exp.append(0)

    return (lst_mantissa + lst_exp + [sign])[::-1]


'''    
def float_addition(a: Float, b: Float):

    if more_or_equal(b.ind, a.ind):
        a, b = b, a
    delta = sum_bin(a.ind, mult(b.ind, get_binary(-1)))
    delta[0] = 0

    while delta != get_binary(0):

        a.ind = sum_bin(a.ind, get_binary(-1))
        a.mantissa = mult(a.mantissa, get_binary(10))

        delta = sum_bin(delta, get_binary(-1))

    out = Float(mantissa=addition(a.mantissa, b.mantissa), ind=a.ind)

    print(f'{"".join(str(x) for x in out.mantissa)} * 2 ^ {"".join(str(x) for x in out.ind)}')
    print(f'{binary2int(out.mantissa)} * 10 ^ {binary2int(out.ind)}')
'''


def binary2int(lst: list) -> int:
    num = 0

    for i in range(len(lst), 1, -1):
        num += pow(2, (len(lst) - i)) * lst[i - 1]

    return num if not lst[0] else -num


def binary_float2float(x: list) -> float:
    sign = x[0]
    exp = x[1:9]
    mantissa = x[9:]
    s = str(binary2int(mantissa))
    out = float(s[:-binary2int(exp)] + '.' + s[-binary2int(exp):])
    return out if not sign else -out


def test(x: list):
    # x = (1 - 2*sign)(1 + mantissa) * 2^(exp - p) ?? p
    sign = x[0]
    exp = binary2int(x[1:9])
    mantissa = x[9:]
    out = (1 - 2 * sign) * binary2int(addition(mantissa, [0 for x in range(22)] + [1])) * pow(10, exp - 8)
    print(out)


def main():
    x, y = 5, 4 #4, 5 //1056

    print(binary_float2float(get_binary_float(-10.2345)))
    test(get_binary_float(-10.2345))
    '''float_addition(Float(mantissa=get_binary(x), ind=get_binary(-1)),
                   Float(mantissa=get_binary(y), ind=get_binary(-2)))'''


if __name__ == '__main__':
    main()
