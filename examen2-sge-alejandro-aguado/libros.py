import json
import os
from datetime import datetime

import pandas as pd

ruta = "users.json"
ruta2 = "libraries-and-books.json"

def crear(ruta2):
    try:
       open(ruta2, 'a').close()
       return "Archivo creado"
    except Exception as e:
       return f"Error al crear el archivo: {e}"

if crear(ruta2):
    print("")

with open(ruta, 'r') as usuarios:
    data = json.load(usuarios)

    user = data[0]
    userId = user['userId']
    book = user['books']


    libro1 = {
        'IdCliente': userId,
        'Libros': book
    }

    user = data[1]
    userId = user['userId']
    book = user['books']


    libro2 = {
        'IdCliente': userId,
        'Libros': book
    }

    user = data[2]
    userId = user['userId']
    book = user['books']

    libro3 = {
        'IdCliente': userId,
        'Libros': book
    }

    user = data[3]
    userId = user['userId']
    book = user['books']

    libro4 = {
        'IdCliente': userId,
        'Libros': book
    }

    user = data[4]
    userId = user['userId']
    book = user['books']

    libro5 = {
        'IdCliente': userId,
        'Libros': book
    }

with open(ruta2, 'r+') as f:
    try:
        data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {'libros': []}
    data.setdefault('libros', []).append(libro1)
    data.setdefault('libros', []).append(libro2)
    data.setdefault('libros', []).append(libro3)
    data.setdefault('libros', []).append(libro4)
    data.setdefault('libros', []).append(libro5)


    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    f.seek(0)
    json.dump(data, f, indent=4)


fechaActual = datetime.now().strftime('%d-%B')
nombreArchivo = f"{fechaActual}-libros-presentados.xlsx"

if os.path.isfile(nombreArchivo):
    print("")
else:
    with open('libraries-and-books.json', 'r') as employees_json:
        employees_data = json.load(employees_json)

    df = pd.DataFrame(employees_data)
    df.to_excel(nombreArchivo)



