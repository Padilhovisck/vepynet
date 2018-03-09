class Cedente:

    def __init__(self, jsonobj):
        self.Codigo = (jsonobj['CONTRATO']['CEDENTE']['Codigo'])
        self.Empresa = (jsonobj['CONTRATO']['CEDENTE']['Empresa'])
        self.Razao = (jsonobj['CONTRATO']['CEDENTE']['Razao'])
        self.Cnpjcpf = (jsonobj['CONTRATO']['CEDENTE']['Cnpjcpf'])
        self.Dtcontrato = (jsonobj['CONTRATO']['CEDENTE']['Dtcontrato'])
        self.NumeroContratoMae = (jsonobj['CONTRATO']['CEDENTE']['NumeroContratoMae'])
        self.Endereco = (jsonobj['CONTRATO']['CEDENTE']['Endereco'])
        self.Cep = (jsonobj['CONTRATO']['CEDENTE']['Cep'])
        self.Cidade = (jsonobj['CONTRATO']['CEDENTE']['Cidade'])
        self.Estado = (jsonobj['CONTRATO']['CEDENTE']['Estado'])
