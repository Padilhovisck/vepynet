class OperacaoEItens:

    def __init__(self, jsonobj):
        self.Numero = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Numero'])
        self.Proposta = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Proposta'])

    def flsItens(objson):
        lsItens = []
        for i in objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']:
            lsItens.append(i)

        return lsItens
