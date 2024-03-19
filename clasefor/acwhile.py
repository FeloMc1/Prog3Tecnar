def menu():
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")



while True:
    menu()
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        print("Hola, has elegido la opción Personas")
    if opcion == 2:
        print("Hola, has elegico la opción Vehiculos")
    if opcion == 3:
        print("Hola, has elegido la opción Universidades")
    if opcion == 4:
        print("Hola, has elegido la opción Notas")
    if opcion == 5:
        print("Gracias por usar nuestro servicio")
        break