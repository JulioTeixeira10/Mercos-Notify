import requests #Biblioteca para fazer requisições HTTP
import time #Biblioteca para fazer o programa esperar quando necessário
import ast #Biblioteca para converter strings em dicionários
from winotify import Notification #Biblioteca para enviar notificações para o Windows
from twilio.rest import Client #Biblioteca para enviar notificações para o celular


cookieinput = "{'Cookie': '" + input("Coloque as cookies de autenticação: ") + "'}" #Coloque as cookies de autenticação do Mercos
result = ast.literal_eval(cookieinput) #Converte a string em um dicionário
 
pri = 0
pro = 0

while(True): 
    #Requisição HTTP
    AuthCookies = result
    url = 'https://app.mercos.com/xxxxx/pedidos/' #Coloque a URL dos pedidos do Mercos
    request = requests.get(url, headers = AuthCookies)
    htmltext = request.text

    def SendMessage(): #Função para enviar notificação para o celular
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body= f'NOVO PEDIDO - #{Npedido}',
                from_ =  ("numero do twilio"),
                to = ("numero do celular"))


    def SendMessage2(): #Função para enviar outra notificação para o celular
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body= f'PEDIDO CANCELADO - #{Npedido}',
                from_ = ("numero do twilio"),
                to = ("numero do celular"))

    #Arquivo HTML
    file = open(f"Coloque o diretorio do arquivo html aqui\\View.html","w+")
    file.write(htmltext)
    file.close()

    #Cookies inválidas
    indexcookie = htmltext.find('<h2 class="subTitulo">Acessar o sistema</h2>')
    while(True):
        if indexcookie != (-1):
            print("[ALTERAÇÃO DE COOKIES NECESSÁRIA]")
            cookieinput = "{'Cookie': '" + input("Coloque as novas cookies de autenticação: ") + "'}"
            result = ast.literal_eval(cookieinput)
            AuthCookies = result
            request = requests.get(url, headers = AuthCookies)
            htmltext = request.text
            indexcookie = htmltext.find('<h2 class="subTitulo">Acessar o sistema</h2>')
            if indexcookie != (-1):
                print("Cookies INVÁLIDAS, tente novamente: ")
            else:
                print("TUDO CERTO")
                break
        else:
            if pro == 0:
                print("TUDO CERTO")
                pro = 1
                break
            else:
                break

    #Olha se o pedido mais recente foi lançado hoje
    indexini = htmltext.find('<div class="section-title"><span>Hoje</span></div>')
    if indexini == (-1):
        while indexini == (-1):
            if pri == 0:
                print("Nenhum pedido foi lançado ainda.")
                pri = 1
            time.sleep(30)
            request = requests.get(url, headers = AuthCookies)
            htmltext = request.text
            indexini = htmltext.find('<div class="section-title"><span>Hoje</span></div>')
            if indexini != (-1):
                break
    else:
        pass

    #Número do pedido mais recente
    Npedido = htmltext[(indexini + 706):(indexini + 710)]
    LastOrder = int(Npedido)

    #Armazena o número do pedido do arquivo .log em uma variável
    with open('Coloque o diretorio do arquivo de log\\Pedido.log') as P:
        panterior = P.readlines()
        p2 = str(panterior)

    #Verifica se o pedido mais recente é o mesmo do arquivo .log, se o pedido anterior foi cancelado ou se é um novo pedido
    if p2[2:6] != Npedido:
        if str(LastOrder + 1) ==  p2[2:6]:
            SendMessage2()
            print(f"PEDIDO CANCELADO - #{LastOrder + 1}")
            file = open(f"Coloque o diretorio do arquivo de log\\Pedido.log","w+")
            file.write(Npedido)
            file.close()
            toast = Notification(app_id="MERCOS",
                        title="PEDIDO CANCELADO",
                        msg=f"O pedido N°{Npedido} foi CANCELADO",
                        icon="Coloque o diretorio do arquivo .ico\\icon.ico")
            toast.show()
        else:
            SendMessage()
            print(f"PEDIDO NOVO - #{Npedido}")
            file = open(f"Coloque o diretorio do arquivo de log\\Pedido.log","w+")
            file.write(Npedido)
            file.close()
            toast = Notification(app_id="MERCOS",
                        title="NOVO PEDIDO",
                        msg=f"Pedido N°{Npedido}",
                        icon="Coloque o diretorio do arquivo .ico\\icon.ico")
            toast.show()
    elif p2[2:6] == Npedido:
        pass
    time.sleep(30)