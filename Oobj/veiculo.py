class Veiculo:

    def __init__(self,cor,rodas,marca,tanque): # Construtor!
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecimento(self,litros):
        self.tanque += litros

    def rodagem(self,km):
        self.tanque -= km/10

