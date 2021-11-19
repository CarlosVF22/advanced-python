#  Palindromo utilizando tipado estatico

def is_palindrome(string: str) -> bool:  # Aceptamos string y retornamos bool
    string = string.replace(" ", "").lower()  # Eliminando espacios y todo minusculas

    return (string == string[::-1])  # Voltear un iterable


def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()
