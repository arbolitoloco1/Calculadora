print("Bienvenido a la Calculadora Python")

reiniciar = True

while reiniciar == True:
    print("1- Suma (+)")
    print("2- Resta (-)")
    print("3- Multiplicación (*)")
    print("4- División (/)")
    
    tipo_de_operacion = int(input("Elegí una operación: "))
    if tipo_de_operacion == 1:
        num1 = int(input("Ingresar primer número: "))
        num2 = int(input("Ingresar segundo número: "))
        resultado = num1 + num2
        print(resultado)
        reiniciar = input("Querés hacer otra operación? S/N: ")
        if reiniciar == "S" or reiniciar == "s":
            reiniciar = True
        else:
            reiniciar = False
    elif tipo_de_operacion == 2:
        num1 = int(input("Ingresar primer número: "))
        num2 = int(input("Ingresar segundo número: "))
        resultado = num1 - num2
        print(resultado)
        input("Querés hacer otra operación? S/N: ")
        if reiniciar == "S" or reiniciar == "s":
            reiniciar = True
        else:
            reiniciar = False
    elif tipo_de_operacion == 3:
        num1 = int(input("Ingresar primer número: "))
        num2 = int(input("Ingresar segundo número: "))
        resultado = num1 * num2
        print(resultado)
        input("Querés hacer otra operación? S/N: ")
        if reiniciar == "S" or reiniciar == "s":
            reiniciar = True
        else:
            reiniciar = False
    elif tipo_de_operacion == 4:
        num1 = int(input("Ingresar primer número: "))
        num2 = int(input("Ingresar segundo número: "))
        resultado = num1 / num2
        print(resultado)
        input("Querés hacer otra operación? S/N: ")
        if reiniciar == "S" or reiniciar == "s":
            reiniciar = True
        else:
            reiniciar = False
    else:
        print("Error")
        input("Querés hacer otra operación? S/N: ")
        if reiniciar == "S" or reiniciar == "s":
            reiniciar = True
        else:
            reiniciar = False