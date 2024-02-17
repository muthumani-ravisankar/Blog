import json
def getConfig(key):
    con_file=r"c:\\Users\muthu\playground\blog\config.json"
    file=open(con_file,'r')
    config=json.loads(file.read())
    file.close()
    if key in config:
        return config[key]
    else:
        raise Exception("string {} is not found".format(key))