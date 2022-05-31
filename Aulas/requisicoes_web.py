import requests  #Beautiful Soup 4 BS4 Melhor para tratamento de paguinas web

cabecalho = {'User-agent':"Win200",
             'referer':'https://meuteste.com'}

try:
    requisicao = requests.get('https://putsreq.com/6X3eHnxNvceaRP5HWWa0')

    requisicao = requests.post('https://putsreq.com/6X3eHnxNvceaRP5HWWa0',
                               headers = cabecalho)
    print(requisicao.text)
except Exception as e:
    print('Erro ao tenta acessar pagina')





