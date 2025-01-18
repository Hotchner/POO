class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validade_input(nome, idade): #se __validade_input for true, o registro é autorizado
            self.__register_user(nome, idade)
        else:
            self.__error_handle() # se não for, apresenta o erro

    #Valida se os tipos são do tipo solicitado
    def __validade_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    #Autoriza o registro
    def __register_user(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrar usuário {nome}, idade {idade}")
    
    #Tratamento de erro
    def __error_handle(self) -> None:
        print("Dados inválidos")
 
sistema = SistemaCadastral()

sistema.cadastrar("Eduardo", "22")
