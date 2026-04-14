#Este código implementa un ataque de fuerza bruta para descifrar un mensaje cifrado con el método César. El programa intentará todas las posibles combinaciones de desplazamiento (de 1 a 25) y mostrará el resultado para cada uno, permitiendo al usuario identificar cuál es el texto original.

def fuerza_bruta_cesar(texto_cifrado):
    ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for desplazamiento in range(1, 26):  # Probar todos los desplazamientos posibles
        resultado = ""
        
        for char in texto_cifrado:
            if char.isalpha():  # Verificar si el carácter es una letra
                inicio = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - inicio - desplazamiento) % 26 + inicio)
            else:
                resultado += char  # Si no es una letra, se deja sin cambios
        
        print(f"Desplazamiento {desplazamiento}: {resultado}")

# Pedir al usuario el texto cifrado
texto_cifrado = input("Ingresa el texto cifrado: ")
fuerza_bruta_cesar(texto_cifrado)


#2 Ejemplo

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
criptograma = input("Introduce el texto cifrado:")
print("Iniciando ataque de fuerza bruta...")

# Recorre una a una todas las claves (1-25)
for clave in range(1, (ALFABETO)):

    salida = "" # Almacena la cadena descifrada
    for simbolo in criptograma:
        if simbolo in ALFABETO:
            pos = ALFABETO.find(simbolo)
            pos = (pos - clave) % len(ALFABETO)
            salida += ALFABETO[pos]
        else:
            salida += simbolo  # Si no es una letra, se deja sin cambios