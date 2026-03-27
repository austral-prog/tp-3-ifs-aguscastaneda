def calculator():
    """
    Ejercicio 7 - Calculadora Simple

    Leer dos números (pueden ser decimales) y una operación (+, -, *, /) mediante input().
    Realizar la operación correspondiente e imprimir el resultado.

    Validaciones:
    - Si la operación es inválida, imprimir "Operacion invalida"
    - Si es división y el divisor es cero, imprimir "Error: division por cero"

    Ejemplo:
        Para las entradas "10", "5" y "+", la salida esperada es:
        Resultado: 15.0

        Para las entradas "10", "2" y "/", la salida esperada es:
        Resultado: 5.0

        Para las entradas "10", "0" y "/", la salida esperada es:
        Error: division por cero

        Para las entradas "10", "5" y "x", la salida esperada es:
        Operacion invalida
    """
    n1 = float(input())
    n2 = float(input())
    opreacion = input()

    if opreacion == "+":
        print("Resultado:", n1 + n2)
    elif opreacion == "-":
        print("Resultado:", n1 - n2)
    elif opreacion == "*":
        print("Resultado:", n1 * n2)
    elif opreacion == "/" and (n1 == 0 or n2 == 0):
        print("Error: division por cero")
    elif opreacion == "/" and n1 != 0 and n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Operacion invalida")
    
