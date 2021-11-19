def is_primo(number: int) -> bool:
    contador = 0
    for i in range(1,number+1):
        if number % i == 0:
            contador +=1

    if contador == 2:
        return True
    else:
        return False

def run():
    number = int(input("Ingresa un numero: "))
    print(is_primo(number))


if __name__ == '__main__':
    run()

