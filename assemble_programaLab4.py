def entero_a_binario():
    """
    Función para convertir un número entero a binario de 8 bits.
    """
    num = int(input("Ingrese un número entero: "))
    binario = format(num, '08b')
    print("El número binario de 8 bits es: ", binario)

def binario_a_complemento_dos():
    """
    Función para convertir un número binario de 8 bits a su complemento a dos.
    """
    binario = input("Ingrese un número binario de 8 bits: ")
    if binario[0] == '1':
        complemento = binario.translate(str.maketrans('01', '10'))
        complemento = bin(int(complemento, 2) + 1)[2:].zfill(8)
    else:
        complemento = binario
    print("El complemento a dos es: ", complemento)
    

def hexadecimal_a_decimal_y_viceversa():
    """
    Función para convertir un número hexadecimal de 3 dígitos a decimal y viceversa.
    """
    entrada = input("Ingrese un número hexadecimal de 3 dígitos o un número decimal: ")
    if '.' in entrada:
        try:
            decimal = float(entrada)
            hexadecimal = '{:x}'.format(int(decimal))
            print("El número hexadecimal es: ", hexadecimal.upper())
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    else:
        if entrada.isdigit():
            decimal = int(entrada)
            hexadecimal = '{:03x}'.format(decimal)
            print("El número hexadecimal es: ", hexadecimal.upper())
        else:
            try:
                if len(entrada) == 3:  # Verificamos si la entrada es un número hexadecimal de 3 dígitos
                    decimal = int(entrada, 16)
                    print("El número decimal es: ", decimal)
                else:  # Si no es de 3 dígitos, convertimos el número decimal a hexadecimal
                    decimal = int(entrada)
                    hexadecimal = '{:x}'.format(decimal)
                    print("El número hexadecimal es: ", hexadecimal.upper())
            except ValueError:
                print("Entrada no válida. Intente de nuevo.")




while True:
    

    print("\n1. Convertir entero a binario de 8 bits")
    print("2. Convertir binario de 8 bits a complemento a dos")
    print("3. Convertir hexadecimal a decimal y viceversa")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        entero_a_binario()
    elif opcion == 2:
        binario_a_complemento_dos()
    elif opcion == 3:
        hexadecimal_a_decimal_y_viceversa()  
    elif opcion == 4:
        break
    else:
        print("Opción no válida. Intente de nuevo.")