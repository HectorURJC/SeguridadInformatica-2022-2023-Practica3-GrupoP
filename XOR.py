# Para desencriptar y encriptar un mensaje en XOR se realiza con la misma implementación
# por tanto, reutilizamos la misma función para desencriptar y encriptar, pero se podría
# hacer en 2 funciones.
def desencriptar_encriptar_XOR(mensaje = "+*5-=;¡.61!47=?9;;;.", clave = "XOR"):
    solucion = ""
    for i in range(len(mensaje)):
        # Se usa el operador ^ que realiza bit a bit la operación XOR 
        # Se utiliza el ord() para poder trabajar con los valores de cada letra en ASCII
        letra_texto = chr(ord(mensaje[i]) ^ ord(clave[i % len(clave)])) # Se cambia su valor decimal por su letra correspondiente
        solucion += letra_texto
    return solucion

mensaje_encriptado = input("Escriba el mensaje encriptado: \n").strip()
clave = input("Escriba la clave: \n").strip()

# Si el input del texto encriptado y/o el de la clave son vacíos, entonces se le pasa el texto encriptado y/o clave del enunciado
if mensaje_encriptado == "":
    mensaje_encriptado = "+*5-=;¡.61!47=?9;;;."
if clave == "":
    clave = "XOR"

solucion_desencriptada = desencriptar_encriptar_XOR(mensaje_encriptado, clave)
solucion_encriptada = desencriptar_encriptar_XOR(solucion_desencriptada, clave)

print(solucion_desencriptada)
print(solucion_encriptada)
