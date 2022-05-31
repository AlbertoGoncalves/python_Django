import time

try:   # (Tente) executar as ações a baixo
    a = 1200 / 0
    sfdsfsd()
except ZeroDivisionError: # (Se não) de certo execute as ações a baixo
    print('Não deu para seguir entrou na validacao de erro')
except NameError: # (Se não) de certo execute as ações a baixo
    print('digitou errado entrou na validacao de erro')

print('fim')



try:   # (Tente) executar as ações a baixo
    #a = 1200 / 0
    sfdsfsd()
except Exception as erro: # (Se não) de certo execute as ações a baixo
    print('deu erro:', erro)

print('fim')



try:   # (Tente) executar as ações a baixo
    open('C:\\Users\\alberto.goncalves\\PycharmProjects\\Aulas\\tcriar.txt', 'r')
except Exception as erro: # (Se não) de certo execute as ações a baixo
    print('deu erro:', erro)
    #time.sleep(5)

print('fim')


def abre_arquivo():
    try:   # (Tente) executar as ações a baixo
        arquivo = open('C:\\Users\\alberto.goncalves\\PycharmProjects\\Aulas\\ttcriar.txt')
        return True
    except Exception as erro: # (Se não) de certo execute as ações a baixo
        print('deu erro:', erro)
        #time.sleep(5)
        return False

    print('fim')

while not abre_arquivo():
    print('Tentando abrir arquivo')
    time.sleep(2)

print('deu certo')