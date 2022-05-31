from veiculo import Veiculo
from carro import Carro

car_1 = Veiculo('verde',4,'audi',10)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    print(car_1)
    print('Car:',car_1.cor,'Marca:' ,car_1.marca)
    print('Numero de Rodas:', car_1.rodas,'e com ',car_1.tanque,'Litros no Tanque')

    car_1.abastecimento(100)
    print('Apos abastecimento com ',car_1.tanque,'Litros no Tanque')

    car_1.rodagem(150)
    print('Apos abastecimento com ', car_1.tanque, 'Litros no Tanque')


    carro_1 = Carro('azul','VW',45)
    print('Car:', carro_1.cor, 'Marca:', carro_1.marca)
    print('Numero de Rodas:', carro_1.rodas, 'e com ', carro_1.tanque, 'Litros no Tanque')

    carro_1.abastecimento(100)
    print('Apos abastecimento com ',carro_1.tanque,'Litros no Tanque')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
