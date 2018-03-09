# vepynet.exe
# 0
# [1-1]
# "AditivoOurolacOp100.pdf"
# "C:\Users\eduar\PycharmProjects\vepynet\build\vepynet\File\AditivoOurolacOp100.json"
# "C:\Users\eduar\PycharmProjects\vepynet\bin\wkhtmltopdf.exe"

import sys

from commands import openfilejson, gravar_arquivo
from importacao import resultSetData

if len(sys.argv) == 6:

    if (int(sys.argv[1])) == 0 or (int(sys.argv[1])) == 1:
        parms = {'document': sys.argv[1], 'numberdocs': sys.argv[2],
                 'templatehtml': 'xxx', 'namefilepdf': sys.argv[3],
                 'filejson': sys.argv[4],
                 'wkhtmltopdf': sys.argv[5]}

        retorno = openfilejson((parms['filejson']))

        if retorno == False:
            gravar_arquivo('log.txt', ('Abrindo arquivo Json <error:' + str(retorno) + '>'))
        else:
            status_code = None
            status_code = resultSetData(parms, retorno)
            if status_code == 200:
                gravar_arquivo('log.txt', ('Arquivo enviado com sucesso!'))
            else:
                gravar_arquivo('log.txt', ('Problema ao enviar o arquivo <status:' + str(status_code) + '>'))
    else:
        gravar_arquivo('log.txt', 'Parametro tem que ser 0 ou 1.')
else:
    gravar_arquivo('log.txt', 'Número de parâmetros errado.')