from contrato import Contrato
from cedente import Cedente
from operacao import OperacaoEItens
from originador import Originador
from converterHtmlToPDF import gerarAditivoPDF, gerarContratoPDF

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
    if int(params['document']) == 0:

        params['templatehtml'] = 'Aditivo.html'

        #gerar arquivo PDF baseado no HTML passado.
        gerarAditivoPDF(Contrato(objson), Cedente(objson), OperacaoEItens(objson),
                         Originador(objson), OperacaoEItens.flsItens(objson), params)

    elif int(params['document']) == 1:

        params['templatehtml'] = 'Contrato.html'

        # gerar arquivo PDF baseado no HTML passado.
        gerarContratoPDF(params)
