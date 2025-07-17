print(f"\nCALCULADORA\nPor favor seleccione la operación que desea realizar\n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n5.- Potenciación\n6.- Raíz cuadrada")
op = int(input("Escriba el número de la opción que desea seleccionar: "))
if op == 1:
    print("SUMA")
    can = int(input("Ingrese la cantidad de números que sumará: "))
    suma = 0
    for i in range(can):
        num = int(input(f"Ingrese la cantidad #{i+1} que sumará: "))
        suma += num
    print(f"El total de la suma es: {suma}")
elif op == 2:
    print("RESTA")
    cant1 = int(input("Ingresa la primer cantidad: "))
    cant2 = int(input("Ingresa la segunda cantidad que restará: "))
    resp = cant1 - cant2
    print(f"El resultado de la resta es: {resp}")
elif op == 3:
    print("MULTIPLICACIÓN")
    multi1 = int(input("Ingresa la primera cantidad: "))
    multi2 = int(input("Ingresa la segunda cantidad a multiplicar: "))
    resp = multi1 * multi2
    print(f"El resultado de la multiplicación es: {resp}")
elif op == 4:
    print('DIVISIÓN')
    div1 = int(input('Ingresa el dividendo: '))
    div2 = int(input('Ingresa el divisor: '))
    resp = div1/div2
    print(f'El resultado de la división es: {resp}')
elif op == 5:
    print('POTENCIACIÓN')
    base = int(input('Ingrese la base: '))
    exp = int(input('Ingrese el exponente: '))
    resp = base ** exp
    print(f'El resultado de la potencia es: {resp}')
elif op == 6:
    print('RAÍZ CUADRADA')
    root = int(input('Ingrese el número al que desea aplicar raíz cuadrada: '))
    resp = root ** (1/2)
    print(f'El resultado de la raíz cuadrada es: {resp}')