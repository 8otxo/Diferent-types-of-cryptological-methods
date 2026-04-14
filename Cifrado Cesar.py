# Esta código implementa el cifrado César, que es un tipo de cifrado por sustitución en el que cada letra del texto se reemplaza por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto.

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():  # Verificar si el carácter es una letra
            # Determinar el punto de inicio dependiendo de si es mayúscula o minúscula
            inicio = ord('A') if char.isupper() else ord('a')
            # Aplicar el desplazamiento y asegurarse de que se mantenga dentro del alfabeto
            resultado += chr((ord(char) - inicio + desplazamiento) % 26 + inicio)
        else:
            resultado += char  # Si no es una letra, se deja sin cambios
    
    return resultado

# Pedir al usuario la palabra y el desplazamiento
texto_original = input("Ingresa la palabra a cifrar: ")
desplazamiento = int(input("Ingresa el número de posiciones: "))
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print(f"Texto original: {texto_original}")
print(f"Texto cifrado: {texto_cifrado}")


# 2 Ejemplo

print("Este ejemplo cifra o descifra un mensaje utilizando el cifrado César.")

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SALIDA = ""

modo = input("¿Deseas cifrar o descifrar? (c/d): ")
texto = input("Ingresa el mensaje: ")
clave = int(input("Ingresa el número de posiciones para el desplazamiento: "))

for simbolo in texto.upper():
    if simbolo in ALFABETO:
        pos = ALFABETO.find(simbolo)
        if modo == 'c':
            indice = (indice +
        SALIDA += ALFABETO[indice]
    else:
        SALIDA += letra  # Si no es una letra, se deja sin cambios