import random


def calculate(func):
    import time

    def results():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return results


def ll(func):
    def wrapper():
        func()
        print("Второй декаратор")

    return wrapper


@ll
@calculate
def result():
    data = [random.randrange(0, 2 ** 1000) for x in range(0, 2 ** 25)]
    sorted(data)
    print("Hola")


result()
