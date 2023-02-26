import constant


def get_binary(num_int: int, length: int = constant.INT_LENGTH) -> list:
    out, sign = [], 0

    if num_int < 0:
        num_int *= -1
        sign = 1

    while num_int > 0:
        out.append(num_int % constant.BINARY_BASE)
        num_int = num_int // constant.BINARY_BASE
    while len(out) < length - 1:
        out.append(0)
    out.append(sign)

    return out[::-1]


def binary2addition_binary(num_bin: list, length: int = constant.INT_LENGTH) -> list:
    if not num_bin[0]:
        return num_bin.copy()

    out = [num_bin[0]]

    for i in range(1, len(num_bin)):
        out.append(0) if num_bin[i] else out.append(1)

    out = addition(out, get_binary(1, length))

    return out


def binary2reverse_binary(num_bin: list) -> list:
    if not num_bin[0]:
        return num_bin.copy()

    out = [int(not x) for x in num_bin]
    out[0] = int(not out[0])
    return out


def get_reverse_binary(num_int: int, length: int = constant.INT_LENGTH) -> list:
    return binary2reverse_binary(get_binary(num_int, length))


def get_addition_binary(num_int: int, length: int = constant.INT_LENGTH) -> list:
    return binary2addition_binary(get_binary(num_int, length), length)


def addition_binary2reverse_binary(num_addition_bin: list, length: int = constant.INT_LENGTH) -> list:
    if not num_addition_bin[0]:
        return num_addition_bin.copy()

    return addition(num_addition_bin, [1] * length) if num_addition_bin[0] else num_addition_bin.copy()


def reverse_binary2binary(num_reverse_bin: list) -> list:
    return binary2reverse_binary(num_reverse_bin)


def addition(first: list, second: list) -> list:
    out, flag = [], False

    for i in range(len(first), 0, -1):
        if (not first[i - 1] and not second[i - 1] and not flag) or \
                (((first[i - 1] and not second[i - 1]) or (not first[i - 1] and second[i - 1])) and flag):
            out.append(0)
        elif (first[i - 1] and second[i - 1] and flag) or \
                (((first[i - 1] and not second[i - 1]) or (not first[i - 1] and second[i - 1])) and not flag):
            out.append(1)
        elif (not first[i - 1] and not second[i - 1] and flag) or (first[i - 1] and second[i - 1] and not flag):
            out.append(int(flag))
            flag = not flag

    return out[::-1]


def more_or_equal(first: list, second: list) -> bool:
    if first[0] != second[0]:
        return not first[0]

    if first[0]:
        for i in range(1, len(first)):
            if first[i] != second[i]:
                return not first[i]
    else:
        for i in range(1, len(first)):
            if first[i] != second[i]:
                return first[i]
    return True


def mult(first: list, second: list, length: int = constant.INT_LENGTH) -> list:
    out = get_binary(0, length)

    flag = (first[0] == second[0])
    first[0], second[0] = 0, 0

    while second != get_binary(0, length):
        out = addition(first, out)
        second = addition(second, [1] * length)

    out[0] = 0 if flag else 1

    return out


def division(first: list, second: list) -> list:
    out = get_binary(0)

    sign = (first[0] == second[0])
    first[0], second[0] = 0, 0

    while more_or_equal(first, second):
        second[0] = 1
        first = addition(first, binary2addition_binary(second))
        out = addition(out, get_binary(1))
        second[0] = 0

    return [int(not sign)] + out


def sum_bin(first: list, second: list, length: int = constant.INT_LENGTH) -> list:
    out = addition(binary2addition_binary(first, length), binary2addition_binary(second, length))
    return reverse_binary2binary(addition_binary2reverse_binary(out, length))


def get_binary_float(num_float: float) -> list:
    sign = 0
    if num_float < 0:
        num_float *= -1
        sign = 1

    try:
        per_dot, after_dot = str(num_float).split(".")
        if int(after_dot):
            mantissa_int = int(''.join([per_dot, after_dot]))
        else:
            mantissa_int = int(num_float)
    except ValueError:
        mantissa_int = int(num_float)

    if int(mantissa_int) == num_float:
        exp_int = 0
        while mantissa_int % constant.DECIMAL_BASE == 0:
            mantissa_int //= constant.DECIMAL_BASE
            exp_int += 1

    else:
        exp_int = str(num_float).find('.') - (len(str(num_float)) - 1)

    mantissa_bin = []
    while mantissa_int > 0:
        mantissa_bin.append(mantissa_int % constant.BINARY_BASE)
        mantissa_int = mantissa_int // constant.BINARY_BASE
    while len(mantissa_bin) < constant.MANTISSA_LENGTH:
        mantissa_bin.append(0)

    exp_bin = get_binary(exp_int, constant.EXP_LENGTH)

    return (mantissa_bin + exp_bin[::-1] + [sign])[::-1]


