from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def desencriptar_AES(cifrador, texto_encriptado = "9bc43d7ec1aa11f64302287b17be9f7b"):
    texto_desencriptado = cifrador.decrypt(bytes.fromhex(texto_encriptado)) # Se modifica el formato del texto de hexadecimal a bytes.
    # En el enunciado no especifica la longitud del bloque, por tanto se usará la estándar,
    # AES:block_size (que son 16 bytes (128 bits)). 
    # Con el unpad se elimina el relleno innecesario de los datos desencriptados.
    solucion_desencriptada = unpad(texto_desencriptado, AES.block_size)
    return solucion_desencriptada.decode('utf-8') # Lo convertimos al formato estándar utf-8 para que sea entendible y legible para un usuario.

def encriptar_AES(cifrador, texto_desencriptado):
    # Con el pad se añade relleno para que los datos al encriptar tengan la longitud necesaria
    # para ser múltiplo del bloque de cifrado.
    texto_padded = pad(texto_desencriptado.encode('utf-8'), AES.block_size) # Se modifica el formato del texto de utf-8 a bytes.
    solucion_encriptada = cifrador.encrypt(texto_padded)
    return solucion_encriptada.hex() # Lo convertimos a hexadecimal que es el formato correspondiente que tiene el mensaje original.

texto_encriptado = input("Escriba el texto encriptado: \n").strip()
clave = input("Escriba la clave: \n").strip()
iv = input("Escriba el iv: \n").strip()

# Si el input del texto encriptado, clave y/o iv son vacíos, entonces se le pasa el texto encriptado, clave y/o iv del enunciado
if texto_encriptado == "":
    texto_encriptado = "9bc43d7ec1aa11f64302287b17be9f7b"
if clave == "":
    clave = 'SeguridadInforma' 
if iv == "":
    iv = 'SeguridadInforma' 
clave = bytes(clave, 'utf-8') # Se modifica el string a un array de bytes
iv = bytes(iv, 'utf-8') # Se modifica el string a un array de bytes

# AES.new(clave, AES.MODE_CBC, iv) no se le puede asignar a una variable global porque no
# se puede cifrar una vez que se ha usado la función decrypt() y lo mismo con encrypt()
solucion_desencriptada = desencriptar_AES(AES.new(clave, AES.MODE_CBC, iv), texto_encriptado)
solucion_encriptada = encriptar_AES(AES.new(clave, AES.MODE_CBC, iv), solucion_desencriptada)

print("Solución desencriptada: " + solucion_desencriptada)
print("Solución encriptada: " + solucion_encriptada)
