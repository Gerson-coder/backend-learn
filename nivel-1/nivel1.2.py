
from datetime import datetime

# nivel 1.2

def calcular_edad(anio_nacimiento):
    anio_actual = datetime.now().year
    return anio_actual - anio_nacimiento


anio_nacimiento = int(input("Indica tu fecha de nacimiento: "))
año = calcular_edad(anio_nacimiento)
print (f'tu fecha de nacimiento es: {anio_nacimiento}  y en el 2026 tu edad sera {año}')

    

