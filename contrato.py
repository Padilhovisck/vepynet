class Contrato:

    def __init__(self, jsonobj):
        self.Cliente = (jsonobj['CONTRATO']['Cliente'])
        self.CnpjCpf = (jsonobj['CONTRATO']['Cnpjcpf'])
        self.Registro = (jsonobj['CONTRATO']['Registro'])
        self.Cidade = (jsonobj['CONTRATO']['Cidade'])
        self.Rep1Nome = (jsonobj['CONTRATO']['IRep'])
        self.Rep1CnpjCpf = (jsonobj['CONTRATO']['ICnpjcpf'])
        self.Rep2Nome = (jsonobj['CONTRATO']['IIRep'])
        self.Rep2CnpjCpf = (jsonobj['CONTRATO']['IICnpjcpf'])
        self.Rep3Nome = (jsonobj['CONTRATO']['IIIRep'])
        self.Rep3CnpjCpf = (jsonobj['CONTRATO']['IIICnpjcpf'])
        self.Rep4Nome = (jsonobj['CONTRATO']['IVRep'])
        self.Rep4CnpjCpf = (jsonobj['CONTRATO']['IVCnpjcpf'])
        self.Rep5Nome = (jsonobj['CONTRATO']['VRep'])
        self.Rep5CnpjCpf = (jsonobj['CONTRATO']['VCnpjcpf'])
        self.Rep6Nome = (jsonobj['CONTRATO']['VIRep'])
        self.Rep6CnpjCpf = (jsonobj['CONTRATO']['VICnpjcpf'])

