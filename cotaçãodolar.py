import requests
import json
import datetime
import time

while True:
    requisicao = requests.get('https://api.promasters.net.br/cotacao/v1/valores')        #fazendo requisição no site metodo "GET"
    cotacao = json.loads(requisicao.text)

    print('### COTAÇÃO ###')
    print('Dolar:', cotacao['valores']['USD']['valor'])
    print('Euro:', cotacao['valores']['EUR']['valor'])
    print('BTC:', cotacao['valores']['BTC']['valor'])
    time.sleep(10)


