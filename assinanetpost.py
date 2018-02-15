import requests
import base64

def sendAssinaNetPost(params):
    try:
        with open(params['RotaPDFGerado'], "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())

        r = requests.post('http://localhost:5000/api/values',
                          json={"NumeroDoLote": 10522,
                                "Cliente": params['templateVars']['contrato_Cliente'],
                                "Cedente": params['templateVars']['cedente_Empresa'],
                                "Filename": encoded_string.decode('utf-8')
                                })
        #print(r.json())
        return r.status_code

    except Exception as erro:
        return 'Retorno do erro', erro


# import urllib
# import oauth2
# import json
#
# class Assinanet:
#
#     def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
#         self.conexao(consumer_key, consumer_secret, token_key, token_secret)
#
#     def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
#         self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
#         self.token = oauth2.Token(token_key, token_secret)
#         self.cliente = oauth2.Client(self.consumer, self.token)
#
#     def sendpdf(self, file):
#         query_codificada = urllib.parse.quote(file, safe="")
#         requisicao = self.cliente.request('http://' + query_codificada, method='POST')
#         decodificar = requisicao[1].decode()
#         objeto = json.loads(decodificar)
#         return objeto