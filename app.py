notas = []

while True:
    print("\n--- REGISTRO DE NOTAS ---")
    print("1. Registrar nota")
    print("2. Ver promedio")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            nota = float(input("Ingrese la nota (0 a 20): "))
            if 0 <= nota <= 20:
                notas.append(nota)
                print("Nota registrada correctamente")
            else:
                print("La nota debe estar entre 0 y 20")
        except ValueError:
            print("Ingrese un valor numérico válido")
    elif opcion == "2":
        if notas:
            promedio = sum(notas) / len(notas)
            print(f"Promedio: {promedio:.2f}")
        else:
            print("No hay notas registradas")
    elif opcion == "3":
        print("Programa finalizado")
        break
    else:
        print("Opción no válida")