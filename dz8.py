import time


def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Час виконання:", end - start, "секунд")

    return wrapper


@measure_time
def test_function():
    time.sleep(2)
    print("Функція виконується")


test_function()