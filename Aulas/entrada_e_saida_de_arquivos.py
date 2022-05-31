open('C:\\Users\\alberto.goncalves\\PycharmProjects\\Aulas\\entrada_e_saidas.txt')

open('C:\\Users\\alberto.goncalves\\PycharmProjects\\Aulas\\teste_criar.txt','w')
# 'r' Leitura 'r+' (Leitura + escrita mas nao cria novo)  'w' escrita/Salvar  'a' append adicionar nao sobescrever

arquivo = open('C:\\Users\\alberto.goncalves\\PycharmProjects\\Aulas\\entrada_e_saidas.txt','r+')
type(print(arquivo))
print(arquivo.read())
'''
arquivo.write("\nNovo teste para arquivos")
arquivo.write('\n')
for i in range(10):
    arquivo.write( str(i) + '\n')
'''

print('Vai imprimir')
for linha in arquivo:
    print(linha)



png = open('C:\\Users\\alberto.goncalves\\PycharmProjects\\Aulas\\Logo TI FINAL.png','rb')
print(png.read())