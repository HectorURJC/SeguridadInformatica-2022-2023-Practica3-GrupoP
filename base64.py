from base64 import b64decode, b64encode

solucion_desencriptada = b64decode("MjAyM19TZWd1cmlkYWRJbmZvcm1hdGljYUJhc2U2NA==").decode('utf-8')
# Se devuelve con un decode de tipo utf-8 porque la función b64decode devuelve
# el string en el tipo byte.
print(solucion_desencriptada)
solucion_encriptada = b64encode(solucion_desencriptada.encode('utf-8')).decode('utf-8')
# Se codifica a utf-8 porque la función b64encode solo acepta parámetros de tipo
# byte y lo volvemos a decodificar para que nos devuelva el resultado esperado.
print(solucion_encriptada)