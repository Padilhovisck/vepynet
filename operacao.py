class Operacao:

    def __init__(self, jsonobj):
        self.Numero = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Numero'])
        self.Proposta = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Proposta'])
        self.Data = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Data'])
        self.Face = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Face'])
        self.Compra = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Compra'])
        self.DepServico = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Despservico'])
        self.DesAdicional = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Despadicional'])
        self.Advalorem = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Advalorem'])
        self.PercAdvalorem = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['PercAdvalorem'])
        self.IOF = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Iof'])
        self.Liquido = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Liquido'])
        self.Liberar = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Liberar'])
        self.ISS = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Iss'])

    def flsItens(objson):
        lsItens = []
        for i in objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']:
            lsItens.append(i)

        return lsItens

    def lendoItens(objson):
        listaDeItens = []
        newlista = []
        for i, item in enumerate(objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']):
            print(item)
            #print(i, listaDeItens[i])


        #print((dic_listaDeItens))

