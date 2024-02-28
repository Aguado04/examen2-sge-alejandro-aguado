import json
import hashlib

ruta = "secure-users.json"
ruta2 = "users.json"

def crear(ruta):
    try:
       open(ruta, 'a').close()
       return "Archivo creado"
    except Exception as e:
       return f"Error al crear el archivo: {e}"

if crear(ruta):
    print("")

with open(ruta2, 'r') as usuarios:
    data = json.load(usuarios)
    print(data)

    user = data[0]
    userId = user['userId']
    password = user['password']
    print(password)
    contHash2 = hashlib.sha256(password.encode()).hexdigest()

    usuario1 = {
        'IdCliente': userId,
        'Password': contHash2
    }

    user = data[1]
    userId = user['userId']
    password = user['password']
    print(password)
    contHash2 = hashlib.sha256(password.encode()).hexdigest()

    usuario2 = {
        'IdCliente': userId,
        'Password': contHash2
    }

    user = data[2]
    userId = user['userId']
    password = user['password']
    print(password)
    contHash2 = hashlib.sha256(password.encode()).hexdigest()

    usuario3 = {
        'IdCliente': userId,
        'Password': contHash2
    }

    user = data[3]
    userId = user['userId']
    password = user['password']
    print(password)
    contHash2 = hashlib.sha256(password.encode()).hexdigest()

    usuario4 = {
        'IdCliente': userId,
        'Password': contHash2
    }

    user = data[4]
    userId = user['userId']
    password = user['password']
    print(password)
    contHash2 = hashlib.sha256(password.encode()).hexdigest()

    usuario5 = {
        'IdCliente': userId,
        'Password': contHash2
    }

    with open(ruta, 'r+') as f:
        try:
            data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {'usuarios': []}
        data.setdefault('usuarios', []).append(usuario1)
        data.setdefault('usuarios', []).append(usuario2)
        data.setdefault('usuarios', []).append(usuario3)
        data.setdefault('usuarios', []).append(usuario4)
        data.setdefault('usuarios', []).append(usuario5)

        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
        f.seek(0)
        json.dump(data, f, indent=4)
        print("Usuario creado exitosamente.")









