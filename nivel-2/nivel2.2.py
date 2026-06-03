 # 5. Calculadora simple: pedile dos números y una operación (+, -, *, /) y mostrá el resultado.


def calcular(num1,num2,operacion):
    try:

        if operacion == "+":
            return  num1 + num2
        elif operacion == "-":
            return  num1 - num2
        elif operacion == "*":
            return num1 * num2 
        elif  operacion == "/":
            return  num1 / num2
    except:
        return 'elija una opcion valida'
        





def main():
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("Ingrese el segundo numero:"))
    operacion = input("Ingrese una operacion: + , -, *: ")

    resultado = calcular(num1, num2,operacion)

    print(f' el resultado de la operacion es: {resultado}')

if __name__ == "__main__":
    main()



