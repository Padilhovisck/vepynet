import jinja2
import pdfkit

#criando o arquivo PDF
def create_PDF(html, params):
    path_wkthmltopdf = params['wkhtmltopdf']
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_string(html, ("Pdf\\"+params['namefilepdf']), configuration=config)
    return pdf

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
         print('Aditivo Gerado com Sucesso!')

#metodo das classes de importação para Contrato
def gerarContratoPDF(params):
    favorites = ["chocolates", "lunar eclipses", "rabbits"]
    templateVars = {"contrato_Cliente": "VENTURE SERVICE", "cedente_Empresa": "EPS BUSINESS", "favorites": favorites}
    params["templateVars"] = templateVars
    ret = create_htmlTopdf(params)
    if ret:
         print('Contrato Gerado com Sucesso!')
