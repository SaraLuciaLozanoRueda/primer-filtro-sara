import json
import os
MY='data/generos.json'
peliculas={}
#Leer y precargar archivo
def read():
    with(MY,'r') as rf:
        return json.load(rf)
#Crear archivo
def crear(*args):
    with open(MY,'w') as wf:
        json.dump(args[0],wf,indent=4)
#Verificar archivo
def checkFile(*args):
    data=list(args)
    if os.path.isfile(MY):
        if len (args):
            data[0].update(read())
        else:
            if len(args):
                crear(data[0])
#agregar datos
def addData(*args):
    with open (MY,'r+') as rwf:
        data_File=json.load(rwf)
    if os.path.isfile(MY):
        if len (args)>1:
            data_File.update({args[0]:args[1]})
        else:
            data_File.update(args[0])
        rwf.seek(0)
        json.dump(data_File,rwf,indent=4)
        rwf.close()
#Eliminar
def eliminar(*args):
    data=list(args)
    data[1].pop(data[0])
    crear(data[1])

