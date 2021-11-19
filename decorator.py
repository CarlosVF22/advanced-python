from datetime import datetime

def execution_time(func):  # tiempo en ejecutarse una función e imprimirlo en pantalla
    def wrapper(*args, **kwargs):  # no importa la cantidad de argumentos posicionales y nombrados la funcion los va a recibir
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

# random_func()

