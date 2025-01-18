class MinhaClasse:

    estatico = "Meow"

    def __init__(self, estado):
        self.__estado = estado

    def print_variavel(self):
        print(self.estatico)

    @classmethod
    def alterar_variavel_de_classe(cls):
        cls.estatico = "Alguma coisa"
        #MinhaClasse.estatico = "Alguma coisa"


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)
obj3 = MinhaClasse(True)
print(f"Values: {obj1.estatico} {obj2.estatico} {obj3.estatico}")

obj1.alterar_variavel_de_classe()

print(obj1.estatico)
print(obj2.estatico)
print(obj3.estatico)
print(MinhaClasse.estatico)

