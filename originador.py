class Originador:

    def __init__(self, jsonobj):
        self.Id = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['ORIGINADOR']['Id'])
        self.Nome = (jsonobj['CONTRATO']['CEDENTE']['OPERACAO']['ORIGINADOR']['Nome'])