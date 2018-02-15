import requests
import base64

with open("C:\\Users\\eduar\PycharmProjects\\vepynet\PDF\\AditivoOurolacOp100.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())

r = requests.post('http://localhost:5000/api/values',
                  json={"NumeroDoLote": 10522,
                        "Cliente": 'ZFAC FOMENTO MERCANTIL LTDA',
                        "Cedente": 'OUROLAC IND. BRASILEIRA ME',
                        "Filename": encoded_string.decode('utf-8')
                        }
                  )
print(r.status_code)
print(r.json())
