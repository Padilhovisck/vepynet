from commands import real_br_money_mask

class Itens:

    def __init__(self, jsonobj):
        self.Total = self.somaTotal(jsonobj)

    # valor total dos itens
    def somaTotal(self, objson):
        total = 0
        for i, item in enumerate(objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']):
            total += (item['Valor'])
        return real_br_money_mask(round(total, 2))

    # colunas do grid
    def readHeader(objson):
        headers = {}
        for i, item in enumerate(objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS']):
            if i == 0:
                headers = list(item)
        return headers

    # style das colunas
    def styleHeader(objson):
        style = ['left', 'left', 'center', 'center', 'left']
        generico = {}
        for i, k in enumerate(Itens.readHeader(objson)):
            generico.update({k.upper(): style[i]})
        return generico

    # monta lista de itens do grid
    def lendoItens(objson, namecoluna):
        returnlist = {}
        generico= []

        for i, item in (enumerate(objson['CONTRATO']['CEDENTE']['OPERACAO']['ITENS'])):
            item_valor = item[namecoluna]
            if namecoluna == 'Valor':
                item_valor = real_br_money_mask(item_valor)
            generico.append(item_valor)
            returnlist.update({namecoluna.upper(): generico})
        return returnlist

    # itens do grid
    def itensdaoperacaoGridHtml(objson):
        lista = {}
        for k in (Itens.readHeader(objson)):
            monta = (Itens.lendoItens(objson, k))
            lista.update(monta)
        return lista

