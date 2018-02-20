class Operacao:

    def __init__(self, jsonobj):
        self.Numero = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Numero'])
        self.Proposta = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['Proposta'])

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

