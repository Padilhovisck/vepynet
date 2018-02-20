from commands import gravar_arquivo

#metodo das classes de importação para Aditivo
def attribuindovalores(classes, params):

    gravar_arquivo('log.txt', ('Criando variaves para substituição no arquivo HTML.'))

    # recupera dados das classes
    contrato = classes['contrato']
    cedente  = classes['cedente']
    operacao = classes['operacao']
    itens    = classes['itens']

    teste = [['LAURINDA   JARDIM DOS SANTOS', 'DUPLICATAS SERVIÃ‡OS', 'ABC1', '10/12/2016', 9863.33],
            ['LAURINDA   JARDIM DOS SANTOS', 'DUPLICATAS SERVIÃ‡OS', 'ABC2', '10/12/2016', 9863.33]]

    d = {'SACADO': ['LAURINDA JARDIM DOS SANTOS', 'LAURINDA JARDIM DOS SANTOS'],
         'DOCUMENTO': ['DUPLICATA DE SERVICO', 'DUPLICATA DE SERVICO'],
         'TITULO': ['ABC1', 'ABC2'],
         'VENCIMENTO': ['10/12/2016', '10/01/2018'],
         'VALOR': ['9863.33', '1230.89']
         }

    headerpos = {'left', 'left', 'center', 'center', 'right'}

    #header grid itens
    icount = 0
    for k in itens:
        icount += 1
        if icount == 1:
            header = (k.keys())

    # itend do grid
    listaDoGrid = []
    for k in itens:
        for item in (list(k.values())):
            listaDoGrid.append(item)

    # Atribuir valores a serem renderizados!
    valoresAtribuidos = {

        # Cedente
        "cedente_Razao"             : cedente.Razao,
        "cedente_Cnpjcpf"           : cedente.Cnpjcpf,
        "cedente_Dtcontrato"        : cedente.Dtcontrato,
        "cedente_NumeroContratoMae" : cedente.NumeroContratoMae,

        # Contrato
        "contrato_Cliente"   : contrato.Cliente.upper(),
        "contrato_Cnpjcpf"   : contrato.CnpjCpf,
        "contrato_Registro"  : contrato.Registro,
        "contrato_IRep"      : contrato.Rep1Nome.upper(),
        "contrato_ICnpjcpf"  : contrato.Rep1CnpjCpf,
        "contrato_IIRep"     : contrato.Rep2Nome.upper(),
        "contrato_IICnpjcpf" : contrato.Rep2CnpjCpf,
        "contrato_IIIRep"    : contrato.Rep3Nome.upper(),
        "contrato_IIICnpjcpf": contrato.Rep3CnpjCpf,
        "contrato_IVRep"     : contrato.Rep4Nome.upper(),
        "contrato_IVCnpjcpf" : contrato.Rep4CnpjCpf,
        "contrato_VRep"      : contrato.Rep5Nome.upper(),
        "contrato_VCnpjcpf"  : contrato.Rep5CnpjCpf,
        "contrato_VIRep"     : contrato.Rep6Nome.upper(),
        "contrato_VICnpjcpf" : contrato.Rep6CnpjCpf,

        # Operacao
        "operacao_Numero":  operacao.Numero,

        # Itens
        "header_grid": headerpos,
        "d": d}

    # Adiciona ao dicionario
    params["templateVars"] = valoresAtribuidos

    return params
