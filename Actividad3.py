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
