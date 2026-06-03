"""
 10. Reemplazo manual: dado un texto,
   reemplazá todos los espacios por guiones bajos 
   SIN usar .replace(). (Tenés que
  pensar con un loop).
"""

def convertir_texto(texto):
    resultado = ""

    for letra in texto:
        if letra == " ":
            resultado += "_"
        else:
            resultado += letra
    return resultado

        

    

def main():
 
    texto = input("escribe un texto para convertirlo en guion ")
    resultado  = convertir_texto(texto)
    print(f'el resultado es {resultado}')
 



if __name__ == "__main__":

    main()

