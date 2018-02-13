import jinja2
import pdfkit

from assinanetpost import Assinanet

#Enviar arquivo PDF para assinanet
def sendAssinaNet(file):
    #parametros da (API.NET)
    print(file)
    #consumer_key = 'akey'
    #consumer_secret = 'asecret'
    #token_key = 'tokenKey'
    #token_secret = 'tokenSecret'
    #assinanet = Assinanet(consumer_key, consumer_secret, token_key, token_secret)
    #assinanet.sendpdf(file)

#criando o arquivo PDF
def create_PDF(html, params):
    path_wkthmltopdf = params['wkhtmltopdf']
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_string(html, ("Pdf\\"+params['namefilepdf']), configuration=config)
    if pdf:
        sendAssinaNet(params['namefilepdf'])
        return ("Pdf\\"+params['namefilepdf'])

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
    return create_PDF(render_html(params), params)

#metodo das classes de importação para Aditivo
def gerarAditivoPDF(contrato, cedente, operacao, originador, itens, params):
    favorites = ["chocolates", "lunar eclipses", "rabbits"]
    templateVars = {"contrato_Cliente": contrato.Cliente, "cedente_Empresa": cedente.Empresa, "favorites": favorites}
    params["templateVars"] = templateVars
    ret = create_htmlTopdf(params)
    if ret:
         print('Aditivo Gerado com Sucesso!', ret)

#metodo das classes de importação para Contrato
def gerarContratoPDF(params):
    favorites = ["chocolates", "lunar eclipses", "rabbits"]
    templateVars = {"contrato_Cliente": "VENTURE SERVICE", "cedente_Empresa": "EPS BUSINESS", "favorites": favorites}
    params["templateVars"] = templateVars
    ret = create_htmlTopdf(params)
    if ret:
         print('Contrato Gerado com Sucesso!')
