import json
import os
import pandas as pd

##Hay que ejecutar el primer ejercicio para que funcione este.

nombreArchivo = f"usuarios.xlsx"

if os.path.isfile(nombreArchivo):
    print("")
else:
    with open('secure-users.json', 'r') as usuarios:
        data = json.load(usuarios)

    df = pd.DataFrame(data)
    df.to_excel(nombreArchivo)


