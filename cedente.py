class Cedente:

    def __init__(self, jsonobj):
        self.Codigo = (jsonobj['CONTRATO']['CEDENTE']['Codigo'])
        self.Empresa = (jsonobj['CONTRATO']['CEDENTE']['Empresa'])
