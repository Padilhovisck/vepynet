import urllib
import oauth2
import json

class Assinanet:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def sendpdf(self, file):
        query_codificada = urllib.parse.quote(file, safe="")
        requisicao = self.cliente.request('http://' + query_codificada, method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto