"""

  8. Palíndromo: pedile una palabra
    y decile si se lee igual al derecho 
    y al revés (ej: "neuquen","reconocer").
"""


def palindromo(palabra):

    return palabra[::-1] == palabra



    



def main():

    palabra = input("Escribe una palabra para poner al revés: ")
    if palindromo(palabra):
        print(f'La palabra {palabra} es palindromo')
    else:
        print( f'La palabra {palabra} no es palindromo')
    

    
   


if __name__ == "__main__":

    main()
