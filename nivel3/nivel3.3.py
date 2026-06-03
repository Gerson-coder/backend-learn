"""
 9. Iniciales: dado un nombre completo
   ("Juan Pablo Pérez"), devolvé las iniciales: "J.P.P."

"""




  
def calcular_iniciales(nombre_completo):
      palabras = nombre_completo.split()
      iniciales = []

      for palabra in palabras:
          primera_letra = palabra[0].upper()
          iniciales.append(primera_letra)

      resultado = ".".join(iniciales) + "."
      return resultado






def  main():

    nombre_completo = input("Escribe tu nombre completo: ")
    resultado = calcular_iniciales(nombre_completo)

    print(resultado)

if __name__ == "__main__":
    main()