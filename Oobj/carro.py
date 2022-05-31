from veiculo import Veiculo  # import Herança class Veiculo

class Carro(Veiculo):

    def __init__(self,cor,marca,tanque):
        Veiculo.__init__(self,cor,4,marca,tanque) # instanciando obj Herança class Veiculo

    def abastecimento(self,litros):
        if (self.tanque + litros) > 50:
            print('Erro de abastecimento')
        else:
            self.tanque += litros