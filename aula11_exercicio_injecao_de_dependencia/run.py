class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None
        self.plataform = "MySQL"
        self.server = "local_host"

    def banco_status(self):
        print(f"Estado atual da conexão: {self.connection}")

    def conectar_ao_banco(self) -> None:
        self.connection = True

class RepositorioDeBanco:
    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def get_conexao(self):
        return self.__conexao.connection

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]
        else:
            return None
        
class RegraDeNegocio:
    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print("Dados não encontrados, verifique sua conexão com o banco")
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f"O resultado e: {resposta}")


#conn = ConectorBancoDeDados()
#conn.conectar_ao_banco()
#print(conn.connection)

#repo1 = RepositorioDeBanco(conn)

#print(repo1.busca_dados())


DBx = ConectorBancoDeDados()
#DBx.banco_status()

DBx.conectar_ao_banco()
#DBx.banco_status()

repositorio_1 = RepositorioDeBanco(DBx)

print(repositorio_1.get_conexao())
print(DBx.plataform)

#print(repositorio_1.__conexao.plataform)