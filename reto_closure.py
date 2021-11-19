#  This closure returns a function that returns the division of an x number by n

def make_division_by(n):
    def division(x):
        assert type(x) == int, "Solo puedes ingresar numeros"
        return x/n
    return division


division_by_3 = make_division_by(3)
print(division_by_3(18))  # 6}


#  DECORADORES

def mayusculas(func):
    def wrapper(string):
        return func(string).upper()
    return wrapper

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'  # Es necesaria la f para imprimir variable en cadena de texto

print(mensaje("Cesar"))