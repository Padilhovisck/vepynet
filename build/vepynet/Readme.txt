[PARAMETROS]
0 - vepynet.exe  : nome do executavel
1 - Documentos	 : [0-aditivo; 1-contrato]
2 - N. de doctos : [1-4] - [1-Aditivo; 2-Recibo; 3-Nota Promissoria; 4-conta grafica]
3 - Nome do PDF  : nome do arquivo PDF a ser gerado
4 - Arquivo Json : arquivo gerado pelo vmoney
5 - PDF (exe)	 : programa que converte html to pdf (wkhtmltopdf.exe)

[EXEMPLO] - Prompt de comando:

...\vepynet.exe 0 [1-1] "nomedoarquivo.pdf" "...\vepynet\File\linha.json" "...\vepynet\bin\wkhtmltopdf.exe"