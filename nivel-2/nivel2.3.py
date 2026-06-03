"""
6. Año bisiesto: dado un año, determiná si es bisiesto.
   Regla: divisible por 4, EXCEPTO si es divisible por 100,
   PERO si es divisible por 400 entonces SÍ es bisiesto.
"""


def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def main():
    anio = int(input("Escribí un año: "))

    if es_bisiesto(anio):
        print(f'El año {anio} es bisiesto')
    else:
        print(f'El año {anio} no es bisiesto')


if __name__ == "__main__":
    main()
