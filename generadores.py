def my_gen():
    #  Un ejemplo de generadores
    # priorizar generadores sobre iteradores
    # sugar sintax de iteradores

    print("Hola mundo")
    n = 0
    yield n  # Retorno n y guardo el valor en scope local

    print("Hola saturno")
    n = 1
    yield n

    print("Hola marte")
    n = 2
    yield n

a = my_gen()
print(next(a))
print(next(a))
# print(next(a))  # StopIteration

#  Generator expression

my_list = [0,1,4,7,9,10]
my_seconds_list = [x*2 for x in my_list]  # List comprehension
my_second_gen = (x*2 for x in my_list)  # Generator expression

print(list(my_second_gen))