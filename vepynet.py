# main.exe 0 "AditivoOurolacOp100.pdf"
# "C:\Users\eduar\PycharmProjects\vepynet\build\vepynet\File\AditivoOurolacOp100.json"
# "C:\Users\eduar\PycharmProjects\vepynet\bin\wkhtmltopdf.exe"

import sys

from commands import openfilejson, gravar_arquivo
from importacao import resultSetData

if len(sys.argv) == 5:

    if (int(sys.argv[1])) == 0 or (int(sys.argv[1])) == 1:
        parms = {'document': sys.argv[1],
                 'templatehtml': 'xxx', 'namefilepdf': sys.argv[2],
                 'filejson': sys.argv[3],
                 'wkhtmltopdf': sys.argv[4]}

        retorno = openfilejson((parms['filejson']))

        if retorno == False:
            gravar_arquivo('log.txt', ('Abrindo arquivo Json <error:' + str(retorno) + '>'))
        else:
            resultSetData(parms, openfilejson((parms['filejson'])))
    else:
        gravar_arquivo('log.txt', 'Parametro tem que ser 0 ou 1.')
else:
    gravar_arquivo('log.txt', 'Número de parâmetros errado.')
