meu_dicionario = {'high':'ligado','low':'desligado'}
meu_conjunto = {'Teste','Teste_1'}
minha_tupla = ('Teste','Teste_1')
minha_lista = ['Teste','Teste_1']
# listas ou list (É mutavel Não pode aumentar via APPEND)

teste = {'@odata.context': 'https://was-p.bcnet.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata$metadata#_CotacaoMoedaDia(paridadeCompra,paridadeVenda,cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim)', 'value': [{'paridadeCompra': 1.0938, 'paridadeVenda': 1.0942, 'cotacaoCompra': 5.5282, 'cotacaoVenda': 5.5309, 'dataHoraCotacao': '2022-03-04 10:04:18.382', 'tipoBoletim': 'Abertura'}, {'paridadeCompra': 1.0906, 'paridadeVenda': 1.0908, 'cotacaoCompra': 5.5429, 'cotacaoVenda': 5.5445, 'dataHoraCotacao': '2022-03-04 11:03:18.388', 'tipoBoletim': 'Intermediário'}, {'paridadeCompra': 1.0906, 'paridadeVenda': 1.091, 'cotacaoCompra': 5.5405, 'cotacaoVenda': 5.5432, 'dataHoraCotacao': '2022-03-04 12:05:17.309', 'tipoBoletim': 'Intermediário'}, {'paridadeCompra': 1.0917, 'paridadeVenda': 1.0921, 'cotacaoCompra': 5.5504, 'cotacaoVenda': 5.5531, 'dataHoraCotacao': '2022-03-04 13:09:36.234', 'tipoBoletim': 'Intermediário'}, {'paridadeCompra': 1.0917, 'paridadeVenda': 1.0921, 'cotacaoCompra': 5.5406, 'cotacaoVenda': 5.5433, 'dataHoraCotacao': '2022-03-04 13:09:36.239', 'tipoBoletim': 'Fechamento PTAX'}]}
print(teste)
print(teste['value'])
print(teste['value'][0])

teste1 = [{'paridadeCompra': 1.0938, 'paridadeVenda': 1.0942, 'cotacaoCompra': 5.5282, 'cotacaoVenda': 5.5309, 'dataHoraCotacao': '2022-03-04 10:04:18.382', 'tipoBoletim': 'Abertura'}, {'paridadeCompra': 1.0906, 'paridadeVenda': 1.0908, 'cotacaoCompra': 5.5429, 'cotacaoVenda': 5.5445, 'dataHoraCotacao': '2022-03-04 11:03:18.388', 'tipoBoletim': 'Intermediário'}, {'paridadeCompra': 1.0906, 'paridadeVenda': 1.091, 'cotacaoCompra': 5.5405, 'cotacaoVenda': 5.5432, 'dataHoraCotacao': '2022-03-04 12:05:17.309', 'tipoBoletim': 'Intermediário'}, {'paridadeCompra': 1.0917, 'paridadeVenda': 1.0921, 'cotacaoCompra': 5.5504, 'cotacaoVenda': 5.5531, 'dataHoraCotacao': '2022-03-04 13:09:36.234', 'tipoBoletim': 'Intermediário'}, {'paridadeCompra': 1.0917, 'paridadeVenda': 1.0921, 'cotacaoCompra': 5.5406, 'cotacaoVenda': 5.5433, 'dataHoraCotacao': '2022-03-04 13:09:36.239', 'tipoBoletim': 'Fechamento PTAX'}]
print(teste1[0])




for valores in dicionario['value']:
    if 'Fechamento PTAX' in valores.values():
        # print('achou')
        # valores['tipoBoletim']
        # valores.keys()

        for valores1 in valores.values():
            print(valores1)
        '''
        print('Moeda:',moeda)
        print('Data Ref.:', data[3:5] +'/'+ data[0:2] +'/'+ data[6:10])
        print('Tipo de Fechamento:',valores['tipoBoletim'])

        print('Cotacao Compra:', valores['cotacaoCompra'])
        print('Paridade Compra:', valores['paridadeCompra'])

        print('\ncotacao Venda:', valores['cotacaoVenda'])
        '''


'''

minha_tupla = ('Teste','Teste_1')
#Tupla  ou tuple (Não é mutavel Não pode aumentar via APPEND)

print(minha_tupla)

print(minha_tupla[0])

for nome in minha_tupla:
    print(nome)

if 'Teste' in minha_tupla:
    print('Esta SIM')












meu_dicionario = {'high':'ligado','low':'desligado'}
meu_dicionario = {'Nome':'Carlos','Idade':'21','Sexo':'MachoMen'}
# Chave/Valor   ou dict

print(meu_dicionario)

print(meu_dicionario['Nome'])
print(meu_dicionario['Sexo'])

print(len(meu_dicionario))

if 'Carlos' in meu_dicionario.values():
    print('Carlos esta no dicionario')


for valores in meu_dicionario.values():
    print(valores)


for valores in meu_dicionario.keys():
    print(valores)


meu_dicionario['Nome'] = 'Jorge'
print(meu_dicionario)

meu_dicionario['Sexo'] = 'Bixa'
print(meu_dicionario)

meu_dicionario ['Endereco'] = 'Rua ate mais' #ADD novos itens
print(meu_dicionario)

# POP = para retirar itens












meu_conjunto = set()
meu_conjunto = {'Teste','Teste_1'}
#meu_conjunto.add('Teste_3') # como valor ja existe não é duplicado
# lista + dicionario  NÃO E ORDENADO NÃO TEM INDICE NÃO PERMITE ITENS REPETIDOS  ou set
# Conjunto é usado para pesquisas, Muito mais rapido para achar, tabela resh fica em memoria

print(meu_conjunto)

meu_conjunto.add('Teste_3')

print(meu_conjunto)

meu_conjunto.add('Teste_3') # como valor ja existe não é duplicado

if 'Teste' in meu_conjunto:
    print('Teste foi encontrado')

meu_conjunto.remove('Teste')

print(meu_conjunto)
'''