import requests
import json
from PySimpleGUI import PySimpleGUI as sg




def cotacao(moeda,data):
    ret_eur = {}
    ret_usd = {}
    try:
        dt = data[3:5] +'-'+ data[0:2] +'-'+ data[6:10]  #'04-03-2022'  MM-DD-AAAA
        print(dt)
        #moeda = 'EUR - Euro'
        #print(moeda[0:3]) #substr em python

        url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda=\''+ moeda[0:3] +'\'&@dataCotacao=\''+ dt +'\'&$top=100&$format=json&$select=paridadeCompra,paridadeVenda,cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim'
        #print(url)
        req = requests.get(url)
        #print('url')
        #print(req.text)
        dicionario = json.loads(req.text)
        #print(dicionario)
        #print(dicionario['value'][4])
        ret_eur = dicionario['value'][4]

        url1 = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda=\'USD\'&@dataCotacao=\''+ dt +'\'&$top=100&$format=json&$select=paridadeCompra,paridadeVenda,cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim'
        req1 = requests.get(url1)
        dicionario1 = json.loads(req1.text)
        # print(dicionario1['value'][4])
        ret_usd =  dicionario1['value'][4]
        #print(ret_eur)
        return [ret_eur,ret_usd]
    except:
        print('erro de conexão')
        exit()
        return None

    return None

# cotacao('EUR','03-04-2022')



def main():
    #Layout
    sg.theme('Reddit')
    layout = [
        [sg.Text('Data'),sg.Input(key='dt')],
        [sg.Text('Moeda'),sg.Input(key='moeda')],
        [sg.Text('Cotacao Compra Dolar: '), sg.Text(size=(10, 1), key='Cot_Comp1'),sg.Text('Cotacao Venda Dolar:'), sg.Text(size=(10, 1), key='Cot_Vend1')],
        # [sg.Text('Paridade Compra Dolar:'), sg.Text(size=(40, 1), key='Pari_Comp1')],
        # [sg.Text('Paridade Venda Dolar:'), sg.Text(size=(40, 1), key='Pari_Vend1')],
        [sg.Text('Cotacao Compra: '),sg.Text(size=(10,1), key='Cot_Comp'),sg.Text('Cotacao Venda:'),sg.Text(size=(10,1), key='Cot_Vend')],
        [sg.Text('Paridade Compra:'),sg.Text(size=(10,1), key='Pari_Comp'),sg.Text('Paridade Venda:'),sg.Text(size=(10,1), key='Pari_Vend')],
        #[sg.Text('Cotacao Venda:'),sg.Text(size=(40,1), key='Cot_Vend')],
        #[sg.Text('Paridade Venda:'),sg.Text(size=(40,1), key='Pari_Vend')],
        [sg.Button('Atualizar'),sg.Button('Sair')]
    ]
    #Janela
    janela = sg.Window('Cotações',layout)

    #Ler os Eventos
    while True:
        eventos,valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Sair':
            break
        if eventos == 'Atualizar':
            print(valores['moeda'],valores['dt'])
            #janela['-OUTPUT-'].update('Hello ' + values['Moeda'] )
            ret_val = cotacao(valores['moeda'], valores['dt'])
            #print(ret_val)
            #print(ret_val[0]['cotacaoCompra'])

            janela['Cot_Comp'].update(ret_val[0]['cotacaoCompra'])
            janela['Pari_Comp'].update(ret_val[0]['paridadeCompra'])
            janela['Cot_Vend'].update(ret_val[0]['cotacaoVenda'])
            janela['Pari_Vend'].update(ret_val[0]['paridadeVenda'])

            janela['Cot_Comp1'].update(ret_val[1]['cotacaoCompra'])
            #janela['Pari_Comp1'].update(ret_val[1]['paridadeCompra'])
            janela['Cot_Vend1'].update(ret_val[1]['cotacaoVenda'])
            #janela['Pari_Vend1'].update(ret_val[1]['paridadeVenda'])


#cotacao('EUR','03-04-2022')
main()

