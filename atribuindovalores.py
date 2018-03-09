#metodo das classes de importação para Aditivo
from commands import gravar_arquivo, real_br_money_mask, dataextenso, diaMesAnoExtenso, valorporextenso
from extenso import NumeroPorExtenso


def attribuindovalores(classes, params):

    gravar_arquivo('log.txt', ('Criando variaves para substituição no arquivo HTML.'))

    # recupera dados das classes
    contrato = classes['contrato']
    cedente = classes['cedente']
    operacao = classes['operacao']
    itens = classes['itens']
    itensTotal = classes['totalDosItens']
    styleHeaderItens = classes['styleHeaderItens']

    # tratamento
    e = valorporextenso(operacao.Liberar)
    np = valorporextenso(operacao.Face)

    # somando
    c = (float(operacao.DesAdicional)) + (float(operacao.DepServico))
    desembolso = (float(operacao.IOF)) + (float(operacao.Liquido))

    # subtraindo
    facemenoscompra = (float(operacao.Face)) - (float(operacao.Compra))
    desembolsosemiof= (desembolso - (float(operacao.IOF)))

    # extenso Nota Promissoria
    dataporextensoMaxDataItens = diaMesAnoExtenso(operacao.MaxDataItens, ' dias do mês de ', ' do ano ')
    dataporextensoDaProposta = diaMesAnoExtenso(operacao.MaxDataItens, ' de ', ' de ')

    # Atribuir valores a serem renderizados!
    valoresAtribuidos = {

        # Cedente
        "cedente_Codigo": cedente.Codigo,
        "cedente_Razao"             : cedente.Razao.upper(),
        "cedente_Cnpjcpf"           : cedente.Cnpjcpf,
        "cedente_Dtcontrato"        : cedente.Dtcontrato,
        "cedente_NumeroContratoMae" : cedente.NumeroContratoMae,
        "cedente_Endereco": cedente.Endereco.upper(),
        "cedente_Cep": cedente.Cep,
        "cedente_Cidade": cedente.Cidade.upper(),
        "cedente_Estado": cedente.Estado.upper(),

        # Contrato
        "contrato_Cliente"   : contrato.Cliente.upper(),
        "contrato_Cnpjcpf"   : contrato.CnpjCpf,
        "contrato_Registro"  : contrato.Registro,
        "contrato_Cidade"    : contrato.Cidade,
        "contrato_IRep"      : contrato.Rep1Nome.upper(),
        "contrato_ICnpjcpf"  : contrato.Rep1CnpjCpf,
        "contrato_INascimento": contrato.Rep1Nascimento,
        "contrato_IEcivil"   : contrato.Rep1EstadoCivil,
        "contrato_IProfissao": contrato.Rep1Profissao,
        "contrato_IRg"       : contrato.Rep1RG,
        "contrato_IEndereco" : contrato.Rep1Endereco,
        "contrato_ICidade"   : contrato.Rep1Cidade,
        "contrato_IEstado"   : contrato.Rep1Estado,
        "contrato_ICep"      : contrato.Rep1Cep,
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
        "dataporextenso": (contrato.Cidade + ' ' + dataextenso(operacao.Data)),

        # Operacao
        "operacao_Numero":  operacao.Numero,
        "Face": real_br_money_mask(operacao.Face),
        "Compra": real_br_money_mask(operacao.Compra),
        "Despesa_Servico": real_br_money_mask(operacao.DepServico),
        "Despesa_Adicional": real_br_money_mask(operacao.DesAdicional),
        "Despesas_Adicional_Servico": real_br_money_mask(c),
        "Advalorem": real_br_money_mask(operacao.Advalorem),
        "percentualAdvalorem": real_br_money_mask(operacao.PercAdvalorem),
        "face_menos_Compra": real_br_money_mask(facemenoscompra),
        "Iof_mais_liquido": real_br_money_mask(desembolso),
        "IOF": real_br_money_mask(operacao.IOF),
        "desembolso_menos_iof": real_br_money_mask(desembolsosemiof),
        "liquido": real_br_money_mask(operacao.Liquido),
        "liberar": real_br_money_mask(operacao.Liberar),
        "extenso": e.extenso_unidade,
        "ISS": real_br_money_mask(operacao.ISS),
        "MaxDataItens": operacao.MaxDataItens,
        "dataporextensoMaxDataItens": dataporextensoMaxDataItens,
        "extensonp": np.extenso_unidade,

        # Itens
        "itens": itens,
        "styleHeaderItens": styleHeaderItens,
        "itensTotal": itensTotal
    }

    # Adiciona ao dicionario
    params["templateVars"] = valoresAtribuidos

    return params
