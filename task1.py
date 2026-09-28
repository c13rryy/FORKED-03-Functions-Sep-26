def sequence(*args):
    result = ()

    if tuple_el_type(args):
        return result

    if len(args) == 1 and args[0] > 0:
        result = tuple(el for el in range(args[0] + 1))
    elif len(args) == 1 and args[0] < 0:
        result = tuple(el for el in range(args[0], 1))
    elif len(args) == 2:
        new_tuple = convert_tuple(args)
        result = tuple(el for el in range(new_tuple[0], new_tuple[1] + 1))
    elif len(args) > 2:
        result = args

    return result


def convert_tuple(data):
    lst = [el for el in data]
    lst.sort()

    return tuple(x for x in lst)


def tuple_el_type(data):
    for el in data:
        return not isinstance(el, int)


assert sequence(5) == (0, 1, 2, 3, 4, 5), "Ожидался диапазон от 0 до 5"
assert sequence(-3) == (-3, -2, -1, 0), "Ожидался диапазон от -3 до 0"
assert sequence(2, 6) == (2, 3, 4, 5, 6), "Ожидался диапазон от 2 до 6"
assert sequence(10, 7) == (7, 8, 9, 10), "Ожидался диапазон от 7 до 10"
assert sequence(-3, -7) == (-7, -6, -5, -4, -3), "Ожидался диапазон от -7 до -3"
assert sequence(1, 2, 3, 4) == (1, 2, 3, 4), "Ожидался кортеж из переданных чисел"
assert sequence() == (), "Ожидался пустой кортеж"
assert sequence("test1", "test2") == (), "Ожидался пустой кортеж"
