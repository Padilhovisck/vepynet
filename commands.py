import json

def openfilejson(filenameJson):
    try:
        with open(filenameJson, 'r') as data_file:
            jsonobjectinfo = json.loads(data_file.read())
            return jsonobjectinfo
    except Exception as erro:
        return 'Retorno do erro', erro