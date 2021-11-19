import time 

class FiboIter():
    def __init__(self, max=None): ## solo lo utilizamos si necesitamos inicializar objeto/atributo
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.n2 + self.n1 < self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            elif self.counter !=0 or self.counter !=1:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux #  self.n1 = self.n2 y self.n2 = self.aux
                self.counter += 1
                return self.n2
        else:
            raise StopIteration

def run():
    max_fibonacci = int(input("Ingresa el numero maximo de la sucesion de fibonacci: "))
    fibonacci = FiboIter(max_fibonacci)  # instanciamos el iterador
    for element in fibonacci:
        print(element)
        time.sleep(0.05) # pausamos 0.05s antes de dar ka siguiente vuelta

if __name__ == "__main__":
    run()