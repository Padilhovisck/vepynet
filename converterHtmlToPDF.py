import jinja2
import pdfkit

from assinanetpost import sendAssinaNetPost, generateBase64encode

#Enviar arquivo PDF para assinanet - <TOKEN>
from commands import gravar_arquivo

# Token <assinatura>
def sendAssinaNet(file):
    #parametros da (API.NET)
    print(file)
    #consumer_key = 'akey'
    #consumer_secret = 'asecret'
    #token_key = 'tokenKey'
    #token_secret = 'tokenSecret'
    #assinanet = Assinanet(consumer_key, consumer_secret, token_key, token_secret)
    #assinanet.sendpdf(file)

# Call Request assinanet
def encoded_string(params):

    # criando a rota do arquivo PDF : encoded
    x = params["filejson"].replace('File', 'Pdf')
    index = (len(x.split('\\')) - 1)
    i = x.split('\\', index)
    domain_name = i[index]
    params["RotaPDFGerado"] = x.replace(domain_name, params["namefilepdf"])

    # chamando metodo encode base64
    encoded_string = generateBase64encode(params["RotaPDFGerado"])
    return encoded_string.decode('utf-8')

#criando o arquivo PDF
def create_PDF(html, params):
    path_wkthmltopdf = params['wkhtmltopdf']
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_string(html, ("Pdf\\"+params['namefilepdf']), configuration=config)
    if pdf:
        gravar_arquivo('log.txt', 'Aditivo gerado com sucesso!')
        gravar_arquivo('log.txt', 'Chamando API (POST)...')
        return encoded_string(params)

#renderizando conforme os dados
def render_html(params):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template_file = 'HTML/' + params['templatehtml']
    template = templateEnv.get_template(template_file)
    html = template.render(params['templateVars'])
    return html

#metodos de conversão HTML To PDF
def create_htmlTopdf(params):
    # retorna o Html com as variaveis substituidas
    html = render_html(params)
    if html:
        gravar_arquivo('log.txt', ('Arquivo HTML (renderizado) com sucesso!'))
        # retira o arquivo PDF e envia via requests
        return create_PDF(html, params)

#metodo das classes de importação para Aditivo
def gerarAditivoPDF(params):
    ret = create_htmlTopdf(params)
    if ret:
        gravar_arquivo('log.txt', 'Montagem do dicionario request')
        return ret

#metodo das classes de importação para Contrato
def gerarContratoPDF(params):
    favorites = ["chocolates", "lunar eclipses", "rabbits"]
    templateVars = {"cedente_Dtcontrato": params['Dtcontrato'],
                    "cedente_NumeroContratoMae": params['NumeroContratoMae'],
                    "operacao_Numero":  params['Numero'],
                    "favorites": favorites}
    params["templateVars"] = templateVars
    print(params)
    # ret = create_htmlTopdf(params)
    # if ret:
    #      print('Contrato Gerado com Sucesso!')