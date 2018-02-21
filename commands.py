import json

# Open File Json
def openfilejson(filenameJson):
    try:
        with open(filenameJson, 'r', encoding="utf-8") as data_file:
            jsonobjectinfo = json.loads(data_file.read())
            return jsonobjectinfo
    except Exception as erro:
        return False

# Criar arquivo TXT
def criar_arquivo(arq):
    with open(arq, "a") as f:
        f.close()

# Contar linhas de um arquivo TXT
def contar_linhas_arquivo(arq):
    with open(arq, 'r') as f:
        t = len(f.readlines())
        f.close()
        return (t)

# Listar conteúdo de um arquivo TXT
def listar_arquivo(arq):
    with open(arq, 'r') as f:
        r = f.read()
        print('Conteúdo do arquivo:')
        print(r)

# Gerar Array a partir de TXT
def txt_para_array(arq):
    print('Lista conteúdo TXT em Array:')
    with open(arq, 'r') as f:
        c = f.read()
        valores = c.split('\n')
        for e in valores:
            print(e)

        print('Total linhas Array', (len(valores) - 1))

# Abrir TXT Append Mode e grava uma linha
def gravar_arquivo(arq, t):
    with open(arq, "a", encoding='utf-8') as f:
        # Grava uma linha no TXT
        f.write(str(t) + '\n')
        f.close()

# Processa arquivo TXT incluindo uma linha
def processar_arquivo(arq, t):
    # Verifica se arquivo existe, se não exitir cria
    try:
        # Se arquivo existir conta o número de linhas
        with open(arq, 'r') as f:
            print('Arquivo já existe!\n')
            f.write(str(t) + ' - Appended text\n')
            f.close()
    except IOError:
        # Se arquivo não existir Cria o arquivo
        print('Arquivo nãoexiste - Criado!\n')
        gravar_arquivo(arq, t)

    # Abrir TXT Append Mode e grava uma linha
    #gravar_arquivo('teste.txt', 'Olá')

    # # Lista o conteúdo do TXT
    # listar_arquivo(arq)
    #
    # # Contar linhas de um arquivo TXT
    # print('Total Linhas:', contar_linhas_arquivo(arq), '\n')
    #
    # txt_para_array(arq)
    #
    # # Define o caminho do arquivo usado
    # arq = 'D:\\temp\\Phyton\\teste.txt'
    #
    # # Processa o arquivo acima e inclui uma linha
    # processar_arquivo(arq)
