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

    def turn_on_connection(self):
        self.__conexao.conectar_ao_banco()

    def get_conexao(self):
        return self.__conexao.connection
    
    def get_server(self):
        return f"A aplicação se encontra no servidor:{self.__conexao.server}"

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



#DBx.conectar_ao_banco()
#DBx.banco_status()

DBx = ConectorBancoDeDados()
DBx.banco_status()
repoX = RepositorioDeBanco(DBx)
print(repoX.get_server())
repoX.turn_on_connection()
DBx.banco_status()
print("*"*50)
print(repoX.busca_dados())

st_roll = RegraDeNegocio(repoX)
print(st_roll.calcular_resultados())



#repositorio_1 = RepositorioDeBanco(DBx)

#print(repositorio_1.get_server())

#print(repositorio_1.__conexao.plataform)

