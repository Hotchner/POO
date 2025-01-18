class MinhaClasse:
    def __init__(self):
        self.__valor = None
        self.__elem = None

    def sertter_valor(self, valor: int) -> None:
        self.__valor = valor

    def getter_valor(self) -> int:
        return self.__valor


myClass = MinhaClasse()

#myClass.valor = 3 #Ferindo o encapsulamento

myClass.sertter_valor(42)
valor = myClass.getter_valor()

print(valor)