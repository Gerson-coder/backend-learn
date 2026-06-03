
# nivel 1
def calcular_temp(celsius):

    
    resultado = celsius * 9/5 + 32
    return resultado

celsius= float(input('Ingresa la temperatura en celsius: '))
fahrenheit = calcular_temp(celsius)

print (f'{celsius} equivale a: {fahrenheit} F')

    

