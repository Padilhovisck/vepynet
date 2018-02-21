class Itens:

    def readHeader(objson):
        headers = {}
        for i, item in enumerate(objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']):
            if i == 0:
                headers = list(item)
        return headers

    def lendoItens(objson, namecoluna):
        returnlist = {}
        generico= []
        for i, item in (enumerate(objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS'])):
            generico.append(item[namecoluna])
            returnlist.update({namecoluna.upper(): generico})
        return returnlist

    def totaldaOperacao(objson):
        Total = 0.0
        for coluna in (objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']):
            print (coluna['Valor'])
            Total = float(coluna['Valor'])
            Total += Total
            return Total



