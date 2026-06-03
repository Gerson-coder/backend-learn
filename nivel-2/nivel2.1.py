#  Par o impar: pedile un número al usuario y decile si es par o impar. (Usá el operador módulo %).



def es_par(numero):

    return numero % 2 == 0




numero = int(input("Escribe un numero: "))
if es_par(numero):
    print(f'El numero {numero} es par')
else:
    print(f'el numero {numero} es impar')



