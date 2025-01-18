class Interruptor:
    def __init__(self, comodo: str):
        self.comodo = comodo

    def acender(self):
        print(f"Estou acendendo a luz do comodo: {self.comodo}")

    def apagar(self):
        print(f"Estou apagando a luz do comodo: {self.comodo}")

class Pessoa:
    def acender_luzes(self, interruptor: Interruptor):
        interruptor.acender()

    def apaga_luzes(self, interruptor: Interruptor):
        interruptor.apagar()

    def dormir(self):
        print("A pessoa foi dormir")

ana = Pessoa()
interruptor_sala = Interruptor("sala")
interruptor_quarto = Interruptor("quarto")

#ana.acender_luzes(interruptor_sala)
#ana.acender_luzes(interruptor_quarto)

class Veiculo:
    def __init__(self, tipo_veiculo: str):
        self.tipo_veiculo = tipo_veiculo

    def acelerar(self):
        print(f"Estou acelerando o veiculo {self.tipo_veiculo}")

    def freiar(self):
        print(f"Estou freiando o veiculo {self.tipo_veiculo}")

class Motorista:
    def acelerar_veiculo(self,veiculo: Veiculo):
        veiculo.acelerar()

    def freiar_veiculo(self, veiculo: Veiculo):
        veiculo.freiar()


luiza = Motorista()

veiculo_caminhao = Veiculo("Caminhao")
veiculo_moto = Veiculo("Moto")

luiza.acelerar_veiculo(veiculo_caminhao)
luiza.acelerar_veiculo(veiculo_moto)





    
    
        
