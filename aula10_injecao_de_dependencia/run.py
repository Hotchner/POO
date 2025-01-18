class Celular:
    def __init__(self, modelo):
        self.modelo = modelo

    def enviar_mensagem(self, mensagem) -> None:
        print(f"Você enviou a mensagem: {mensagem}")

    def abrir_emails(self) -> None:
        print("Abrindos os E-mails")

    def abrir_youtube(self) -> None:
        print("Abrindo Youtube")

class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print("Localizando celular...")
        print("Definindo sabor...")
        self.__celular.enviar_mensagem("Quero de uma 4 queijos")
        print("Pedido realizado!")

    def estudar(self) -> None:
        print("Sentando na cadeira")
        self.__celular.abrir_youtube()

android = Celular("Motorola")
iphone = Celular("iPhone 13")

regina = Pessoa(android)
paulo = Pessoa(iphone)

regina.pedir_pizza()
print("------------------")
paulo.estudar()