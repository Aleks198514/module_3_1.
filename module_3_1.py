calls = 0


def count_calls():
    print(calls)
def count_calls():  # подсчитывающая вызовы остальных функций.
    global calls
    calls += 1


def string_info(string):  # Принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Capybarattt'))
print(string_info('Armageddonnnn'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
