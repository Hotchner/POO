class MinhaClasse:

    estatico = "Meow"

    def __init__(self, estado):
        self.__estado = estado

    def print_variavel(self):
        print(self.estatico)

    def alterar__variavel(self):
        self.estatico = "Alguma coisa"


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)