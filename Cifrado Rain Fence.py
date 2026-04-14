#Este código implementara ek cifrado con el método de cifrado Rail Fence (zig zag), que es un tipo de cifrado por transposición en el que las letras del mensaje se escriben en un patrón de zigzag a lo largo de varias filas, y luego se leen en orden para formar el texto cifrado.

def cifrado_rail_fence(texto, num_rails):
    if num_rails <= 1:
        return texto  # No se puede cifrar con menos de 2 rieles

    # Crear una matriz para almacenar los caracteres en zigzag
    rail = [['\n' for i in range(len(texto))] for j in range(num_rails)]

    # Llenar la matriz en zigzag
    dir_down = False
    row, col = 0, 0

    for char in texto:
        if char != ' ':  # Ignorar espacios
            if row == 0 or row == num_rails - 1:
                dir_down = not dir_down
            
            rail[row][col] = char
            col += 1
            
            row += 1 if dir_down else -1

    # Leer la matriz en zigzag para formar el texto cifrado
    resultado = ""
    for i in range(num_rails):
        for j in range(len(texto)):
            if rail[i][j] != '\n':
                resultado += rail[i][j]

    return resultado

# Pedir al usuario la palabra y el número de rieles
texto_original = input("Ingresa la palabra a cifrar: ")
num_rails = int(input("Ingresa el número de rieles: "))
texto_cifrado = cifrado_rail_fence(texto_original, num_rails)
print(f"Texto original: {texto_original}")
print(f"Texto cifrado: {texto_cifrado}")

#Este código tiene una complejifad de O(n) debido a que recorre el texto original una vez para llenar la matriz y luego recorre la matriz para formar el texto cifrado.

# 2 Ejemplo
