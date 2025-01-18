class MinhaClasse:
    def __init__(self):
        self.__valor = None
        self.__elem = None

    def sertter_valor(self, valor: int) -> None:
        self.__valor = valor
    
    @property
    def getter_valor(self) -> int:
        return self.__valor


myClass = MinhaClasse()

print(myClass.getter_valor)