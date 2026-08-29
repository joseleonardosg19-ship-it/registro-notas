from notas import registrar_nota, calcular_promedio


while True:

    print("\n--- REGISTRO DE NOTAS ---")
    print("1. Registrar nota")
    print("2. Ver promedio")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_nota()

    elif opcion == "2":
        calcular_promedio()

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")