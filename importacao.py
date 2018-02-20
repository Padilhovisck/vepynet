from assinanetpost import sendAssinaNetPost
from contrato import Contrato
from cedente import Cedente
from operacao import Operacao
from originador import Originador
from atribuindovalores import attribuindovalores
from converterHtmlToPDF import gerarAditivoPDF, gerarContratoPDF
from commands import gravar_arquivo

# alimenta classes com o arquivo Json
def readjsonToClass(objson):
    classes = {'contrato': Contrato(objson),
               'cedente': Cedente(objson),
               'operacao': Operacao(objson),
               'itens': Operacao.flsItens(objson),
               'originador': Originador(objson)
               }

    # d = {'Sacado': ['LAURINDA JARDIM DOS SANTOS', 'LAURINDA JARDIM DOS SANTOS'],
    #      'Documento': ['DUPLICATA DE SERVICO', 'DUPLICATA DE SERVICO'],
    #      'Titulo': ['ABC1','ABC2'],
    #      'Vencimento': ['10/12/2016','10/01/2018'],
    #      'Valor': ['9863.33', '1230.89']
    #      }
    #
    # for i in range(len(d['Sacado'])):
    #     for k in d:
    #         print(d[k][i])


    return classes

# logica de documento de Contrato
def contrato(x, y):
    return 'contrato.html'

# logica de documento de Aditivo
def aditivo(x, y):
    documentos = []
    numero_html = (y-x)

    if x - y == 0:

        if x == 1:
            documentos.append('aditivo.html')
        elif x == 2:
            documentos.append('recibo.html')
        elif x == 3:
            documentos.append('notapromissoria.html')
        elif x == 4:
            documentos.append('contagrafica.html')
    else:
        documentos = ['aditivo.html', 'recibo.html']

        if numero_html > 1:
            documentos.append('notapromissoria.html')

        if numero_html > 2:
            documentos.append('contagrafica.html')

    return documentos

documentoAserConvertido = {0: aditivo, 1: contrato}

# identificando templates HTML
def templatesHTML(params):
    documento = int(params['document'])  # index
    parametro = params['numberdocs']
    return documentoAserConvertido[documento](int(parametro[1]), int(parametro[3]))

def resultSetData(params, objson):
    # Dados do Contrato
    # contrato = Contrato(objson)
    # print('Dados do Contrato: (Nome do Cliente) - {0}'.format(contrato.Cliente))

    # Dados do Cedente
    # cedente = Cedente(objson)
    # print('Dados do Cedente: (Código) - {0}'.format(cedente.Empresa))
    #
    # # Dados da Operacao
    # operacao = Operacao(objson)
    # print('Dados da Operação: (N. da Proposta) - {0}'.format(operacao.Proposta))
    #
    # # Originador da Operacao
    # originador = Originador(objson)
    # print('Dados do Originador: (Nome) - {0}'.format(originador.Nome))
    #
    # # Itens da Operacao
    # for item in itens.flsItens(objson):
    #     print(item['Sacado'], item['Titulo'], item['Vencimento'], item['Valor'])

    # Call render html to pdf - (document = 0 (Aditivo) | 1 (contrato))

    # Aditivo (modelo)

    if int(params['document']) == 0:

        # alimenta classes com o arquivo json
        classes = readjsonToClass(objson)

        try:
            # chamando metodo de atribuição de valores ao HTML.
            objAtribuicao = attribuindovalores(classes, params)

        except Exception as erro:
            gravar_arquivo('log.txt', ('erro na atribuição:', str(erro)))

        # identificar os templates a serem renderizados
        documentosAseremRenderizados = templatesHTML(params)

        # percorrendo numero de documentos a serem gerados
        documentos = {}
        count = 0
        if len(documentosAseremRenderizados) > 0:

             for namehtml in documentosAseremRenderizados:
                 count += 1
                 # add e anexa o nome do template em HTML
                 params['templatehtml'] = namehtml
                 if count == 1:
                     nomedoPDF = params['namefilepdf']

                 params['qtdeDoctos'] = count
                 params['namefilepdf'] = namehtml.replace('.html', '') + nomedoPDF

                 # gerando aditivo em Base64
                 encoded_string = gerarAditivoPDF(objAtribuicao)

                 if encoded_string:
                     nome = namehtml.replace('.html', '')
                     if count == 1:
                         documentos = {nome: encoded_string}
                     else:
                         documentos[nome] = encoded_string

        return sendAssinaNetPost(params, documentos)

    elif int(params['document']) == 1:

        params['templatehtml'] = 'Contrato.html'

        # gerar arquivo PDF baseado no HTML passado.
        gerarContratoPDF(params)
