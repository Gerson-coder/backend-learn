"""
  7. Contador de vocales:
  dada una palabra, contá cuántas vocales tiene.
"""


def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


def main():
    palabra = input("Escribí una palabra: ")
    cantidad = contar_vocales(palabra)
    print(f'La palabra "{palabra}" tiene {cantidad} vocales')


if __name__ == "__main__":
    main()
