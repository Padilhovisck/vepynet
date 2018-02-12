class Contrato:

    def __init__(self, jsonobj):
        self.Cliente = (jsonobj['CONTRATO']['Cliente'])
        self.CnpjCpf = (jsonobj['CONTRATO']['Cnpjcpf'])
