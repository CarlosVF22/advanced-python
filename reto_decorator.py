#  el decorador debe agregar el nombre de la funcion que se esta ejecutando y el tiempo que duro en hacerlo
from datetime import datetime


def info(func):
    def wrapper(*args, **kwargs):
        print(f'Usted ha ejecutado la {func}')
        initial_time = datetime.now()
        print("Ejecucion de la función: ")
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper


@info
def saludo(text):
    print(str(text))

def run():
    saludo("Hola, soy carlos")



if __name__ == "__main__":
    run()


