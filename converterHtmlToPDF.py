import jinja2
import pdfkit

from assinanetpost import sendAssinaNetPost

#Enviar arquivo PDF para assinanet - <TOKEN>
from commands import gravar_arquivo


def sendAssinaNet(file):
    #parametros da (API.NET)
    print(file)
    #consumer_key = 'akey'
    #consumer_secret = 'asecret'
    #token_key = 'tokenKey'
    #token_secret = 'tokenSecret'
    #assinanet = Assinanet(consumer_key, consumer_secret, token_key, token_secret)
    #assinanet.sendpdf(file)

#criando o arquivo PDF and Request assinanet
def create_PDF(html, params):
    path_wkthmltopdf = params['wkhtmltopdf']
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_string(html, ("Pdf\\"+params['namefilepdf']), configuration=config)
    if pdf:
        gravar_arquivo('log.txt', 'Aditivo gerado com sucesso!')
        gravar_arquivo('log.txt', 'Chamando API (POST)...')
        params["RotaPDFGerado"] = params['filejson'].replace('File', 'Pdf').replace('.json', '.pdf')
        status_code = sendAssinaNetPost(params)
        if status_code == 200:
            gravar_arquivo('log.txt', ('Arquivo enviado com sucesso <status:' + str(status_code) + '>'))
            return True
        else:
            gravar_arquivo('log.txt', ('Problema ao enviar o arquivo <status:' + str(status_code) + '>'))
            return False

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
    html = render_html(params)
    if html:
        gravar_arquivo('log.txt', ('Arquivo HTML (renderizado) com sucesso!'))
        return create_PDF(html, params)

#metodo das classes de importação para Aditivo
def gerarAditivoPDF(contrato, cedente, operacao, originador, itens, params):
    favorites = ["chocolates", "lunar eclipses", "rabbits"]
    templateVars = {"contrato_Cliente": contrato.Cliente, "cedente_Empresa": cedente.Empresa, "favorites": favorites}
    params["templateVars"] = templateVars
    gravar_arquivo('log.txt', ('Criando variaves para substituição no arquivo HTML.'))
    ret = create_htmlTopdf(params)
    if ret:
        gravar_arquivo('log.txt', 'Fim da execução...')

#metodo das classes de importação para Contrato
def gerarContratoPDF(params):
    favorites = ["chocolates", "lunar eclipses", "rabbits"]
    templateVars = {"contrato_Cliente": "VENTURE SERVICE", "cedente_Empresa": "EPS BUSINESS", "favorites": favorites}
    params["templateVars"] = templateVars
    ret = create_htmlTopdf(params)
    if ret:
         print('Contrato Gerado com Sucesso!')
