def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    password = input("Ingrese una contrasenia: ")

    corta = len(password) < 8

    tiene_num = ("0" in password or "1" in password
        or "2" in password or "3" in password or "4" in password
        or "5" in password or "6" in password or "7" in password
        or "8" in password or "9" in password)

    sin_num = not tiene_num

    if corta and sin_num:
        print("Contraseña muy corta")
        print("Debe contener un numero")
    elif corta:
        print("Contraseña muy corta")
    elif sin_num:
        print("Debe contener un numero")
    else:
        print("Contraseña valida")