def float_addition(first: list, second: list):

    if more_or_equal(second[1:9], first[1:9]):
        first, second = second, first

    while first[1:9] != second[1:9]:

        first[1:9] = sum_bin(first[1:9], get_binary(-1, constant.EXP_LENGTH), constant.EXP_LENGTH)

        first[9:] = mult(first[9:],
                         get_binary(constant.DECIMAL_BASE, constant.MANTISSA_LENGTH),
                         constant.MANTISSA_LENGTH)

    out = sum_bin([first[0]] + first[9:], [second[0]] + second[9:], 24)
    return [out[0]] + first[1:9] + out[9:]


def binary2int(num_bin: list) -> int:
    num_int = 0

    for i in range(len(num_bin), 1, -1):
        num_int += pow(constant.BINARY_BASE, (len(num_bin) - i)) * num_bin[i - 1]

    return num_int if not num_bin[0] else -num_int


def binary_float2float(num: list):
    return (1 - 2 * num[0]) * binary2int(num[9:]) * \
        pow(constant.DECIMAL_BASE, binary2int(sum_bin(num[1:9], get_binary(127), constant.EXP_LENGTH)))


def main():

    match input('1 - Операции с целыми\n2 - Операции с дробными\n'):
        case '1':
            first = int(input("Введите первое число: "))
            second = int(input("Введите второе число: "))

            print(f'''
                Представление числа {first} в бинарном коде:
                    Прямое - {''.join([str(i) for i in get_binary(first)])}
                    Обратное - {''.join([str(i) for i in get_reverse_binary(first)])}
                    Дополнительное - {''.join([str(i) for i in get_addition_binary(first)])}
                
                Представление числа {-first} в бинарном коде:
                    Прямое - {''.join([str(i) for i in get_binary(-first)])}
                    Обратное - {''.join([str(i) for i in get_reverse_binary(-first)])}
                    Дополнительное - {''.join([str(i) for i in get_addition_binary(-first)])}
                    
                Представление числа {second} в бинарном коде:
                    Прямое - {''.join([str(i) for i in get_binary(second)])}
                    Обратное - {''.join([str(i) for i in get_reverse_binary(second)])}
                    Дополнительное - {''.join([str(i) for i in get_addition_binary(second)])}
                
                Представление числа {-second} в бинарном коде:
                    Прямое - {''.join([str(i) for i in get_binary(-second)])}
                    Обратное - {''.join([str(i) for i in get_reverse_binary(-second)])}
                    Дополнительное - {''.join([str(i) for i in get_addition_binary(-second)])}
                    
                        
                {first} + {second} = {binary2int(sum_bin(get_binary(first), get_binary(second)))}
                {first} - {second} = {binary2int(sum_bin(get_binary(first), get_binary(-second)))}
                -{first} + {second} = {binary2int(sum_bin(get_binary(-first), get_binary(second)))}
                -{first} - {second} = {binary2int(sum_bin(get_binary(-first), get_binary(-second)))}
                
                {first} * {second} = {binary2int(mult(get_binary(first), get_binary(second)))}
                {first} * (-{second}) = {binary2int(mult(get_binary(first), get_binary(-second)))}
                (-{first}) * {second} = {binary2int(mult(get_binary(-first), get_binary(second)))}
                (-{first}) * (-{second}) = {binary2int(mult(get_binary(-first), get_binary(-second)))}
                
                {first} / {second} = {binary2int(division(get_binary(first), get_binary(second)))} 
                {first} / (-{second}) = {binary2int(division(get_binary(first), get_binary(-second)))} 
                (-{first}) / {second} = {binary2int(division(get_binary(-first), get_binary(second)))} 
                (-{first}) / (-{second}) = {binary2int(division(get_binary(-first), get_binary(-second)))}
            ''')
        case '2':
            first = float(input("Введите первое число: "))
            second = float(input("Введите второе число: "))
            print(f'''
            {first} + {second} = {binary_float2float(
                float_addition(get_binary_float(first), get_binary_float(second))
            )}
            -{first} + {second} = {binary_float2float(
                float_addition(get_binary_float(-first), get_binary_float(second))
            )}
            {first} - {second} = {binary_float2float(
                float_addition(get_binary_float(first), get_binary_float(-second))
            )}
            -{first} - {second} = {binary_float2float(
                float_addition(get_binary_float(-first), get_binary_float(-second))
            )}''')


if __name__ == '__main__':

    main()
