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
    cant1 = int(input("Ingrea la primer cantidad: "))
    cant2 = int(input("Ingresa la segunda cantidad que restará: "))
    resp = cant1 - cant2
    print(f"El resultado de la resta es: {resp}")
elif op == 3:
    print("MULTIPLICACIÓN")
    multi1 = int(input("Ingresa la primera cantidad: "))
    multi2 = int(input("Ingresa la segunda cantidad a multiplicar: "))
    resp = multi1 * multi2
    print(f"El resultado de la multiplicación es: {resp}")