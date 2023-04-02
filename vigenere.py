def desencriptar_vigenere(texto_encriptado, clave="Vigenere"):
    solucion_desencriptada = ""
    for i in range(len(texto_encriptado)):
        # Se puede trabajar tanto con el método lower() como upper, la única regla para que se cumpla correctamente la desencriptación y
        # la encriptación es que el mensaje y la clave estén en el mismo formato para poder trabajar correctamente con la función
        # ord, sino se cumple la regla puede que falle en alguna letra en la encriptación y/o desencriptación. El 26 corresponde,
        # a las letras del abecedario y el 65 es el número ASCII cuando aparece la primera letra.
        letra_desencriptada = chr(((ord(texto_encriptado.upper()[i]) - ord(clave.upper()[i % len(clave)])) % 26) + 65)
        # Se comprueba si la letra tiene que ir en mayúscula o minúscula dependiendo del mensaje original.
        solucion_desencriptada += letra_desencriptada if texto_encriptado[i].isupper() else letra_desencriptada.lower()
    return solucion_desencriptada

def encriptar_vigenere(texto_desencriptado, clave="Vigenere"):
    solucion_encriptada = ""
    for i in range(len(texto_desencriptado)):
        letra_encriptada = chr(((ord(texto_desencriptado.upper()[i]) + ord(clave.upper()[i % len(clave)])) % 26) + 65)
        solucion_encriptada += letra_encriptada if texto_desencriptado[i].isupper() else letra_encriptada.lower()
    return solucion_encriptada

texto_encriptado = "QqmiaiiiYmisqmwmxijs"
clave = "Vigenere"

solucion_desencriptada = desencriptar_vigenere(texto_encriptado, clave)
print(solucion_desencriptada)
solucion_encriptada = encriptar_vigenere(solucion_desencriptada, clave)
print(solucion_encriptada)