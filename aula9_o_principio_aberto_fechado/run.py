class Artista:
    def __init__(self, tipo: str):
        self.tipo = tipo
        
    def apresentar_show(self):
        print(f"O artista {self.tipo} vai apresentar o seu show")
        
class Circo:
    def apresentar(self, artista: Artista):
        print("O Show começou!")
        artista.apresentar_show()
        print(f"O Show acabou!")

circo = Circo()

palhaco = Artista("Palhaço")
magico = Artista("Magico")

circo.apresentar(palhaco)