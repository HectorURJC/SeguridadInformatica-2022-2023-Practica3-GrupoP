def desencriptar_cesar(texto_encriptado,n):
    solucion_desencriptada=""
    for letra in texto_encriptado:
        letra_cesar=ord(letra.upper()) + n # Se obtiene el decimal del char en ASCII en mayúscula, sumándole el desplazamiento
        if letra_cesar>ord('Z'):
            letra_cesar -= 26 # Si se obtiene un valor mayor a 90, por tanto para obtener su letra correspondiente se 
                              # le resta la longitud del alfabeto
        sol=chr(letra_cesar).lower() if letra.islower() else chr(letra_cesar) # Lo convertimos a su char correspondiente en ASCII
        solucion_desencriptada += sol
    return solucion_desencriptada

def encriptar_cesar(texto_desencriptado,n):
    solucion_encriptada=""
    for letra in texto_desencriptado:
        letra_cesar=ord(letra.upper()) - n # Se obtiene el decimal del char en ASCII en mayúscula, restándole el desplazamiento 
        if letra_cesar<ord('A'):
            letra_cesar += 26 # Si se obtiene un valor menor a 65, por tanto para obtener su letra correspondiente se
                              # le suma la longitud del alfabeto
        sol=chr(letra_cesar).lower() if letra.islower() else chr(letra_cesar) # Lo convertimos a su char correspondiente en ASCII
        solucion_encriptada += sol
    return solucion_encriptada

n=input().strip()# 6 es donde te da la clave oculta
n=int(n)
solucion_desencriptada = desencriptar_cesar("MyaolcxuxChzilguncwuWymul", n)
print(solucion_desencriptada)
solucion_encriptada = encriptar_cesar(solucion_desencriptada, n)
print(solucion_encriptada)