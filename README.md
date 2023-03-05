Notificação de Pedido do Mercos
Este script foi desenvolvido para notificar você quando um novo pedido é realizado ou um pedido é cancelado na plataforma do Mercos. O script é executado continuamente em segundo plano, verificando novos pedidos a cada 30 segundos e enviando uma notificação para a área de trabalho do seu Windows e/ou dispositivo móvel usando o Twilio.

Começando
Para usar este script, você precisará ter o Python 3 instalado em seu computador. Além disso, será necessário instalar as seguintes bibliotecas:
requests
time
ast
winotify
twilio

Você pode instalar essas bibliotecas usando o pip:
pip install requests
pip install winotify
pip install twilio

Uso
Clone este repositório em sua máquina local.
Abra um terminal ou prompt de comando e navegue até o diretório onde o script está localizado.

Execute o script usando o seguinte comando:
python mercos_order_notification.py

Você será solicitado a inserir seus cookies de autenticação para a plataforma do Mercos.
O script verificará continuamente novos pedidos a cada 30 segundos. Se um novo pedido for realizado ou um pedido for cancelado, você receberá uma notificação na área de trabalho do seu Windows e/ou dispositivo móvel.

Personalização
Você precisará personalizar as seguintes partes do script para fazê-lo funcionar para o seu caso de uso específico:

cookieinput: substitua o URL pelo URL da página do pedido na plataforma do Mercos.

SendMessage e SendMessage2: substitua o SID da conta e o token de autenticação pelo SID da sua conta Twilio e pelo token de autenticação. Além disso, substitua os números de telefone "from" e "to" pelo número de telefone Twilio e pelo seu número pessoal, respectivamente.

file: substitua o diretório do arquivo View.html pelo diretório onde você deseja salvar o arquivo HTML.

file: substitua o diretório do arquivo Pedido.log pelo diretório onde você deseja salvar o arquivo de log.

toast: substitua os parâmetros app_id, title, msg e icon pelos valores que deseja para suas notificações.
